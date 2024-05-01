from flask import Blueprint, request
from .models import Trajectories

trajectories = Blueprint('trajectories', __name__)

# Route trajectories


@trajectories.route('/trajectories', methods=['GET'])
def show_trajectories():
    """show trajectories"""
    taxi_id = request.args.get('taxi_id')
    date = request.args.get('date')

    trajectories = Trajectories.query_trajectories(taxi_id, date)
