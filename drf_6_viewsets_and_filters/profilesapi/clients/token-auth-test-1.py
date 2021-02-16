import requests


def client():
    credentials = {
        "username": "admin",
        "password": "admin",
    }

    # response = requests.post("http://localhost:8000/api/rest-auth/login/", data=credentials)
    token_h = "Token 4d0d7e976a5dc99cb4e673ccd90791b940e31760"
    headers = dict(Authorization=token_h)
    response = requests.get("http://localhost:8000/api/profiles/", headers=headers)

    print("status code:", response.status_code)
    print("data:", response.json())


if __name__ == '__main__':
    client()
