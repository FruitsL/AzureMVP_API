from fastapi import FastAPI
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from datetime import datetime

import logging
import os
from opencensus.ext.azure.log_exporter import AzureLogHandler

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Application Insights 연결 문자열 환경변수 사용
connection_string = os.getenv("APPLICATIONINSIGHTS_CONNECTION_STRING", "")
if connection_string:
    logger.addHandler(AzureLogHandler(connection_string=connection_string))

app = FastAPI()

@app.post("/now")
def get_current_time():
    logger.info("/now endpoint called")
    return {"current_time": datetime.now().isoformat()}

class AddParams(BaseModel):
    param1: int
    param2: int

@app.post("/add")
def add(params: AddParams):
    logger.info(f"/add endpoint called with param1={params.param1}, param2={params.param2}")
    return {"result": params.param1 + params.param2}
