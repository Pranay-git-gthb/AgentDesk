from sqlalchemy import Column, Integer, String, TIMESTAMP, text

from app.database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer , primary_key=True, index=True)
    username = Column(String(100) , nullable=False)
    email = Column(String(255), unique=True , nullable = False)
    created_at = Column(TIMESTAMP , server_default=text('CURRENT_TIMESTAMP'))