# FROM python:3.7-slim
FROM rappdw/docker-java-python


WORKDIR /demo

COPY . /demo

EXPOSE 8002

RUN pip install -r requirements.txt


CMD ["uvicorn","src.main:app","--reload","--port=8002","--host=0.0.0.0" ]



