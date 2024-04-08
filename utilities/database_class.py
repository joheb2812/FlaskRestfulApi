from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    userId = Column(Integer, primary_key=True)
    firstName = Column(String(50))
    lastName = Column(String(100))
    transactions = relationship('Transaction', back_populates='user')

class Transaction(Base):
    __tablename__ = 'transactions'
    transactionId = Column(Integer, primary_key=True)
    userId = Column(Integer, ForeignKey('users.userId'))
    transactionDate = Column(DateTime)
    amount = Column(Float)
    debitOrCredit = Column(String(255))
    user = relationship('User', back_populates='transactions')
