"""test e2e"""
import requests


def test_show_taxis_e2e():
    """test e2e"""
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


def test_show_trajectories():
    """test e2e show trajectories"""
    response = requests.get(
        'http://localhost:5000/trajectories?taxi_id=7957&date=2008-02-02', timeout=5)
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

# def test_show_trajectories(client):
#     response = requests.get('/trajectories?taxi_id=7957&date=2008-02-02')
#     assert response.status_code == 200
#     trajectories_data = response.json()
#     assert trajectories_data
#     assert isinstance(trajectories_data, (trajectories_data, list))
#     assert len(trajectories_data) > 0
#     assert isinstance(trajectories_data[0], dict)


#     # chek the first element has the key 'taxi_id', 'date', 'latitude' y 'longitude'
#     assert 'date' in trajectories_data[0]
#     assert 'id' in trajectories_data[0]
#     assert 'latitude' in trajectories_data[0]
#     assert 'longitude' in trajectories_data[0]
#     assert 'taxi_id' in trajectories_data[0]
#     assert 'time' in trajectories_data[0]
#     # check that values match of 'date', 'latitude' y 'longitude' match with expected values
#     for item in trajectories_data:
#         assert item['date'] == "2008-02-02"
#         assert item['id'] == 1
#         assert item['latitude'] == 116.28709
#         assert item['longitude'] == 39.95843
#         assert item['taxi_id'] == 7957
#         assert item['time'] == "13:47:48"
# Ejecutar el test E2E
if __name__ == "__main__":
    test_show_taxis_e2e()
