from sqlalchemy import *
from sqlalchemy import create_engine,ForeignKey,unique()
from sqlalchemy import Column,Date,Integer,String
from sqlalchemy.orm import relationship,backref,declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import joinedload
from sqlalchemy.orm import aliased

Base=declarative_base()
class AdminUserType(Base):
    __tablename__="tblAdminUserType"
    id=Column(Integer,primary_key=True)
    usertype=Column(String,unique=True)
    adminusers=relationship("AdminUser",back_populates="AdminUser")
    
    def __init__(self,usertype):
        self.usertype=usertype
        
class AdminUser(Base):
    __tablename__="tblAdminUser"
    id=Column(Integer,primary_key=True)
    username=Column(String)
    emailid=Column(String)
    doc=Column(Date)
    pwd=Column(String)
    status=Column(String) #active,suspended,retired
    usertype=relationship("AdminUser",back_populates="AdminUserType")
    def __init__(self,username,emailid,pwd,usertype):
        self.username=username
        self.emailid=emailid
        self.pwd=pwd
        self.usertype=usertype
    