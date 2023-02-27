from flask import Flask, redirect
import stripe

# Stripe API
stripe.api_key = '************************************************************'
# Create a Web Server with Flask
app = Flask(__name__,
            static_url_path='',
            static_folder='public')

# URL Building with Flask
YOUR_DOMAIN = 'http://localhost:4242'



#Flask URL Paths and the Flask Debugger
# Python Decorator Functions and the @ Syntax

@app.route('/create-checkout-session', methods=['POST'])
def create_checkout_session():
    try:
        checkout_session = stripe.checkout.Session.create(
            line_items=[
                {
                    'price': '*****************************',
                    'quantity': 1,
                },
            ],
            mode='payment',
            success_url=YOUR_DOMAIN + '/success.html',
            cancel_url=YOUR_DOMAIN + '/cancel.html',
        )
    except Exception as e:
        return str(e)

    return redirect(checkout_session.url, code=303)


if __name__ == '__main__':
    app.run(port=4242)