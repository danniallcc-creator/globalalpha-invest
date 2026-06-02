import random
from typing import List, Dict

class LocalEcomService:
    @staticmethod
    def get_regional_trends(region: str) -> List[Dict]:
        """
        Mock data for local e-commerce platforms based on real-world trends in 2026.
        Regions: SE_ASIA (Shopee), LATAM (Mercado Libre), EU_GERMANY (OTTO)
        """
        if region == "SE_ASIA":
            return [
                {"platform": "Shopee", "product": "Wireless Earbuds (Active Noise Canceling)", "trend": "Trending in PH/TH/ID", "growth": "42%", "icon": "🎧"},
                {"platform": "Lazada", "product": "Portable Blender (USB-C Rechargeable)", "trend": "Healthy lifestyle surge", "growth": "38%", "icon": "🥤"},
                {"platform": "Shopee", "product": "Smartwatch (AOD Display)", "trend": "Affordable luxury trend", "growth": "31%", "icon": "⌚"}
            ]
        elif region == "LATAM":
            return [
                {"platform": "Mercado Libre", "product": "Solar Flood Lights (Outdoor)", "trend": "Security & Sustainability", "growth": "55%", "icon": "💡"},
                {"platform": "Mercado Libre", "product": "Smartphone Stabilizer/Gimbal", "trend": "Content creation boom in Brazil", "growth": "47%", "icon": "📸"},
                {"platform": "Amazon MX", "product": "Air Fryer (XL Capacity)", "trend": "Kitchen efficiency focus", "growth": "29%", "icon": "🍟"}
            ]
        elif region == "EU_GERMANY":
            return [
                {"platform": "OTTO", "product": "Smart Home Hub (Energy Monitoring)", "trend": "Energy crisis response", "growth": "62%", "icon": "🏠"},
                {"platform": "OTTO", "product": "Ergonomic Office Chair", "trend": "Long-term WFH upgrade", "growth": "24%", "icon": "💺"},
                {"platform": "Zalando", "product": "Eco-friendly Sportswear", "trend": "Sustainable fashion demand", "growth": "19%", "icon": "👟"}
            ]
        return []

    @staticmethod
    def get_all_platforms() -> Dict[str, List[Dict]]:
        return {
            "Southeast Asia": LocalEcomService.get_regional_trends("SE_ASIA"),
            "Latin America": LocalEcomService.get_regional_trends("LATAM"),
            "Germany (EU)": LocalEcomService.get_regional_trends("EU_GERMANY")
        }
