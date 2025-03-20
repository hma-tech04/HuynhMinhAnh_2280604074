from cryptography.hazmat.primitives.asymmetric import dh
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes


def generate_client_dh_key_pair(parameters):
    client_private_key = parameters.generate_private_key()
    client_public_key = client_private_key.public_key()
    return client_private_key, client_public_key


def derive_shared_secret(private_key, public_key):
    shared_key = private_key.exchange(public_key)
    return shared_key


def main():
    with open("server_public_key.pem", "rb") as f:
        server_public_key = serialization.load_pem_public_key(
            f.read()
        )
    parameters = server_public_key.parameters()
    private_key, public_key = generate_client_dh_key_pair(parameters)

    shared_secret = derive_shared_secret(private_key, server_public_key)

    print(f"Shared secret: {shared_secret.hex()}")


if __name__ == "__main__":
    main()
