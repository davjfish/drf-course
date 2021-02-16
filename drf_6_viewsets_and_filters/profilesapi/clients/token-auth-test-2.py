import requests


def client():
    # data = {
    #     "username": "resttest",
    #     "email": "test@test.com",
    #     "password1": "why123FFs3",
    #     "password2": "why123FFs3",
    # }
    # response = requests.post("http://localhost:8000/api/rest-auth/registration/", data=data)

    token_h = "Token f34fe8b63b204835449c96ea8b2a3946666d4cfa"
    headers = dict(Authorization=token_h)
    response = requests.get("http://localhost:8000/api/profiles/", headers=headers)
    print("status code:", response.status_code)
    print("data:", response.json())
    print("headers:", response.headers)


if __name__ == '__main__':
    client()
