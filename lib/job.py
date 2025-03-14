from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base, session

class Job(Base):
    __tablename__ = "jobs"

    id = Column(Integer, primary_key=True)  
    title = Column(String, nullable=False) 
    worker_id = Column(Integer, ForeignKey("workers.id"), nullable=False)  

    worker = relationship("Worker", back_populates="jobs")  

    def __repr__(self):
        return f"<Job(id={self.id}, title={self.title}, worker_id={self.worker_id})>"

    @classmethod
    def create(cls, title, worker_id):
        job = cls(title=title, worker_id=worker_id)
        session.add(job)
        session.commit()
        return job

    @classmethod
    def get_all(cls):
        return session.query(cls).all()

    @classmethod
    def find_by_id(cls, job_id):
        return session.query(cls).filter_by(id=job_id).first()

    @classmethod
    def delete(cls, job_id):
        job = cls.find_by_id(job_id)
        if job:
            session.delete(job)
            session.commit()
            return True
        return False
