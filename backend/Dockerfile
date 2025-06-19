FROM python:3.13-alpine

ARG DATABASE_URL
ENV DATABASE_URL=$DATABASE_URL

ARG FRONTEND_URL
ENV FRONTEND_URL=$FRONTEND_URL


WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]