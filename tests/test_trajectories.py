"""test routes of trajectoriesd"""
def test_response(client):
    """check the response"""
    response = client.get('/trajectories?taxi_id=6418&date=2008-02-02')
    expected_status = 200
    data = response.json
    assert response.status_code == expected_status
    assert isinstance(data, list)


def test_missing_taxi_id(client):
    """check the response when there is missind id_taxi"""
    response = client.get('/trajectories?date=2008-02-02')
    error_data = response.json
    assert response.status_code == 400
    assert 'error' in error_data
    assert error_data['error'] == "Debe proporcionar el ID de taxi"


def test_invalidate_date(client):
    """check the response when date has a invalid format"""
    response = client.get('/trajectories?taxi_id=6418&date=20008-02-02')
    error_data = response.json
    assert response.status_code == 400
    assert 'error' in error_data
    assert error_data['error'] == "Enter the date in the format YYYY-MM-DD"


def test_nononexistent_database(client):
    """check the response when trajectories no exist"""
    response = client.get('/trajectories?taxi_id=0000&date=2008-02-02')
    error_data = response.json
    assert response.status_code == 404  # information doesn't exist
    assert 'error' in error_data
    assert error_data['error'] == "The ID or the date does not exist in the database"
