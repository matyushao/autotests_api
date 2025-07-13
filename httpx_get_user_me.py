import httpx

user_login_payload = {
    "email": "user@example.com",
    "password": "rrr"
}

user_login_response = httpx.post("http://127.0.0.1:8000/api/v1/authentication/login", json=user_login_payload)
user_login_response_data = user_login_response.json()

print("Login response:", user_login_response_data)
print("Status code:", user_login_response.status_code)

headers = {
    f"Authorization": f"Bearer {user_login_response_data["token"]["accessToken"]}"
}

user_me_token_response = httpx.get("http://127.0.0.1:8000/api/v1/users/me", headers=headers)
user_me_token_response_json = user_me_token_response.json()

print("User me token response:", user_me_token_response_json)


