import pytest
import json


@pytest.mark.parametrize("expected_status", [200])
def test_show_taxis(client, expected_status):
    """test for function taxis"""
    # Make the GET request to the '/taxis' endpoint
    response = client.get('/taxis')
    assert response.status_code == expected_status


@pytest.mark.parametrize('page', [1, 7, 50])
def test_pagination(client, page):
    """test for pagination of the show_taxis function."""
    limit = 10
    response = client.get(f'/taxis?limit={limit}&page={page}')
    taxis_data = json.loads(response.data)

    remaining_data_count = len(taxis_data)
    if remaining_data_count < limit:
        assert len(taxis_data) == remaining_data_count
    else:
        assert len(taxis_data) == limit


@pytest.mark.parametrize('expected_plates', [
    [
        {
            "id": 7249,
            "plate": "CNCJ-2997"
        },
        {
            "id": 10133,
            "plate": "PAOF-6727"
        }
    ]
])
def test_return_data(client, expected_plates):
    """check data returned match expected data."""
    response = client.get('/taxis')
    # convert a json data to a python object
    data = json.loads(response.data)
    returned_plates = [taxi['plate'] for taxi in data]
    for expected_plate in expected_plates:
        assert expected_plate['plate'] in returned_plates
