
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from datetime import datetime

import logging
import os
from dotenv import load_dotenv
from opencensus.ext.azure.log_exporter import AzureLogHandler
from opencensus.ext.azure.trace_exporter import AzureExporter
from opencensus.ext.fastapi.fastapi_middleware import FastAPIMiddleware
from opencensus.trace.samplers import ProbabilitySampler

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# .env 파일에서 환경변수 로드
load_dotenv()

# Application Insights 연결 문자열 환경변수 사용
connection_string = os.getenv("APPLICATIONINSIGHTS_CONNECTION_STRING", "")
app = FastAPI()
if connection_string:
    app.add_middleware(
        FastAPIMiddleware,
        exporter=AzureExporter(connection_string=connection_string),
        sampler=ProbabilitySampler(1.0)
    )
    print("[Application Insights] FastAPIMiddleware 등록됨 (trace only)")
else:
    print("[Application Insights] 연결 문자열이 없습니다. 로그가 수집되지 않습니다.")

@app.post("/now")
def get_current_time():
    logger.info("/now endpoint called")
    return {"time": datetime.now().isoformat()}

class AddParams(BaseModel):
    param1: int
    param2: int

@app.post("/add")
def add(params: AddParams):
    logger.info(f"/add endpoint called with param1={params.param1}, param2={params.param2}")
    return {"result": params.param1 + params.param2}
