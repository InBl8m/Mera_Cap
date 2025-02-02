FROM python:3.10-slim

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY requirements/ requirements/

RUN pip install --upgrade pip \
        && pip install -r requirements.txt \

COPY . .

CMD ["python", "./main.py"]
