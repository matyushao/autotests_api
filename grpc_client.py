import grpc

import user_service_pb2
import user_service_pb2_grpc
from grpc import StatusCode


def run():
    # Устанавливаем соединение с сервером
    channel = grpc.insecure_channel('localhost:50051')
    stub = user_service_pb2_grpc.UserServiceStub(channel)

    try:
        # Пытаемся вызвать метод GetUser
        response = stub.GetUser(user_service_pb2.GetUserRequest(username="Alice"))
        print(response.message)  # Выведет: Привет, Alice!

    except grpc.RpcError as e:
        # Обрабатываем исключения от gRPC
        status_code = e.code()
        details =e.details()

        if status_code == StatusCode.UNAVAILABLE:
            print(f"Сервер недоступен: {details}")
        elif status_code == StatusCode.UNIMPLEMENTED:
            print(f"Метод не реализован на сервере: {details}")
        else:
            print(f"RPC завершился с кодом: {status_code} и сообщением {details}")

if __name__ == '__main__':
    run()


