from fastapi import FastAPI
from datetime import datetime

app = FastAPI()

@app.post("/now")
def get_current_time():
    return {"current_time": datetime.now().isoformat()}
