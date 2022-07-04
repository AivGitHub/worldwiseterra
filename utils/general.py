import secrets


class General:
    @staticmethod
    def generate_secret_key(key_length=50, allowed_chars=None):
        if not allowed_chars:
            allowed_chars = [chr(i) for i in range(0x21, 0x7F)]

        if not key_length:
            key_length = 50

        return ''.join(secrets.choice(allowed_chars) for i in range(key_length))
