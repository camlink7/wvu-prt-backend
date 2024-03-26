from sqlalchemy import Column, String, Integer
from Database import Base

class StatusReport(Base):
    __tablename__ = "StatusReports"

    timestamp = Column("timestamp", Integer, primary_key=True)
    status = Column("status", Integer, nullable=False)
    message = Column("message", String(2000), nullable=True)
    buses_dispatched = Column("buses_dispatched", Integer, nullable=False)

    def __init__(self, timestamp, status, message, buses_dispatched):
        self.timestamp = timestamp
        self.status = status
        self.message = message
        self.buses_dispatched = buses_dispatched


    # Getters
    def get_timestamp(self):
        return self.timestamp
    def get_status(self):
        return self.status
    def get_message(self):
        return self.message
    def get_buses_dispatched(self):
        return self.buses_dispatched