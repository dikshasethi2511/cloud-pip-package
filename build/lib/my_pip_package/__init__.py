import your_proto_file_pb2
import your_proto_file_pb2_grpc
import grpc


def get_file(peer_ip, peer_port, filepath):
    channel = grpc.insecure_channel(f"{peer_ip}:{peer_port}")
    stub = your_proto_file_pb2_grpc.FileServiceStub(channel)
    response = stub.GetFile(
        your_proto_file_pb2.GetFileRequest(
            address=your_proto_file_pb2.Address(IP=peer_ip, port=peer_port),
            file_path=filepath,
        )
    )
    return response


def set_file(peer_ip, peer_port, filepath, content):
    channel = grpc.insecure_channel(f"{peer_ip}:{peer_port}")
    stub = your_proto_file_pb2_grpc.FileServiceStub(channel)
    response = stub.SetFile(
        your_proto_file_pb2.SetFileRequest(
            address=your_proto_file_pb2.Address(IP=peer_ip, port=peer_port),
            file_path=filepath,
            file_content=content,
        )
    )
    return response


def delete_file(peer_ip, peer_port, filepath):
    channel = grpc.insecure_channel(f"{peer_ip}:{peer_port}")
    stub = your_proto_file_pb2_grpc.FileServiceStub(channel)
    response = stub.DeleteFile(
        your_proto_file_pb2.DeleteRequest(
            address=your_proto_file_pb2.Address(IP=peer_ip, port=peer_port),
            file_path=filepath,
        )
    )
    return response
