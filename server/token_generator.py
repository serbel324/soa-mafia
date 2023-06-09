import random

def generate_token(length: int, chars: str) -> str:
    token = ""
    for _ in range(length):
        token += random.choice(chars)
    return token