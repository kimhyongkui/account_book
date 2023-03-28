from sqlalchemy import VARCHAR, Column, Integer
from db.connection import Base

class route_data(Base):
    __tablename__ = "route_data"

    routeId = Column(Integer, primary_key=True, nullable=False)
    routeNm = Column(VARCHAR(45), nullable=False)
    stnOrd = Column(Integer, primary_key=True, nullable=False)
    stnNm = Column(VARCHAR(45), nullable=False)
    stnId = Column(Integer, nullable=False)
