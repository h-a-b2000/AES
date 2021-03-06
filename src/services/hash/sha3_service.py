from services.base_service import BaseService
from Crypto.Hash import SHA3_256


class SHA3Service(BaseService):
    def __init__(self, text):
        self.text = text
        super().__init__()

    @staticmethod
    def encode(plain_text):
        hash_object = SHA3_256.new()
        hash_object.update(plain_text.encode())
        return hash_object.hexdigest()

    def validate(self):
        pass

    def process(self):
        return self.encode(self.text)


if __name__ == "__main__":
    sha3 = SHA3Service(text="aaa").execute()
    print(sha3)
