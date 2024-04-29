import requests


def test_show_taxis_e2e():
    # Simular una solicitud GET a la ruta '/taxis' con parámetros de paginación
    response = requests.get('http://localhost:5000/taxis',
                            params={'limit': 10, 'page': 1})

    assert response.status_code == 200

    # Verificar la estructura de la respuesta JSON
    taxis_data = response.json()
    assert isinstance(taxis_data, list)
    for taxi in taxis_data:
        assert isinstance(taxi, dict)
        assert 'id' in taxi
        assert 'plate' in taxi

# Ejecutar el test E2E
if __name__ == "__main__":
    test_show_taxis_e2e()
