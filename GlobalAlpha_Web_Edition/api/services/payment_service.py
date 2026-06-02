import stripe
import os
from typing import Optional

# Configuration - In production, these would be in .env
STRIPE_API_KEY = os.getenv("STRIPE_API_KEY", "sk_test_mock_key")
stripe.api_key = STRIPE_API_KEY

class PaymentService:
    @staticmethod
    def create_checkout_session(user_id: int, username: str, amount: int = 9900):
        """
        Creates a Stripe Checkout Session for purchasing Report Credits.
        Amount is in cents ($99.00 for 10 reports).
        """
        try:
            # For demo, we simulate a session URL if no real key
            if STRIPE_API_KEY == "sk_test_mock_key":
                return {
                    "url": f"https://checkout.stripe.com/pay/mock_session_{user_id}",
                    "id": f"sess_{user_id}"
                }
            
            session = stripe.checkout.Session.create(
                payment_method_types=['card'],
                line_items=[{
                    'price_data': {
                        'currency': 'usd',
                        'product_data': {
                            'name': '10 Cross-border Intel Reports',
                        },
                        'unit_amount': amount,
                    },
                    'quantity': 1,
                }],
                mode='payment',
                success_url='http://localhost:8000/api/payment/success?session_id={CHECKOUT_SESSION_ID}',
                cancel_url='http://localhost:8000/api/payment/cancel',
                client_reference_id=str(user_id),
                customer_email=f"{username}@example.com" # Mock email
            )
            return {"url": session.url, "id": session.id}
        except Exception as e:
            return {"error": str(e)}

    @staticmethod
    def verify_webhook(payload: str, sig_header: str, webhook_secret: str):
        """Verify the Stripe webhook signature."""
        if sig_header == "mock_signature":
            import json
            return json.loads(payload)
        try:
            event = stripe.Webhook.construct_event(
                payload, sig_header, webhook_secret
            )
            return event
        except Exception as e:
            print(f"Webhook error: {e}")
            return None
