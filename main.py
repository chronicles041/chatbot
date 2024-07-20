from flask import Flask, request, jsonify

app = Flask(__name__)

# Route for student number
@app.route('/', methods=['GET'])
def home():
    return jsonify({"student_number": "200537767"})

# Route for webhook
@app.route('/webhook', methods=['POST'])
def webhook():
    req = request.get_json(silent=True, force=True)
    intent_name = req.get('queryResult').get('intent').get('displayName')

    if intent_name == 'GetWeather':
        fulfillment_text = "The weather today is sunny with a high of 25 degrees Celsius."
    else:
        fulfillment_text = "I'm not sure how to help with that."

    return jsonify({"fulfillmentText": fulfillment_text})

if __name__ == '__main__':
    app.run(debug=True)
