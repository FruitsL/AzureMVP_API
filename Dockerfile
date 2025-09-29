# 1) 빌드
FROM python:3.11-slim AS base
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 2) 런타임
COPY app ./app
ARG APPINSIGHTS_INSTRUMENTATIONKEY
ENV APPINSIGHTS_INSTRUMENTATIONKEY=$APPINSIGHTS_INSTRUMENTATIONKEY
ENV APP_VERSION=1.0.0
ENV APP_BUILD=docker
EXPOSE 8000
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
