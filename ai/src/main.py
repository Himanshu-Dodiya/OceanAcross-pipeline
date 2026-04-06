from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def predict():
    return jsonify({ 'service': 'ai', 'prediction': 'demo', 'status': 'ok','message': 'AI service is running successfully' })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)