import hashlib


def blake2(message):
    blake2_hash = hashlib.blake2b(digest_size=64)
    blake2_hash.update(message)
    return blake2_hash.digest()


def main():
    text = input("Nhap chuoi can bam: ").encode('utf-8')
    hashed_text = blake2(text)

    print("Chuoi van ban da nhap: ", text)
    print("Blake2 hash: ", hashed_text.hex())


if __name__ == "__main__":
    main()
