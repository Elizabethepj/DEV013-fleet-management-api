from flask import Blueprint, jsonify
from sqlalchemy import func
from .models import db, Trajectories, Taxi
from sqlalchemy.sql import desc

last_trajectory = Blueprint('last_trajectory', __name__)


@last_trajectory.route('/last_trajectory', methods=['GET'])
def show_last_trajectory():
    # Subconsulta para obtener el último registro de cada taxi
    subquery = db.session.query(
        Trajectories.taxi_id,
        func.max(Trajectories.date).label('latest_date')
    ).group_by(
        Trajectories.taxi_id
    ).subquery()

    # Consulta principal para obtener la última ubicación de cada taxi
    last_location = db.session.query(
        subquery.c.taxi_id,
        Trajectories.longitude,
        Trajectories.latitude,
        Trajectories.date,
        Taxi.plate
    ).join(
        Trajectories,
        (Trajectories.taxi_id == subquery.c.taxi_id) & (
            Trajectories.date == subquery.c.latest_date)
    ).join(
        Taxi,
        Trajectories.taxi_id == Taxi.id
    ).distinct().all()  # distinct elimina filas duplicadas

    result = []

    for location in last_location:
        result.append({
            'taxi_id': location[0],
            'longitude': location[1],
            'latitude': location[2],
            'date': location[3],
            'plate': location[4]
        })

    print(result)
    length_last_location = len(result)
    print(length_last_location)

    return jsonify(result)

# func.max es el similar de max en python. Calcula el valor máximo.
# label permite darle un alias a la consulta resultante
# subquery:una consulta anidada dentro de otra
# with_entities se utiliza para identificar las columnas que se hace la consulta
# session por el congtrario ingresa a toda la base de datos


# @last_trajectory.route('/last_trajectory', methods=['GET'])
# def show_last_trajectory():
#     last_location = db.session.query(
#         Trajectories.taxi_id,
#         Taxi.plate,
#         func.max(Trajectories.date),
#         Trajectories.latitude,
#         Trajectories.longitude,
#     ).join(Taxi, Trajectories.taxi_id == Taxi.id
#            ).group_by(
#         Trajectories.taxi_id,
#         Taxi.plate,
#         Trajectories.latitude,
#         Trajectories.longitude,
#         Trajectories.date  # Incluir la columna date en GROUP BY
#     ).order_by(
#         Trajectories.taxi_id,
#         # Ordenar por fecha descendente dentro de cada grupo de taxi_id
#         desc(Trajectories.date)
#     ).all()

#     print(last_location)
#     length_last_location = len(last_location)
#     print(length_last_location)

#     return "Esto es un mensaje"
