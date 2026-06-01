import random

class CompetitorService:
    @staticmethod
    def get_pricing_analysis(category: str):
        """
        Simulated competitor pricing analysis across regions.
        In production, this would scrape Amazon/Lazada/Allegro or use Pricing APIs.
        """
        regions = {
            "North America (Amazon)": {"currency": "USD", "base": 100},
            "Europe (Amazon/OTTO)": {"currency": "EUR", "base": 95},
            "Southeast Asia (Shopee/Lazada)": {"currency": "USD", "base": 70},
            "Latin America (Mercado Libre)": {"currency": "USD", "base": 85}
        }
        
        analysis = {}
        for region, info in regions.items():
            base = info["base"]
            analysis[region] = {
                "currency": info["currency"],
                "entry_level": round(base * random.uniform(0.7, 0.9), 2),
                "mid_range": round(base * random.uniform(1.1, 1.4), 2),
                "premium": round(base * random.uniform(1.8, 2.5), 2),
                "avg_discount": f"{random.randint(5, 20)}%",
                "top_competitors": ["Brand A", "Global Brand B", "Local Choice C"]
            }
        return analysis
