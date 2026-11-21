def verify_token(token: str) -> bool:
    return bool(token and token.startswith('Bearer '))
