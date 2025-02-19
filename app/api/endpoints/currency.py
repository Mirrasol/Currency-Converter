from fastapi import APIRouter, Depends
from app.api.schemas.currency import Currency
from app.core.security import get_user_from_token
from app.utils.external_api import get_current_exchange_rates, get_currencies_list

currency_router = APIRouter(
    prefix='/currency',
    tags=['Currency'],
)


@currency_router.get('/list')
def show_currencies_list(user: str = Depends(get_user_from_token)):
    """ Get the list of the available currency codes"""
    currency_list = get_currencies_list()
    return currency_list


@currency_router.post('/exchange')
def exchange_currency(currencies: Currency, user: str = Depends(get_user_from_token)):
    """Convert from one currency to another"""
    result = get_current_exchange_rates(currencies)
    return result
