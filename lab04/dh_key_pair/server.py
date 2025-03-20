from cryptography.hazmat.primitives.asymmetric import dh
from cryptography.hazmat.primitives import serialization


def generate_dh_parameters():
    parameters = dh.generate_parameters(generator=2, key_size=2048)
    return parameters


def generate_server_dh_key_pair(parameters):
    server_private_key = parameters.generate_private_key()
    server_public_key = server_private_key.public_key()
    return server_private_key, server_public_key


def main():
    parameters = generate_dh_parameters()
    server_private_key, server_public_key = generate_server_dh_key_pair(parameters)

    with open("server_private_key.pem", "wb") as f:
        f.write(server_private_key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.PKCS8,
            encryption_algorithm=serialization.NoEncryption()
        ))

    with open("server_public_key.pem", "wb") as f:
        f.write(server_public_key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        ))



if __name__ == "__main__":
    main()
