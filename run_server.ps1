# PowerShell 스크립트: run_server.ps1
# venv 활성화 후 FastAPI 서버 실행

. .\.venv\Scripts\Activate.ps1
uvicorn app.main:app --host 0.0.0.0 --port 8000
