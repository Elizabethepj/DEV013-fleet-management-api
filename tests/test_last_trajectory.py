"""test routes of last_trajectory"""
import json
import pytest


def test_response(client):
    """check the response"""
    response = client.get('/last_trajectory')
    expected_status = 200
    assert response.status_code == expected_status


def test_kind_of_data(client):
    """check kind of data"""
    response = client.get('/last_trajectory')
    data = response.json
    assert isinstance(data, list)


@pytest.mark.parametrize('expected_data',
                         [
                             {
                                 "date": "Thu, 07 Feb 2008 22:11:26 GMT",
                                 "latitude": 116.30509,
                                 "longitude": 39.96563,
                                 "plate": "GHGH-1458",
                                 "taxi_id": 6418
                             },
                             {
                                 "date": "Fri, 08 Feb 2008 17:37:43 GMT",
                                 "latitude": 116.32706,
                                 "longitude": 39.84801,
                                 "plate": "FHLB-7962",
                                 "taxi_id": 6598
                             }
                         ])
def test_expected_data(client, expected_data):
    """verify length data and data"""
    response = client.get('/last_trajectory')
    data = json.loads(response.data)
    assert expected_data in data
    expected_length_data = len(expected_data)
    assert len(expected_data) == expected_length_data


def test_len_data(client):
    """verify real length data"""
    response = client.get('/last_trajectory')
    data = json.loads(response.data)
    length_data = 10
    assert len(data) == length_data
