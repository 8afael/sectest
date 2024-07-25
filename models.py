from database import Base
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey

class Vulnerabilities(Base):
    __tablename__= 'vulnerabilities'

    id = Column(Integer, autoincrement=True, primary_key=True, index=True)
    idTopTen = Column(String)
    description = Column(String)
    cwe_id = Column(Integer, ForeignKey("cwe.recordId"))
    owasp_id = Column(Integer, ForeignKey("alertOwasp.id"))
    arachni_id = Column(Integer, ForeignKey("arachni.id"))
    wapiti_id = Column(Integer, ForeignKey("alertsWapiti.id"))

class alertsWapiti(Base):
    __tablename__= 'alertsWapiti'

    id = Column(Integer, autoincrement=True, primary_key=True, index=True)
    classifications = Column(String)
    description = Column(String)
    solution = Column(String)
    cwe_id = Column(String)
    vulnerabilities_id = Column(Integer, ForeignKey("vulnerabilities.id"))
    
class referencesWapiti(Base):
    __tablename__= 'referenceswapiti'

    id = Column(Integer, autoincrement=True, primary_key=True, index=True)
    references = Column(String)
    alertsWapiti_id = Column(Integer, ForeignKey("alertsWapiti.id"))

class Arachni(Base):
    __tablename__= 'arachni'

    id = Column(Integer, autoincrement=True, primary_key=True, index=True)
    cwe_id = Column(String)
    description = Column(String)
    vulnerabilities_id = Column(Integer, ForeignKey("vulnerabilities.id"))
    cwe_id = Column(Integer, ForeignKey("vulnerabilities.id"))

class Cwe(Base):
    __tablename__= 'cwe'

    recordId = Column(Integer, autoincrement=True, primary_key=True, index=True)
    description = Column(String)
    vulnerabilities_id = Column(Integer, ForeignKey("vulnerabilities.id"))

class AlertOwasp(Base):
    __tablename__= 'alertOwasp'

    id = Column(Integer, autoincrement=True, primary_key=True, index=True)
    alert = Column(String)
    description = Column(String)
    solution = Column(String)
    otherinfo = Column(String)
    cwe_id = Column(Integer)
    vulnerabilities_id = Column(Integer, ForeignKey("vulnerabilities.id"))


    