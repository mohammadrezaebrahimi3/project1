FROM python:3.13

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1


WORKDIR /app

COPY  requirements.txt .

RUN pip install  -r requirements.txt

COPY . .

CMD [ "python", 'app.py']


HEALTHCHECK --interval=30s --timeout=5s --retries=2 \
  CMD curl -f http://localhost:8000/ || exit 1