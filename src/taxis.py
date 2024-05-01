from flask import Blueprint, jsonify, request
from .models import Taxi


# Define Blueprint taxis modul
taxis = Blueprint('taxis', __name__)



# Route taxis


@taxis.route('/taxis', methods=['GET'])
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


# from flask import Flask, jsonify, request
# from flask_sqlalchemy import SQLAlchemy
# from flasgger import Swagger

# app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://default:Hs1ODnhjr2lU@ep-holy-sunset-a405zt5y-pooler.us-east-1.aws.neon.tech/verceldb'
# db = SQLAlchemy(app)

# # Initialize Swagger
# swagger = Swagger(app)

# # Define the Taxi model


# class Taxi(db.Model):
#     """Model representing a Taxi."""
#     __tablename__ = 'taxis'
#     id = db.Column(db.Integer, primary_key=True)
#     plate = db.Column(db.String(20), nullable=False)

# # Route to show all taxis


# @app.route('/taxis', methods=['GET'])
# def show_taxis():
#     """
#     Endpoint to get all taxis.

#     ---
#     parameters:
#       - name: query
#         in: query
#         type: string
#         required: false
#         description: Plate of the taxi.

#       - name: page
#         in: query
#         type: integer
#         required: false
#         description: Page number of the results to retrieve. Default is 1.

#       - name: limit
#         in: query
#         type: integer
#         required: false
#         description: Number of elements per page. Default is 10.

#     responses:
#       200 :
#         description: A JSON array of all taxis.
#         schema:
#           type: array
#           items:
#             type: object
#             properties:
#               id:
#                 type: integer
#                 description: The taxi ID.
#               plate:
#                 type: string
#                 description: Plate of the taxi.
#     """

#     # Get pagination parameters from the request
#     limit = request.args.get("limit", default=10, type=int)
#     page = request.args.get("page", default=1, type=int)

#     # Calculate home index based on page and limit
#     start_index = (page - 1) * limit

#     # Query database with limit and starting index
#     taxis = Taxi.query.offset(start_index).limit(limit).all()

#     # Create list
#     taxis_list = [{'id': taxi.id, 'plate': taxi.plate} for taxi in taxis]

#     return jsonify(taxis_list)


# if __name__ == "__main__":
#     app.run(debug=True)
