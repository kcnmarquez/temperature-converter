def test_landing(client):
    landing = client.get("/")
    html = landing.data.decode()

    assert "<h1>Temperature Converter</h1>" in html

    assert landing.status_code == 200

def test_convert_to_fahrenheit(client):
    response = client.post("/convert/", json={
        "value": 0,
        "desired_unit": "F"
    })
    assert response.json["result"] == 32

def test_convert_to_celsius(client):
    response = client.post("/convert/", json={
        "value": 253.4,
        "desired_unit": "C"
    })
    assert response.json["result"] == 123