from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from database import Base, session

class Worker(Base):
    __tablename__ = "workers"

    id = Column(Integer, primary_key=True)  
    name = Column(String, nullable=False)  
    skill = Column(String, nullable=False)  

    jobs = relationship("Job", back_populates="worker", cascade="all, delete-orphan")

    def __repr__(self):
        return f"<Worker(id={self.id}, name={self.name}, skill={self.skill})>"

    @classmethod
    def create(cls, name, skill):
        worker = cls(name=name, skill=skill)
        session.add(worker)
        session.commit()
        return worker

    @classmethod
    def get_all(cls):
        return session.query(cls).all()

    @classmethod
    def find_by_id(cls, worker_id):
        return session.query(cls).filter_by(id=worker_id).first()

    @classmethod
    def delete(cls, worker_id):
        worker = cls.find_by_id(worker_id)
        if worker:
            session.delete(worker)
            session.commit()
            return True
        return False
