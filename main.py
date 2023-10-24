import pickle

import numpy as np
from flask import Flask, render_template, request

app = Flask(__name__)
model = pickle.load(open('model/model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict', methods=['GET', 'POST'])
def predict():
    age = int(request.form.get('age'))
    exp = int(request.form.get('exp'))
    income = int(request.form.get('income'))
    family = int(request.form.get('family'))
    cd_raw = request.form.get('cd')
    online_raw = request.form.get('online')
    if cd_raw == 'Yes':
        cd = int(1)
    else:
        cd = int(0)

    if online_raw == 'Yes':
        online = int(1)
    else:
        online = int(0)

    data = [[age, exp, income, family, cd, online]]
    prediction = model.predict(data)

    result = round(prediction[0], 2)

    return render_template('index.html', prediction_output=result)

if __name__ == '__main__':
    app.run(debug=True)
