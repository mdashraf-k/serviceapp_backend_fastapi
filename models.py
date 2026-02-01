from databases import Base
from sqlalchemy import Column, Integer, ForeignKey,String, Boolean

class Services(Base):
    __tablename__ = "services"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    phone_number = Column(String)
    address = Column(String)
    product = Column(String)

