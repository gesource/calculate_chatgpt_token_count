from flask import Flask, jsonify, request
from flask_cors import CORS
import tiktoken
import json

app = Flask(__name__)
CORS(app)

# 日本語を使えるように
app.config['JSON_AS_ASCII'] = False

@app.route('/', methods=['GET'])
def hello_world():
    return 'Hello, World!'

@app.route('/get_encoding', methods=['GET'])
def get_encoding():
    return jsonify({'encoding': list(tiktoken.model.MODEL_TO_ENCODING.keys())})

@app.route('/count_token', methods=['POST'])
def count_token():
    data = json.loads(request.data.decode('utf-8'))
    encoding = data['encoding']
    prompt = data['prompt']
    encoding = tiktoken.encoding_for_model(encoding)
    tokens = encoding.encode(prompt)
    return jsonify({'token_count': len(tokens)})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
