import hashlib                                  # SHA, MD5 등의 해시 알고리즘 제공하는 Python 내장 라이브러리(암호화 또는 무결성 검증)
from typing     import Dict, List               # 타입 힌트를 위한 Dict, List 모듈

# 유저별 접근 가능한 기능
USER_PERMISSIONS: Dict[str, List[str]] = {
    "user1": ["feature1", "feature2", "feature3"],
    "user2": ["feature1", "feature3"],
    "user3": ["feature2"],
    "user4": [] #접근 불가
}

# 하드코딩된 사용자 정보 (SHA-256으로 해싱된 비밀번호 저장)
USERS = {
    "user1": hashlib.sha256("password1".encode()).hexdigest(),
    "user2": hashlib.sha256("password2".encode()).hexdigest(),
    "user3": hashlib.sha256("password3".encode()).hexdigest(),
    "user4": hashlib.sha256("password4".encode()).hexdigest()
}

