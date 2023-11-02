from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api/data', methods=['GET', 'POST'])
def get_or_post_data():
    if request.method == 'GET':
        # Simulate getting data from the database or another source.
        data = {'message': 'This is data from the backend.'}
        return jsonify(data)
    elif request.method == 'POST':
        # Get data from the Flutter frontend.
        request_data = request.get_json()
        # Process the data as needed.
        response_data = {'message': 'Data received and processed on the backend.'}
        return jsonify(response_data)

class Data:
    def __init__(self, fname:str, calcount:int, typemeal:str, date:str):
        self.fname = fname
        self.calcount = calcount
        self.typemeal = typemeal
        self.date = date

    def get_data(self):
        return f"{self.fname}, {self.calcount}, {self.typemeal}, {self.date}"


if __name__ == '__main__':
    app.run(debug=True)

