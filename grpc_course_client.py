import grpc

import course_service_pb2
import course_service_pb2_grpc
from grpc import StatusCode

def run_course():
    channel = grpc.insecure_channel('localhost:50051')
    stub = course_service_pb2_grpc.CourseServiceStub(channel)

    try:
        response = stub.GetCourse(course_service_pb2.GetCourseRequest(course_id="api-course"))
        print(response)

    except grpc.RpcError as e:
        status_code = e.code()
        details = e.details()

        if status_code == grpc.StatusCode.UNAVAILABLE:
            print(f"Сервер недоступен: {details}")
        elif status_code == grpc.StatusCode.UNIMPLEMENTED:
            print(f"Метод не реализован на сервере: {details}")
        else:
            print(f"RPC завершился с кодом: {status_code} и сообщением {details}")

if __name__ == '__main__':
    run_course()