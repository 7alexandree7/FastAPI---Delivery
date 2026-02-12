from fastapi import Depends
from models.models import User
from sqlalchemy.orm import Session
from db.session import get_session
from jose import jwt, JWTError
from main import SECRET_KEY, ALGORITHM, oauth2_scheme
from fastapi import HTTPException


def verify_token(token: str = Depends(oauth2_scheme), session: Session = Depends(get_session)):
    try:
        dic_info = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        id_user = int(dic_info.get("sub"))
        user = session.query(User).filter(User.id == id_user).first()

        if not user:
            raise HTTPException(status_code=404, detail="user not found")
        
        return user

    except JWTError:
        raise HTTPException(status_code=401, detail="invalid token")
