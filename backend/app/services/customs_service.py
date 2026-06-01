import random

class CustomsService:
    @staticmethod
    def get_customs_stats(category: str):
        """
        Simulated Customs & Logistics Data (HS Code Level Insight).
        In production, this would integrate with UN Comtrade or Chinese Customs API.
        """
        # Simulated HS Code mapping
        hs_codes = {
            "户外储能": "8507.60",
            "建材": "7308.90",
            "母婴": "9403.70",
            "电子": "8543.70"
        }
        hs = hs_codes.get(category, "8500.00")
        
        return {
            "hs_code": hs,
            "export_volume_yoy": f"+{random.randint(15, 45)}%",
            "top_export_hubs": ["Shenzhen", "Ningbo", "Guangzhou"],
            "main_destination_ports": ["Los Angeles, USA", "Rotterdam, Netherlands", "Singapore"],
            "average_shipping_days": {
                "Ocean (Mainland to US West)": 18,
                "Ocean (Mainland to Europe)": 35,
                "Air (Mainland to Global)": 5
            },
            "top_exporting_countries": ["China", "Vietnam", "Germany", "South Korea"]
        }
