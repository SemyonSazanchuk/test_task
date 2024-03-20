import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel


class ContactData(BaseModel):
    address: str
    phone: int

app = FastAPI()

@app.post('/write_date')
async def write_data(record: ContactData):
    """
    Save phone number by address.
    """

    pass


@app.post('/write_date')
async def check_data():
    """
    Get address by phone number.
    """

    pass


if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8008)
