from fastapi import FastAPI
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from datetime import datetime
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

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
