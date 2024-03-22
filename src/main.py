import os

import uvicorn
from fastapi import FastAPI, Response
from pydantic import BaseModel
import redis


class ContactData(BaseModel):
    address: str
    phone: int


app = FastAPI()
redis_host = os.environ.get('REDIS_HOST', 'localhost')
redis_port = int(os.environ.get('REDIS_PORT', 6379))
redis_client = redis.Redis(host=redis_host, port=redis_port, decode_responses=True)


@app.post('/write_data')
async def write_data(response: Response, record: ContactData):
    """
    Save phone number and address to storage.
    """
    result = redis_client.set(record.phone, record.address)
    if not result:
        response.status_code = 500


@app.get('/check_data')
async def check_data(response: Response, phone: int):
    """
    Get address by phone number from storage.
    """
    result = redis_client.get(phone)
    if result is None:
        response.status_code = 400
    return result


if __name__ == '__main__':
    host = os.environ.get('APP_HOST', '0.0.0.0')
    port = int(os.environ.get('APP_PORT', 8008))
    uvicorn.run(app, host=host, port=port)
