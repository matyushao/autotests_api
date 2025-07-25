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

# Выполняем загрузку файла
create_file_headers = {
    "Authorization": f"Bearer {login_user_response_data['token']['accessToken']}",
}
create_file_response = httpx.post(
    "http://127.0.0.1:8000/api/v1/files",
    data={"filename": "image.png", "directory": "courses"},
    files={"upload_file": open("./testdata/files/image.png", "rb")},
    headers=create_file_headers
)
create_file_response_data = create_file_response.json()
print("Create file data:", create_file_response_data)
