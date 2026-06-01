import random

class CustomsService:
    @staticmethod
    def get_customs_stats(category: str):
        """
        Simulated Customs & Logistics Data (HS Code Level Insight).
        Enhanced with Import Tariffs for major markets.
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
            "tariffs": {
                "USA": f"{random.choice(['0%', '2.5%', '7.5%'])} + 301 (25%)",
                "EU": f"{random.randint(0, 12)}%",
                "Southeast Asia (RCEP)": "0% (Form E Required)",
                "Latin America": f"{random.randint(10, 25)}%"
            },
            "top_exporting_countries": ["China", "Vietnam", "Germany", "South Korea"]
        }
