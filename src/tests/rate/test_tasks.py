from unittest.mock import MagicMock

from rate.models import Rate
from rate.tasks import parse_privatbank


def test_parse_privatbank(mocker):
    count_rates = Rate.objects.count()
    currencies = [{"ccy": "USD", "base_ccy": "UAH", "buy": "28.20000", "sale": "28.60000"},
                  {"ccy": "EUR", "base_ccy": "UAH", "buy": "33.00000", "sale": "33.60000"},
                  {"ccy": "RUR", "base_ccy": "UAH", "buy": "0.35400", "sale": "0.39400"},
                  {"ccy": "BTC", "base_ccy": "USD", "buy": "12893.1627", "sale": "14250.3377"}]
    requests_get_patcher = mocker.patch('requests.get')
    requests_get_patcher.return_value = MagicMock(
        status_code=200,
        json=lambda: currencies
    )
    parse_privatbank()
    assert Rate.objects.count() == count_rates + 2

    # we save rates if amount of buy or sale field was changed
    parse_privatbank()
    assert Rate.objects.count() == count_rates + 2
