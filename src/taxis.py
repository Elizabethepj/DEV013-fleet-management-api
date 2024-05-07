"""Endpoint taxis"""
from flask import Blueprint, jsonify, request
from .models import Taxi


# Define Blueprint taxis modul
taxis_routes = Blueprint('taxis', __name__)


# Route taxis


@taxis_routes.route('/taxis', methods=['GET'])
def show_taxis():
    """
    Endpoint para obtener todos los taxis.

    ---
    parameters:
      - name: query
        in: query
        type: string
        required: false
        description: Placa del taxi.

      - name: page
        in: query
        type: integer
        required: false
        description: Número de página de los resultados a recuperar. El valor predeterminado es 1.

      - name: limit
        in: query
        type: integer
        required: false
        description: Número de elementos por página. El valor predeterminado es 10.

    responses:
      200 :
        description: Un arreglo JSON de todos los taxis.
        schema:
          type: array
          items:
            type: object
            properties:
              id:
                type: integer
                description: El ID del taxi.
              plate:
                type: string
                description: Placa del taxi.
    """

    # pagination parameters
    limit = request.args.get("limit", default=10, type=int)
    page = request.args.get("page", default=1, type=int)

    # Calcula el índice de inicio basado en la página y el límite
    start_index = (page - 1) * limit

    # Query database with limit and starting index
    taxis = Taxi.query.offset(start_index).limit(limit).all()

    # Create result list
    taxis_list = [{'id': taxi.id, 'plate': taxi.plate} for taxi in taxis]

    return jsonify(taxis_list)
