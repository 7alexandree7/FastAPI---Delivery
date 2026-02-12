from fastapi import HTTPException
from models.models import User
from main import bcrypt_context, ACCESS_TOKEN_EXPIRES_MINUTES, SECRET_KEY, ALGORITHM
from jose import jwt
from datetime import datetime, timedelta, timezone


def create_token(id_user):
    expiration_date = datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_EXPIRES_MINUTES)
    dic_info = { "sub": id_user, "exp": expiration_date }
    encoded_jwt = jwt.encode(dic_info, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt



def authenticate_user(email, password, session):
    user = session.query(User).filter(User.email == email).first()

    if not user:
        raise HTTPException(status_code=404, detail="user not found")
    
    elif not bcrypt_context.verify(password, user.password):
        raise HTTPException(status_code=401, detail="invalid password")

    return user