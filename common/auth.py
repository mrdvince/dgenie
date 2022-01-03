import datetime

import jwt

from dgenie import settings


class JWTAuth:
    @staticmethod
    def generate_token(user_id):
        payload = {
            "user_id": user_id,
            "exp": datetime.datetime.utcnow() + datetime.timedelta(days=1),
            "iat": datetime.datetime.utcnow(),
        }
        token = jwt.encode(payload, settings.SECRET_KEY, algorithm="HS256")
        return token
