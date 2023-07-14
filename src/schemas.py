import decimal
from datetime import date

from pydantic import BaseModel


class CheckRate(BaseModel):
    date: date
    cargo_type: str
    rate: decimal.Decimal
