from flask import Flask, jsonify, request

from flask_cors import CORS

app = Flask(__name__)
CORS(app)

transactions = []

@app.route('/transactions', methods=['GET'])
def get_transactions():
    return jsonify(transactions)

@app.route('/transactions', methods=['POST'])
def add_transaction():
    data = request.json
    transactions.append(data)
    return jsonify({'message': 'Transaction added successfully'})

@app.route('/transactions/clear', methods=['POST'])
def clear_transactions():
    global transactions
    transactions = []
    return jsonify({'message': 'Transactions cleared successfully'})

if __name__ == '__main__':
    app.run(debug=True)
