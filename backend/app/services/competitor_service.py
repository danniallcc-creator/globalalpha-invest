import random

class CompetitorService:
    @staticmethod
    def get_pricing_analysis(category: str):
        """
        Simulated competitor pricing analysis across regions.
        Enhanced with ratings, reviews and stock levels.
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
                "top_products": [
                    {
                        "name": f"Top Seller {random.choice(['X', 'Y', 'Z'])}",
                        "price": round(base * 1.2, 2),
                        "rating": round(random.uniform(4.2, 4.9), 1),
                        "reviews": random.randint(500, 15000),
                        "stock_status": random.choice(["In Stock", "Low Stock", "Out of Stock"])
                    },
                    {
                        "name": f"Rising Star {random.randint(1, 10)}",
                        "price": round(base * 0.9, 2),
                        "rating": round(random.uniform(4.5, 5.0), 1),
                        "reviews": random.randint(50, 400),
                        "stock_status": "In Stock"
                    }
                ]
            }
        return analysis
