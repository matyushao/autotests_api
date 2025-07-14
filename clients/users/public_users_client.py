from clients.api_client import APIClient
from httpx import Response
from typing import TypedDict

class CreateUserRequest(TypedDict):
    """
    Описание структуры запроса на создание пользователя
    """
    email: str
    password: str
    lastName: str
    firstName: str
    middleName: str

class PublicUsersClient(APIClient):
    """
    Клиент для публичного взаимодействия с пользователем
    """

    def create_user_api(self, request: CreateUserRequest) -> Response:
        """
        Метод создает нового пользователя
        :param request: Данные пользователя: email, password, lastName, firstName, middleName
        :return: Объект Response с данными ответа
        """
        return self.post("/api/v1/users", json=request)
