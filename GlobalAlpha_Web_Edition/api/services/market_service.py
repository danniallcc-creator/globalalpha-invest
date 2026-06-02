import requests
from typing import Dict, List

class MarketService:
    @staticmethod
    def get_exchange_rates() -> Dict:
        """
        Fetch exchange rates. 
        Tries Frankfurter.app (ECB data, reliable for closing/reference) 
        and falls back to ExchangeRate-API.
        """
        try:
            # Try Frankfurter (Uses European Central Bank data)
            url = "https://api.frankfurter.app/latest?from=CNY"
            response = requests.get(url, timeout=5)
            if response.status_code == 200:
                data = response.json()
                rates = data.get("rates", {})
                # Note: Rates are 1 CNY = X Currency. We invert later.
                return {
                    "USD": 1/rates.get("USD") if rates.get("USD") else 6.76,
                    "EUR": 1/rates.get("EUR") if rates.get("EUR") else 7.87,
                    "JPY": 1/rates.get("JPY") if rates.get("JPY") else 0.042,
                    "AUD": 1/rates.get("AUD") if rates.get("AUD") else 4.51,
                    "CAD": 1/rates.get("CAD") if rates.get("CAD") else 4.90,
                    "GBP": 1/rates.get("GBP") if rates.get("GBP") else 9.13,
                    "last_update": data.get("date"),
                    "source": "ECB (Frankfurter)"
                }
        except:
            pass

        try:
            # Fallback to ExchangeRate-API
            url = "https://open.er-api.com/v6/latest/CNY"
            response = requests.get(url, timeout=5)
            data = response.json()
            rates = data.get("rates", {})
            return {
                "USD": rates.get("USD"),
                "EUR": rates.get("EUR"),
                "JPY": rates.get("JPY"),
                "AUD": rates.get("AUD"),
                "CAD": rates.get("CAD"),
                "GBP": rates.get("GBP"),
                "last_update": data.get("time_last_update_utc"),
                "source": "ExchangeRate-API"
            }
        except Exception as e:
            print(f"Error fetching exchange rates: {e}")
            return {}

    @staticmethod
    def get_gold_price() -> Dict:
        """
        Current London Gold (XAU/USD) 2026 Reference.
        For real-time production, please provide a GoldAPI.io or MetalPriceAPI key.
        """
        # Current discovered 2026-06-01 price: ~$4,522.57
        # Previous Close: ~$4,539.27
        return {
            "price": 4522.57, 
            "prev_close": 4539.27,
            "change": "-0.37%",
            "currency": "USD",
            "unit": "troy ounce",
            "last_update": "2026-06-01 10:00 UTC",
            "source": "Market Consensus (Mock for 2026)"
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
