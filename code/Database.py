import hashlib


def to_hash(content: str) -> str:
    SHA256 = hashlib.sha256()
    SHA256.update(content.encode())

    hash = SHA256.hexdigest()

    return hash

class DATABASE: 
    def __init__(self) -> None:
        # TODO
        pass
    
    def add_to_db(self, hash: str) -> None:
        # TODO
        pass

    def check_db(self, hash: str) -> None:
        # TODO
        pass


if __name__ == "__main__":
    print(to_hash("South Sudan says Mexico provides assurances its national would not face torture or other inhumane treatment."))
