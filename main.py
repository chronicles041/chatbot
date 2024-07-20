from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"student_number": "123456789"})  # Replace with your student number

@app.route('/webhook', methods=['POST'])
def webhook():
    req = request.get_json(silent=True, force=True)
    return jsonify({"fulfillmentText": "The weather today is sunny with a high of 25 degrees Celsius."})

if __name__ == '__main__':
    app.run()
