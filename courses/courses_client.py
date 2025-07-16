from typing import TypedDict
from httpx import Response
from clients.api_client import APIClient

class GetCoursesQueryDict(TypedDict):
    """
    Описание структуры запроса на получение списка курсов
    """
    userID: str

class CreateCoursesRequestDict(TypedDict):
    """
    Описание структуры запроса на создание курса
    """
    title: str
    maxScore: int
    minScore: int
    description: str
    estimatedTime: str
    previewFileId: str
    createdByUserId: str

class UpdateCoursesRequestDict(TypedDict):
    """
    Описание структуры запроса на обновление курса
    """
    title: str | None
    maxScore: int | None
    minScore: int | None
    description: str | None
    estimatedTime: str | None

class CoursesClient(APIClient):
    """
    Клиент для работы с /api/v1/courses
    """

    def get_courses_api(self, query: GetCoursesQueryDict) -> Response:
        """
        Метод для получения списка курсов

        :param query: Словарь с userId
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.get(url="/api/v1/courses/", params=query)

    def get_course_api_by_course_id(self, course_id: str) -> Response:
        """
        Метод получения курса

        :param course_id: Идентификатор курса
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.get(f"url=/api/v1/courses/{course_id}/")

    def create_courses_api(self, request:CreateCoursesRequestDict) -> Response:
        """
        Метод создания курса

        :param request: Словарь с title, maxScore, minScore, description, estimatedTime, previewFileId, createdByUserId
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.post(url="/api/v1/courses/", json=request)

    def update_courses_api(self, course_id: str, request:UpdateCoursesRequestDict) -> Response:
        """
        Метод обновления курса

        :param course_id: Идентификатор курса
        :param request: Словарь с title, maxScore, minScore, description, estimatedTime
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.patch(f"url=/api/v1/courses/{course_id}", json=request)

    def delete_courses_api(self, course_id: str) -> Response:
        """
        Метод удаления курса

        :param course_id: Идентификатор курса
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.delete(f"url=/api/v1/courses/{course_id}/")
