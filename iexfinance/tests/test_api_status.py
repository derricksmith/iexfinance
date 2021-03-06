import pandas as pd
import pytest

from iexfinance.tools.api import get_api_status


@pytest.mark.cloud
class TestAPIStatus(object):

    def test_api_status_json(self):
        data = get_api_status()

        assert isinstance(data, dict)

    def test_api_status_pandas(self):
        data = get_api_status(output_format='pandas')

        assert isinstance(data, pd.DataFrame)
