FROM python:3.10-slim
WORKDIR /app
COPY requirements.txt .
COPY src src/
ENV PYTHONPATH "${PYTHONPATH}:/app"

RUN pip install --no-cache-dir --upgrade -r requirements.txt
EXPOSE 8008
CMD ["python3", "-m", "src.main"]