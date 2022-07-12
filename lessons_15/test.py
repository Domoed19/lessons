import json
import requests

from faker import Faker

fake = Faker()

if __name__ == "__main__":
    response = requests.get("http://127.0.0.1:5000/")
    assert response.status_code == 200
    assert response.json() == {"message" : "Index page"}
    assert response.headers.get("content_type") == "application/json"

    response = requests.get("http://127.0.0.1:5000/user/")
    assert response.status_code == 200

    headers = {"Content-Type": "application/json"}
    data = {"email": "", "password": ""}
    response = requests.post("http://127.0.0.1:5000/user/", data=json.dumps(data), headers=headers)
    assert response.status_code == 400

    headers = {"Content-Type": "application/json"}
    data = {"email": fake.email(), "password": fake.word()}
    response = requests.post("http://127.0.0.1:5000/user/", data=json.dumps(data), headers=headers)


    assert response.status_code == 201
    assert response.json.get("email") == data.get("email")
    assert response.json.get("email") is not None

    assert response.headers.get("content_type") == "application/json"
    response = requests.get("http://127.0.0.1:5000/user/")
    assert response.status_code == 200
    print("All tests have passed")