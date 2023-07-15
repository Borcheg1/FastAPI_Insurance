import decimal
from datetime import date

from fastapi import status, Body, APIRouter

from src.models import RateModel


router = APIRouter()


@router.post("/rate", status_code=status.HTTP_201_CREATED)
async def add_rates(rate_dict: dict = Body(...)):
    """
    ### add to database some data\n
    ### example data format
    ~~~
    {
      "2020-06-01": [
        {
          "cargo_type": "Glass",
          "rate": "0.04"
        },
        {
          "cargo_type": "Other",
          "rate": "0.01"
        }
      ]
    }
    ~~~
    """
    for key, values in rate_dict.items():
        date_from = key
        for rate in values:
            try:
                if not await RateModel.exists(
                        date_from=date_from,
                        cargo_type=rate["cargo_type"],
                        current_rate=rate["rate"]
                ):
                    await RateModel.create(
                        date_from=date_from,
                        cargo_type=rate["cargo_type"],
                        current_rate=rate["rate"]
                    )
            except Exception as error:
                print(error)
    return {f"message: rates added successfully"}


@router.get("/check", status_code=status.HTTP_200_OK)
async def check_rate(date_from: date, cargo_type: str, price: decimal.Decimal):
    """
    **date_from:** date in format 2023-06-24<br>
    **cargo_type:** string<br>
    **price:** decimal<br>
    **return:** calculation of the cost of insurance, JSON
    ### return example
    ~~~
    {
      "payable": 2
    }
    ~~~
    """
    try:
        query = await RateModel.filter(date_from=date_from, cargo_type=cargo_type).first()
        if query:
            return {"payable": price * query.current_rate}
        return {"message": "Date or cargo_type not found"}
    except Exception as error:
        print(f"{error}, try again")
