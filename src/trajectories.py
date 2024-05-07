
from datetime import datetime
from flask import Blueprint, request, jsonify
from sqlalchemy import func
from .models import Trajectories

trajectories = Blueprint('trajectories', __name__)


@trajectories.route('/trajectories', methods=['GET'])
def show_trajectories():
    """Show all trajectories filtered by taxi_id"""

    # Get the taxi_id parameter from the request
    taxi_id = request.args.get("taxi_id")
    print("Taxi ID:", taxi_id)
    date = request.args.get('date')
    print("fecha", date)
    date = date.strip()

    # if not taxi_id return error
    if not taxi_id:
        return jsonify({"error": "Debe proporcionar el ID de taxi"}), 400

    # Convert the taxi_id to an integer
    taxi_id = int(taxi_id)

    if date:
        try:
            # become date in a python object
            date = datetime.strptime(date, '%Y-%m-%d').date()
        except ValueError:
            return jsonify({"error": "Ingrese la fecha en el formato YYYY-MM-DD"}), 400

    # filter trajectories by taxi_id and date
    trajectories_filter = Trajectories.query.filter(func.date(Trajectories.date) == date,
                                                    Trajectories.taxi_id == taxi_id)

    # Verify if there are trajectories
    if not trajectories_filter.first():  # first: verify if there are any results
        return jsonify({"error": "La identificación o la fecha proporcionada no existe en la base de datos"}), 404

    # pagination parameters
    limit = request.args.get("limit", default=10, type=int)
    page = request.args.get("page", default=1, type=int)

    # Calculate the index of the pagination
    offset = (page - 1) * limit

    # Paginate the filtered trajectories
    # trajectories_paginated = trajectories_filter.paginate(  # paginate is used to automatically handle pagination
    #     page=page, per_page=limit)

    # Filtrar las trayectorias por taxi_id con paginación
    trajectories_filter = Trajectories.query.filter(func.date(Trajectories.date) == date,
                                                    Trajectories.taxi_id == taxi_id
                                                    ).limit(limit).offset(offset).all()

    # Convert the Trajectories objects to dictionaries
    trajectories_dict = []
    for trajectory in trajectories_filter:
        trajectory_dict = {
            "id": trajectory.id,
            "taxi_id": trajectory.taxi_id,
            "datetime": trajectory.date.strftime('%Y-%m-%d %H:%M:%S'),
            "latitude": trajectory.latitude,
            "longitude": trajectory.longitude
        }
        trajectories_dict.append(trajectory_dict)

    # Return the filtered trajectories in JSON format
    return jsonify(trajectories_dict)


# http://localhost:5000/trajectories?taxi_id=6418&date=2008-02-02&page=10
# Route trajectories

# @trajectories.route('/trajectories', methods=['GET'])
# def show_trajectories():
#     """Show all trajectories filtered by taxi_id"""

#     # Obtener el parámetro taxi_id de la solicitud
#     taxi_id = request.args.get("taxi_id")
#     print("Taxi ID:", taxi_id)

#     # Si no se proporciona taxi_id, devolver un mensaje de error
#     if not taxi_id:
#         return jsonify({"error": "Debe proporcionar el ID de taxi"}), 400

#     # Convertir el taxi_id a un entero
#     taxi_id = int(taxi_id)

#     # pagination parameters
#     limit = request.args.get("limit", default=10, type=int)
#     page = request.args.get("page", default=1, type=int)

#     # Calcular el índice de inicio para la paginación
#     offset = (page - 1) * limit

#     # Filtrar las trayectorias por taxi_id con paginación
#     trajectories_filter = Trajectories.query.filter_by(taxi_id=taxi_id).limit(limit).offset(offset).all()

#     # Convertir los objetos Trajectories a diccionarios
#     trajectories_dict = []
#     for trajectory in trajectories_filter:
#         trajectory_dict = {
#             "id": trajectory.id,
#             "taxi_id": trajectory.taxi_id,
#             "datetime": trajectory.date.strftime('%Y-%m-%d %H:%M:%S'),
#             "latitude": trajectory.latitude,
#             "longitude": trajectory.longitude
#         }
#         trajectories_dict.append(trajectory_dict)

#     # Retornar las trayectorias filtradas en formato JSON
#     return jsonify(trajectories_dict)
