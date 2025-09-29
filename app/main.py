from fastapi import FastAPI
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from datetime import datetime

# Application Insights 연동
from opencensus.ext.azure.log_exporter import AzureLogHandler
from opencensus.ext.azure.trace_exporter import AzureExporter
from opencensus.ext.fastapi.fastapi_middleware import FastAPIMiddleware
from opencensus.trace.samplers import ProbabilitySampler
import logging
import os
from dotenv import load_dotenv

load_dotenv()

APPINSIGHTS_KEY = os.getenv("APPINSIGHTS_INSTRUMENTATIONKEY", "<YOUR_INSTRUMENTATION_KEY>")

app = FastAPI()
app.add_middleware(FastAPIMiddleware, exporter=AzureExporter(connection_string=f"InstrumentationKey={APPINSIGHTS_KEY}"), sampler=ProbabilitySampler(1.0))

# 로그 핸들러 추가
logger = logging.getLogger(__name__)
logger.addHandler(AzureLogHandler(connection_string=f"InstrumentationKey={APPINSIGHTS_KEY}"))

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
