from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/',methods=['GET'])
def test():
    try:
        return jsonify({"status": "get", "message": "api working"})
    except Exception as e:
        return jsonify({"message":"not working"})


@app.route('/payment', methods=['POST'])
def process_payment():
    try:
        # Extract data from the request
        data = request.get_json()

        # Perform payment processing logic (replace this with your actual payment processing code)
        amount = data.get('amount')
        payment_method = data.get('payment_method')
        server=data.get('server')
        # Your payment processing code goes here...

        # Assume the payment is successful for this example
        success=True
        if(server==False):
            success=False

        if success:
            return jsonify({"status": "success", "message": "Payment successful","amount":amount,"payment_method":payment_method})
        else:
            return jsonify({"status": "failure", "message": "Payment failed"})

    except Exception as e:
        return jsonify({"status": "error", "message": str(e)})

if __name__ == '_main_':
    app.run(debug=True)