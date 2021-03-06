import flask
from flask import request, jsonify
from sample_response import sample_sessions

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/api/v2/appointment/sessions/public/findByPin', methods=['GET'])
def home():
    query_parameters = request.args
    date = query_parameters.get('date')
    pincode = query_parameters.get('pincode')

    return jsonify(sample_sessions)


if __name__ == '__main__':
    app.run()
