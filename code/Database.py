import psycopg
import hashlib
import dotenv
import os


dotenv.load_dotenv()

DATABASE_NAME: str | None = os.getenv("database")
USER: str | None = os.getenv("user")
PASSWORD: str | None = os.getenv("password")
HOST: str | None = os.getenv("host")
PORT: str | None = os.getenv("port")


def to_hash(content: str) -> str:
    SHA256 = hashlib.sha256()
    SHA256.update(content.encode())

    hash = SHA256.hexdigest()

    return hash

class DATABASE: 
    def __init__(self) -> None:
        self.CONN = psycopg.connect(
            dbname=DATABASE_NAME,
            user=USER,
            password=PASSWORD,
            host=HOST,
            port=PORT
        )

        self.CURSOR = self.CONN.cursor()

        self.CURSOR.execute("CREATE TABLE IF NOT EXISTS hashes (id SERIAL PRIMARY KEY, hash text)")
        print("TABLE CREATED SUCCESSFULLY")
    
    def add_to_db(self, hash: str) -> None:
        # TODO
        pass

    def check_db(self, hash: str) -> None:
        # TODO
        pass


if __name__ == "__main__":
    print(to_hash("South Sudan says Mexico provides assurances its national would not face torture or other inhumane treatment."))
    db = DATABASE()
