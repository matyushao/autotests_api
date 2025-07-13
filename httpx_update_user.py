import httpx
from tools.fakers import get_randon_email

# Создание пользователя
create_user_payload = {
    "email": get_randon_email(),
    "password": "string",
    "lastName": "string",
    "firstName": "string",
    "middleName": "string"
}

create_user_response = httpx.post("http://127.0.0.1:8000/api/v1/users", json=create_user_payload)
create_user_response_data = create_user_response.json()
print("Create user data:", create_user_response_data)

# Прохождение аутентификации
login_user_payload = {
    "email": create_user_payload["email"],
    "password": create_user_payload["password"]
}

login_user_response = httpx.post("http://127.0.0.1:8000/api/v1/authentication/login", json=login_user_payload)
login_user_response_data = login_user_response.json()
print("Login user data:", login_user_response_data)

# Обновление пользователя
update_user_headers = {
    "Authorization": f"Bearer {login_user_response_data['token']['accessToken']}"
}

update_user_payload = {
    "email": get_randon_email(),
    "lastName": "string",
    "firstName": "string",
    "middleName": "string"
}

update_user_response = httpx.patch(
    f"http://127.0.0.1:8000/api/v1/users/{create_user_response_data['user']['id']}",
    headers=update_user_headers, json=update_user_payload
)
update_user_data = update_user_response.json()

print("Update user data:", update_user_data)
print("Update user status code:", update_user_response.status_code)