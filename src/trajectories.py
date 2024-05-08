
from datetime import datetime
from flask import Blueprint, request, jsonify
from sqlalchemy import func
from .models import Trajectories

trajectories = Blueprint('trajectories', __name__)


@trajectories.route('/trajectories', methods=['GET'])
def show_trajectories():
    """
    Gets the list of all trajectories.

    ---
    parameters:
      - name: page
        in: query
        type: integer
        required: false
        description: Page number for pagination.

      - name: per_page
        in: query
        type: integer
        required: false
        description: Number of items per page.

    responses:
      200:
        description: A list of taxis.
        schema:
          type: array
          items:
            type: object
            properties:
              id:
                type: integer
                description: The ID of the trajectory.
              taxi_id:
                type: string
                description: The ID of the associate taxi.
              date:
                type: string
                format: date-time
                description: The date and time of the trajectory
              latitude:
                type: float
                description: The latitude of the trajectory
              longitude:
                type: float
                description: The longitude of the trajectory

    """

    # Get the taxi_id parameter from the request
    taxi_id = request.args.get("taxi_id")
    # print("Taxi ID:", taxi_id)
    date = request.args.get('date')
    # print("fecha", date)

    # if not taxi_id return error
    if not taxi_id:
        return jsonify({"error": "Debe proporcionar el ID de taxi"}), 400

    # Convert the taxi_id to an integer
    taxi_id = int(taxi_id)

    if not date:
        date = date.strip()
        return jsonify({"error": "You must provide a date"})

    if date:
        try:
            # become date in a python object
            date = datetime.strptime(date, '%Y-%m-%d').date()
        except ValueError:
            return jsonify({"error": "Enter the date in the format YYYY-MM-DD"}), 400

    # pagination parameters
    limit = request.args.get("limit", default=10, type=int)
    page = request.args.get("page", default=1, type=int)

    # Calculate the index of the pagination
    offset = (page - 1) * limit

    # Filtrar las trayectorias por taxi_id con paginación
    trajectories_filter = Trajectories.query.filter(func.date(Trajectories.date) == date,
                                                    Trajectories.taxi_id == taxi_id
                                                    ).limit(limit).offset(offset).all()

    # Verify if there are trajectories

    if not trajectories_filter:
        return jsonify({"error": "The ID or the date does not exist in the database"}), 404

    # Convert the Trajectories objects to dictionaries
    trajectories_dict = []
    for trajectory in trajectories_filter:
        trajectory_dict = {
            "taxi_id": trajectory.taxi_id,
            "id": trajectory.id,
            "date": trajectory.date.strftime('%Y-%m-%d'),
            "time": trajectory.date.strftime('%H:%M:%S'),
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
