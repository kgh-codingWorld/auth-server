import hashlib # SHA, MD5 등의 해시 알고리즘 제공하는 Python 내장 라이브러리(암호화 또는 무결성 검증)

# 비밀번호 암호화
def hash_password(password: str) -> str:
    return hashlib.sha256(password.encode()).hexdigest()