import httpx

response = httpx.get("https://jsonplaceholder.typicode.com/todos/1")

# print(response.status_code)
# print(response.json())


data = {
    "title": "New lesson",
    "completed": False,
    "userId": 1
}

response = httpx.post("https://jsonplaceholder.typicode.com/todos", json=data)

# print(response.status_code)
# print(response.json())

data = {"username": "test_name", "password": "12345"}
response = httpx.post("https://httpbin.org/post", data=data)

# print(response.json())
# print(response.status_code)

headers = {"Authorization": "Token <PASSWORD>"}
response = httpx.get("https://httpbin.org/get", headers=headers)

# print(response.json())
# print(response.request.headers)

params = {"userId": 1}
response = httpx.get("https://jsonplaceholder.typicode.com/todos", params=params)

# print(response.json())
# print(response.url)

files = {"file": ("example.txt", open("example.txt", "rb"))}
response = httpx.post("https://httpbin.org/post", files=files)

# print(response.json())

with httpx.Client() as client:
    response1 = client.get("https://jsonplaceholder.typicode.com/todos/1")
    response2 = client.get("https://jsonplaceholder.typicode.com/todos/2")

# print(response1.json())
# print(response2.json())

client = httpx.Client(headers={"Authorization": "Token <PASSWORD>"})
response = client.get("https://httpbin.org/get")

# print(response.json())

# try:
#     response = httpx.get("https://jsonplaceholder.typicode.com/invalid-url")
#     response.raise_for_status()
# except httpx.HTTPStatusError as e:
#     print(f"Ошибка запроса {e}")

try:
    response = httpx.get("https://httpbin.org/delay/5", timeout=2)
except httpx.ReadTimeout as e:
    print("Запрос превысил лимит времени")