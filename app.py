from flask import Flask, request, render_template
import pickle

app = Flask(__name__)

model_file = open('model_dt.pkl', 'rb')
model = pickle.load(model_file, encoding='bytes')

@app.route('/')
def index():
    return render_template('index.html', insurance_cost=0)

@app.route('/predict', methods=['POST'])
def predict():
    '''
    Predict the insurance cost based on user inputs
    and render the result to the html page
    '''
    age, job, marital, education, default, housing, loan, contact, month, day_of_week, duration, campaign, pdays, previous, poutcome = [x for x in request.form.values()]

    data = []

    data.append(int(age))
    data.append(int(job))
    data.append(int(marital))
    data.append(int(education))
    data.append(int(default))
    data.append(int(housing))
    data.append(int(loan))
    data.append(int(contact))
    data.append(int(month))
    data.append(int(day_of_week))
    data.append(int(duration))
    data.append(int(campaign))
    data.append(int(pdays))
    data.append(int(previous))
    data.append(int(poutcome))


    prediction = model.predict([data])
    if prediction==1 :
        output = "Bayar"
    else:
        output = "Gagal Bayar"

    return render_template('index.html', prediction=output, age=age, job=job, marital=marital, education=education, default=default, housing=housing, loan=loan, contact=contact, month=month, day_of_week=day_of_week, duration=duration, campaign=campaign, pdays=pdays, previous=previous, poutcome=poutcome)


if __name__ == '__main__':
    app.run(debug=True)
