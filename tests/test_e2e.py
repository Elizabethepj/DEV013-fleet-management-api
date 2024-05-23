"""test e2e"""
import requests


def test_show_taxis_e2e():
    """test e2e taxis"""
    # Simular una solicitud GET a la ruta '/taxis' con parámetros de paginación
    response = requests.get('http://localhost:5000/taxis',
                            params={'limit': 10, 'page': 1},
                            timeout=5)

    assert response.status_code == 200

    # Verificar la estructura de la respuesta JSON
    taxis_data = response.json()
    assert isinstance(taxis_data, list)
    for taxi in taxis_data:
        assert isinstance(taxi, dict)
        assert 'id' in taxi
        assert 'plate' in taxi


def test_show_trajectories_e2e():
    """test e2e show trajectories"""
    response = requests.get(
        'http://localhost:5000/trajectories?taxi_id=7957&date=2008-02-02',
        timeout=5)
    assert response.status_code == 200

    trajectories_data = response.json()
    assert isinstance(trajectories_data, list)
    for trajectory in trajectories_data:
        assert isinstance(trajectory, dict)
        assert 'date' in trajectory
        assert 'id' in trajectory
        assert 'latitude' in trajectory
        assert 'longitude' in trajectory
        assert 'taxi_id' in trajectory
        assert 'time' in trajectory


def test_show_lasttrajectory_e2e():
    """test e2e last trajectory"""
    response = requests.get(
        'http://localhost:5000/last_trajectory',
        timeout=5)
    assert response.status_code == 200

    locations_data = response.json()
    assert isinstance(locations_data, list)
    for location in locations_data:
        assert isinstance(location, dict)
        assert 'taxi_id' in location
        assert 'latitude' in location
        assert 'longitude' in location
        assert 'date' in location
        assert 'plate' in location


# Ejecutar test E2E
if __name__ == "__main__":
    test_show_taxis_e2e()
