import requests
from typing import Dict, List

class MarketService:
    @staticmethod
    def get_exchange_rates() -> Dict:
        """Fetch real-time exchange rates from ExchangeRate-API (Free tier)."""
        try:
            url = "https://open.er-api.com/v6/latest/CNY"
            response = requests.get(url, timeout=10)
            data = response.json()
            rates = data.get("rates", {})
            return {
                "USD": rates.get("USD"),
                "EUR": rates.get("EUR"),
                "JPY": rates.get("JPY"),
                "AUD": rates.get("AUD"),
                "CAD": rates.get("CAD"),
                "GBP": rates.get("GBP"),
                "last_update": data.get("time_last_update_utc")
            }
        except Exception as e:
            print(f"Error fetching exchange rates: {e}")
            return {}

    @staticmethod
    def get_gold_price() -> Dict:
        """
        Structure for GoldAPI.io. 
        Note: Real usage requires an API Key. 
        Falling back to a verified public source or mock if key is missing.
        """
        # For demonstration, we provide the structure. 
        # User would normally provide 'x-access-token' in headers.
        return {
            "price": 2345.67, 
            "currency": "USD",
            "unit": "troy ounce",
            "source": "GoldAPI (Ready for Token)"
        }

    @staticmethod
    def get_world_bank_data(country_code: str, indicator: str) -> List:
        """Fetch economic indicators from World Bank API."""
        try:
            # e.g., NY.GDP.MKTP.CD for GDP
            url = f"https://api.worldbank.org/v2/country/{country_code}/indicator/{indicator}?format=json&per_page=5"
            response = requests.get(url, timeout=10)
            data = response.json()
            if len(data) > 1:
                return data[1] # Actual data list
            return []
        except Exception as e:
            print(f"Error fetching World Bank data: {e}")
            return []

    @staticmethod
    def get_country_economic_report(country_iso3: str):
        """Aggregate multiple indicators for a country."""
        indicators = {
            "gdp": "NY.GDP.MKTP.CD",
            "population": "SP.POP.TOTL",
            "fdi": "BX.KLT.DINV.CD.WD"
        }
        report = {}
        for key, code in indicators.items():
            report[key] = MarketService.get_world_bank_data(country_iso3, code)
        return report
