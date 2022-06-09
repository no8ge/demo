FROM python:3.7-slim

WORKDIR /demo

COPY . /demo

EXPOSE 8002

RUN pip install fastapi uvicorn[standard]


CMD ["uvicorn","src.main:app","--reload","--port=8002","--host=0.0.0.0" ]



