from . import file_service_pb2
from . import file_service_pb2_grpc
import grpc


def get_file(peer_ip, peer_port, filepath):
    channel = grpc.insecure_channel(f"{peer_ip}:{peer_port}")
    stub = file_service_pb2_grpc.FileServiceStub(channel)
    response = stub.GetFile(
        file_service_pb2.GetFileRequest(
            address=file_service_pb2.AddressPeer(IP=peer_ip, port=peer_port),
            file_path=filepath,
        )
    )
    return response


def set_file(peer_ip, peer_port, filepath, content):
    channel = grpc.insecure_channel(f"{peer_ip}:{peer_port}")
    stub = file_service_pb2_grpc.FileServiceStub(channel)
    response = stub.SetFile(
        file_service_pb2.SetFileRequest(
            address=file_service_pb2.AddressPeer(IP=peer_ip, port=peer_port),
            file_path=filepath,
            file_content=content,
        )
    )
    return response


def delete_file(peer_ip, peer_port, filepath):
    channel = grpc.insecure_channel(f"{peer_ip}:{peer_port}")
    stub = file_service_pb2_grpc.FileServiceStub(channel)
    response = stub.DeleteFile(
        file_service_pb2.DeleteRequest(
            address=file_service_pb2.AddressPeer(IP=peer_ip, port=peer_port),
            file_path=filepath,
        )
    )
    return response
