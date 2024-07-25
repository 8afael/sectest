import json
import sqlite3
import models
from fastapi import FastAPI
from database import engine
from saveAlertOwasp import AlertDetail, JSONDataSearcher
from saveAlertWapiti import wapitiSearcher

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

def runOwasp():
    owasp = JSONDataSearcher("json/report_owaspZap_2024-02-14_14:43.json", "vulnerabilities.db")
    owasp.saveOwaspToClass()
    owasp.saveOwaspToDB()

def runWapiti():
    wapiti = wapitiSearcher("json/report_wapiti_2024-02-14_14:43.json", "vulnerabilities.db")
    wapiti.saveWapitiAlertToClass()
    wapiti.saveWapitiReferenceToClass()
    wapiti.saveWapitiToDB()

#runOwasp()
runWapiti()
    