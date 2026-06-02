import requests
import random

class TrendsService:
    @staticmethod
    def get_tiktok_trends(keyword: str):
        # In a real app, this would use TikTok API or a professional scraper
        # Using real-world data discovered in our research
        return {
            "hashtags": ["#portablepowerstation", "#solargenerator", "#offgridlife", "#greenenergy", "#vanlife"],
            "vibe": "Focus on high-capacity LiFePO4 batteries and fast-charging tech.",
            "top_engagement_region": "North America / Europe"
        }

    @staticmethod
    def get_amazon_trends(keyword: str):
        # Real-world data discovered: LiFePO4, 1.5H Fast Charge, UPS, Hybrid Inverter
        return {
            "top_sellers": [
                {"name": "LIBRIDS C600 (640Wh LiFePO4)", "price": "$599", "features": "1.5H Fast Charge, UPS"},
                {"name": "GENMAX 5500W Hybrid 2026", "price": "$1299", "features": "Hybrid Inverter"}
            ],
            "hot_keywords": ["Fast Charge", "UPS mode", "Outdoor Backup", "LiFePO4"]
        }

    @staticmethod
    def get_ai_insight(category: str):
        return (
            f"针对 {category} 市场，2026 年的核心突破点在于‘极端天气适应性’（低至 -20℃ 充放电）"
            "和‘多模态能源管理’。建议重点布局具有 UPS 功能和 1.5 小时内充满电的快充机型。"
        )
