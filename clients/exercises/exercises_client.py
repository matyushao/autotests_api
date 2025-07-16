from typing import TypedDict
from httpx import Response
from clients.api_client import APIClient

class GetExercisesQueryDict(TypedDict):
    """
    Описание структуры запроса на получение списка упражнений
    """
    courseId: str

class CreateExercisesRequestDict(TypedDict):
    """
    Описание структуры запроса на создание упражнения
    """
    title: str
    courseId: str
    maxScore: int
    minScore: int
    orderIndex: int
    description: str
    estimatedTime: str

class UpdateExercisesRequestDict(TypedDict):
    """
    Описание структуры запроса на обновление упражнения
    """
    title: str | None
    maxScore: int | None
    minScore: int | None
    orderIndex: int | None
    description: str | None
    estimatedTime: str | None

class ExercisesClient(APIClient):
    """
    Клиент для работы с /api/v1/exercises
    """

    def get_exercises_api(self, query: GetExercisesQueryDict) -> Response:
        """
        Метод для получения списка упражнений

        :param query: Словарь с courseId
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.get(url="/api/v1/exercises", params=query)

    def create_exercises_api(self, request: CreateExercisesRequestDict) -> Response:
        """
        Метод создания упражнения

        :param request: Словарь с title, courseId, maxScore, minScore, orderIndex, description, estimatedTime
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.post(url="/api/v1/exercises", json=request)

    def get_exercises_api_by_exercise_id(self, exercise_id: str) -> Response:
        """
        Метод получения упражнения

        :param exercise_id: Идентификатор упражнения
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.get(f"/api/v1/exercises/{exercise_id}")

    def update_exercises_api(self, exercise_id: str, request: UpdateExercisesRequestDict) -> Response:
        """
        Метод обновления упражнения

        :param exercise_id: Идентификатор упражнения
        :param request: Словарь title, maxScore, minScore, orderIndex, description, estimatedTime
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.patch(f"/api/v1/exercises/{exercise_id}", json=request)

    def delete_exercises_api(self, exercise_id: str) -> Response:
        """
        Метод удаления упражнения

        :param exercise_id: Идентификатор упраженения
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.delete(f"/api/v1/exercises/{exercise_id}")

