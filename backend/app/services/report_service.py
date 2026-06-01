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
        pdf.set_font("Helvetica", "B", 20)
        pdf.cell(0, 15, "1. Market Research & Layout", ln=True)
        pdf.line(10, pdf.get_y(), 200, pdf.get_y())
        pdf.ln(5)
        
        pdf.set_font("Helvetica", "", 11)
        pdf.multi_cell(0, 7, f"This section provides an overview of the most promising markets for '{category}' based on macroeconomic indicators, consumption power, and growth potential.")
        pdf.ln(5)

        recs = data.get("recommendations", {})
        for key, countries in recs.items():
            pdf.set_font("Helvetica", "B", 14)
            pdf.set_text_color(26, 43, 60)
            pdf.cell(0, 10, f"Target Segment: {key.replace('_', ' ').title()}", ln=True)
            pdf.set_text_color(0, 0, 0)
            
            for country in countries:
                pdf.set_font("Helvetica", "B", 12)
                pdf.cell(0, 8, f"• {country['name']}", ln=True)
                pdf.set_font("Helvetica", "", 10)
                
                # Fetching mock/real economic details if available in data
                details = data.get("market_details", {}).get(country['name'], {})
                gdp = details.get("gdp", "N/A")
                pop = details.get("population", "N/A")
                
                pdf.multi_cell(0, 6, f"  - Market Dynamics: High demand for '{category}' driven by {country.get('reason', 'local consumption trends')}.")
                pdf.cell(0, 6, f"  - Economic Data: GDP (Nominal) ${gdp} | Population {pop}M", ln=True)
                pdf.ln(2)
            pdf.ln(5)

        # --- SECTION 2: INDUSTRY ANALYSIS (行业分析) ---
        pdf.add_page()
        pdf.set_font("Helvetica", "B", 20)
        pdf.cell(0, 15, "2. Industry & Platform Analysis", ln=True)
        pdf.line(10, pdf.get_y(), 200, pdf.get_y())
        pdf.ln(5)
        
        pdf.set_font("Helvetica", "B", 14)
        pdf.cell(0, 10, "Global Platform Trends (E-commerce)", ln=True)
        pdf.set_font("Helvetica", "", 10)
        
        ecom_data = data.get("ecom_trends", {})
        for region, items in ecom_data.items():
            pdf.set_font("Helvetica", "B", 11)
            pdf.cell(0, 8, f"Region: {region}", ln=True)
            pdf.set_font("Helvetica", "", 10)
            for item in items:
                pdf.cell(0, 6, f"  * {item['platform']}: {item['product']} (Growth: {item['growth']})", ln=True)
            pdf.ln(2)
            
        pdf.ln(5)
        pdf.set_font("Helvetica", "B", 14)
        pdf.cell(0, 10, "Social Media Buzz (TikTok & Trends)", ln=True)
        pdf.set_font("Helvetica", "", 10)
        
        tiktok_data = data.get("tiktok_trends", [])
        for video in tiktok_data:
            pdf.cell(0, 6, f"  - {video['title']} ({video['play_count']} views by {video['author']})", ln=True)
        
        # --- SECTION 3: PRODUCT & COMPLIANCE (产品与合规) ---
        pdf.add_page()
        pdf.set_font("Helvetica", "B", 20)
        pdf.cell(0, 15, "3. Product Analysis & Compliance", ln=True)
        pdf.line(10, pdf.get_y(), 200, pdf.get_y())
        pdf.ln(5)
        
        compliance_items = data.get("compliance_info", [])
        if not compliance_items:
            pdf.set_font("Helvetica", "I", 10)
            pdf.cell(0, 10, "No specific compliance data found for this category. General standards apply.", ln=True)
        else:
            for item in compliance_items:
                pdf.set_font("Helvetica", "B", 13)
                pdf.set_text_color(192, 57, 43) # Dark Red for Warning
                pdf.cell(0, 8, f"Compliance Redlines: {item['category']}", ln=True)
                pdf.set_text_color(0, 0, 0)
                pdf.set_font("Helvetica", "", 10)
                pdf.multi_cell(0, 6, f"Reason for Restriction: {item['reason']}")
                pdf.ln(2)
                
                pdf.set_font("Helvetica", "B", 11)
                pdf.set_text_color(39, 174, 96) # Green for Success
                pdf.cell(0, 8, "Transformation & Strategic Breakthrough:", ln=True)
                pdf.set_text_color(0, 0, 0)
                pdf.set_font("Helvetica", "", 10)
                pdf.multi_cell(0, 6, f"{item['breakthrough']}")
                pdf.ln(2)
                pdf.multi_cell(0, 6, f"Expert Suggestion: {item['suggestion']}")
                pdf.ln(5)

        # --- SECTION 4: STRATEGIC RECOMMENDATIONS (战略建议) ---
        pdf.ln(10)
        pdf.set_font("Helvetica", "B", 20)
        pdf.cell(0, 15, "4. Strategic Recommendations", ln=True)
        pdf.line(10, pdf.get_y(), 200, pdf.get_y())
        pdf.ln(5)
        
        pdf.set_font("Helvetica", "I", 12)
        pdf.set_text_color(50, 50, 50)
        pdf.multi_cell(0, 8, data.get("ai_insight", "Expand your presence in high-growth blue ocean markets while ensuring certifications for high-profit premium regions."))
        
        # --- FOOTER ON ALL PAGES (fpdf handles this via footer method if overridden, but we'll do it manually for simplicity here) ---
        
        # Ensure directory exists
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        pdf.output(output_path)
        return output_path
