FROM python:3.12.11-alpine

ENV PYTHONUNBUFFERED 1

RUN mkdir /backend

WORKDIR /backend

COPY requirements.txt .

RUN apk add --no-cache gcc musl-dev && \
    pip install -r requirements.txt && \
    apk del gcc musl-dev

COPY . .

EXPOSE 8000

CMD ["uvicorn", "backend.main:app", "--host", "0.0.0.0", "--port", "8000"]