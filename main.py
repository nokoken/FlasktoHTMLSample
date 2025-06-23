import csv
from flask import Flask, jsonify, render_template

path = "./data.csv"
with open(path, encoding='shift_jis', newline='') as f:
    csvreader = csv.reader(f)
    list_csv = list(csvreader)

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get-data')
def get_data():
    global list_csv
    return jsonify(list_csv)

if __name__ == '__main__':
    app.run(debug=True)