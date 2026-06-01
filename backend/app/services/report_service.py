from fpdf import FPDF
import os
from datetime import datetime

class ReportService:
    @staticmethod
    def generate_pdf(category: str, data: dict, output_path: str):
        pdf = FPDF()
        pdf.set_auto_page_break(auto=True, margin=15)
        
        # --- COVER PAGE ---
        pdf.add_page()
        pdf.set_fill_color(26, 43, 60) # Deep Navy
        pdf.rect(0, 0, 210, 297, 'F')
        
        pdf.set_text_color(255, 255, 255)
        pdf.set_font("Helvetica", "B", 32)
        pdf.set_y(80)
        pdf.cell(0, 20, "CROSS-BORDER", ln=True, align="C")
        pdf.cell(0, 20, "INTEL REPORT", ln=True, align="C")
        
        pdf.set_font("Helvetica", "", 18)
        pdf.ln(20)
        pdf.cell(0, 10, f"Industry: {category.upper()}", ln=True, align="C")
        
        pdf.set_font("Helvetica", "I", 12)
        pdf.set_y(250)
        pdf.cell(0, 10, f"Generated on: {datetime.now().strftime('%Y-%m-%d')}", ln=True, align="C")
        pdf.cell(0, 10, "Confidential Business Intelligence", ln=True, align="C")

        # --- SECTION 1: MARKET RESEARCH (市场调研) ---
        pdf.add_page()
        pdf.set_text_color(0, 0, 0)
        pdf.set_font("Helvetica", "B", 18)
        pdf.cell(0, 15, "1. Market Research & Layout", ln=True)
        pdf.line(10, pdf.get_y(), 200, pdf.get_y())
        pdf.ln(5)
        
        pdf.set_font("Helvetica", "", 10)
        pdf.multi_cell(0, 6, f"Promising markets for '{category}' based on macroeconomic indicators and consumption power.")
        pdf.ln(3)

        recs = data.get("recommendations", {})
        for key, countries in recs.items():
            pdf.set_font("Helvetica", "B", 12)
            pdf.set_text_color(26, 43, 60)
            pdf.cell(0, 8, f"Segment: {key.replace('_', ' ').title()}", ln=True)
            pdf.set_text_color(0, 0, 0)
            for country in countries:
                pdf.set_font("Helvetica", "", 10)
                details = data.get("market_details", {}).get(country['name'], {})
                pdf.cell(0, 6, f" • {country['name']}: GDP ${details.get('gdp', 'N/A')} | Pop {details.get('population', 'N/A')}M", ln=True)
            pdf.ln(2)

        # --- SECTION 2: COMPETITOR PRICING (竞争对手价格监测) ---
        pdf.add_page()
        pdf.set_font("Helvetica", "B", 18)
        pdf.cell(0, 15, "2. Competitor Pricing Analysis", ln=True)
        pdf.line(10, pdf.get_y(), 200, pdf.get_y())
        pdf.ln(5)
        
        pricing = data.get("pricing_analysis", {})
        for region, info in pricing.items():
            pdf.set_font("Helvetica", "B", 11)
            pdf.cell(0, 8, f"Region: {region}", ln=True)
            pdf.set_font("Helvetica", "", 10)
            pdf.cell(0, 6, f"  - Entry-Level: {info['currency']} {info['entry_level']}", ln=True)
            pdf.cell(0, 6, f"  - Mid-Range: {info['currency']} {info['mid_range']}", ln=True)
            pdf.cell(0, 6, f"  - Premium: {info['currency']} {info['premium']}", ln=True)
            pdf.cell(0, 6, f"  - Avg Discount: {info['avg_discount']} | Competitors: {', '.join(info['top_competitors'])}", ln=True)
            pdf.ln(2)

        # --- SECTION 3: CUSTOMS & LOGISTICS (海关数据看板) ---
        pdf.add_page()
        pdf.set_font("Helvetica", "B", 18)
        pdf.cell(0, 15, "3. Customs & Logistics Insights", ln=True)
        pdf.line(10, pdf.get_y(), 200, pdf.get_y())
        pdf.ln(5)
        
        c = data.get("customs_stats", {})
        pdf.set_font("Helvetica", "B", 11)
        pdf.cell(0, 8, f"HS Code Category: {c.get('hs_code', 'N/A')}", ln=True)
        pdf.set_font("Helvetica", "", 10)
        pdf.cell(0, 6, f"  - Global Export Volume Trend: {c.get('export_volume_yoy', 'N/A')} YoY", ln=True)
        pdf.cell(0, 6, f"  - Top Export Hubs: {', '.join(c.get('top_export_hubs', []))}", ln=True)
        pdf.cell(0, 6, f"  - Main Ports: {', '.join(c.get('main_destination_ports', []))}", ln=True)
        pdf.ln(3)
        pdf.set_font("Helvetica", "B", 11)
        pdf.cell(0, 8, "Estimated Logistics Lead Times:", ln=True)
        pdf.set_font("Helvetica", "", 10)
        for route, days in c.get("average_shipping_days", {}).items():
            pdf.cell(0, 6, f"  * {route}: {days} days", ln=True)

        # --- SECTION 4: INDUSTRY & SOCIAL TRENDS (行业与社交趋势) ---
        pdf.add_page()
        pdf.set_font("Helvetica", "B", 18)
        pdf.cell(0, 15, "4. E-commerce & Social Trends", ln=True)
        pdf.line(10, pdf.get_y(), 200, pdf.get_y())
        pdf.ln(5)
        
        ecom = data.get("ecom_trends", {})
        for region, items in ecom.items():
            pdf.set_font("Helvetica", "B", 11)
            pdf.cell(0, 8, f"Platform Context: {region}", ln=True)
            pdf.set_font("Helvetica", "", 10)
            for item in items:
                pdf.cell(0, 6, f"  - {item['platform']}: {item['product']} (Growth: {item['growth']})", ln=True)
        pdf.ln(3)
        pdf.set_font("Helvetica", "B", 11)
        pdf.cell(0, 8, "TikTok Viral Monitoring:", ln=True)
        pdf.set_font("Helvetica", "", 10)
        for v in data.get("tiktok_trends", []):
            pdf.cell(0, 6, f"  - {v['title']} ({v['play_count']} views)", ln=True)

        # --- SECTION 5: COMPLIANCE & REDLINES (合规红线) ---
        pdf.add_page()
        pdf.set_font("Helvetica", "B", 18)
        pdf.cell(0, 15, "5. Product Compliance Redlines", ln=True)
        pdf.line(10, pdf.get_y(), 200, pdf.get_y())
        pdf.ln(5)
        for item in data.get("compliance_info", []):
            pdf.set_font("Helvetica", "B", 12); pdf.set_text_color(192, 57, 43)
            pdf.cell(0, 8, f"Warning: {item['category']}", ln=True)
            pdf.set_text_color(0, 0, 0); pdf.set_font("Helvetica", "", 10)
            pdf.multi_cell(0, 6, f"Reason: {item['reason']}")
            pdf.set_font("Helvetica", "B", 10); pdf.set_text_color(39, 174, 96)
            pdf.cell(0, 8, "Solution:", ln=True)
            pdf.set_text_color(0, 0, 0); pdf.set_font("Helvetica", "", 10)
            pdf.multi_cell(0, 6, item['breakthrough'])
            pdf.ln(4)

        # --- SECTION 6: STRATEGIC RECOMMENDATIONS (战略建议) ---
        pdf.add_page()
        pdf.set_font("Helvetica", "B", 18)
        pdf.cell(0, 15, "6. Final Strategic Recommendations", ln=True)
        pdf.line(10, pdf.get_y(), 200, pdf.get_y())
        pdf.ln(5)
        pdf.set_font("Helvetica", "I", 12)
        pdf.multi_cell(0, 8, data.get("ai_insight", ""))
        
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        pdf.output(output_path)
        return output_path
