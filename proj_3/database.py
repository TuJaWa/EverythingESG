from sqlalchemy import create_engine, Column, Integer, Float, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import datetime

Base = declarative_base()

class EconomyLog(Base):
    __tablename__ = 'economy_log'
    id = Column(Integer, primary_key=True)
    timestamp = Column(DateTime, default=datetime.datetime.utcnow)
    gdp_growth_rate = Column(Float)
    population_growth_rate = Column(Float)

def get_engine():
    return create_engine('sqlite:///simulation.db', echo=True)

def create_tables(engine):
    Base.metadata.create_all(engine)

def log_economy_data(engine, gdp_growth_rate, population_growth_rate):
    Session = sessionmaker(bind=engine)
    session = Session()
    log_entry = EconomyLog(gdp_growth_rate=gdp_growth_rate, population_growth_rate=population_growth_rate)
    session.add(log_entry)
    session.commit()

# Setup database and tables
engine = get_engine()
create_tables(engine)