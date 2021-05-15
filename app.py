from flask import Flask, render_template, request
import jsonify
import requests
import pickle
import sklearn
app = Flask(__name__)
model = pickle.load(open('logreg_model.pkl', 'rb'))
@app.route('/',methods=['GET'])
def Home():
    return render_template('index.html')

@app.route("/predict", methods=['POST'])
def predict():
    if request.method == 'POST':
        age = int(request.form['age'])
        dept=request.form['dept']
        if (dept == 'rd'):
            dept = 961
        elif (dept == 'sales'):
            dept = 446
        else:
            dept = 63
        dfh = int(request.form['distance'])
        edu= request.form['education']
        if (edu == 'belowclg'):
            edu = 1
        elif (edu == 'clg'):
            edu = 2
        elif (edu == 'bachelor'):
            edu = 3
        elif (edu == 'master'):
            edu = 4
        else:
            edu = 5
        ef=request.form['ef']
        if (ef == 'ls'):
            ef = 606
        elif (ef == 'medical'):
            ef = 464
        elif (ef == 'marketing'):
            ef = 159
        elif (ef == 'td'):
            ef = 132
        elif (ef == 'hrs'):
            ef = 27
        else:
            ef = 82
        envsat=request.form['envsat']
        if (envsat == 'low'):
            envsat = 1
        elif (envsat == 'medium'):
            envsat = 2
        elif (envsat == 'high'):
            envsat = 3
        else:
            envsat = 4
        jobsat = request.form['jobsat']
        if (jobsat == 'bad'):
            jobsat = 1
        elif (jobsat == 'good'):
            jobsat = 2
        elif (jobsat == 'better'):
            jobsat = 3
        else:
            jobsat = 4
        ms=request.form['marstat']
        if (ms == 'single'):
            ms = 470
        elif (ms == 'married'):
            ms = 673
        else:
            ms = 327
        mi=int(request.form['mi'])
        ncw = int(request.form['ncw'])
        wlb = request.form['wlb']
        if (wlb == 'bad'):
            wlb = 1
        elif (wlb == 'good'):
            wlb = 2
        elif (wlb == 'better'):
            wlb = 3
        else:
            wlb = 4
        ytc = int(request.form['ytc'])

        prediction=model.predict([[age,dept,dfh,edu,ef,envsat,jobsat,ms,mi,ncw,wlb,ytc]])
        output=prediction[0]


        if output==0:
            return render_template('index.html',prediction_text="Employee Attrition(Reduction) is very unlikely to happen")
        else:
            return render_template('index.html',prediction_text="Employee Attrition(Reduction) likely to happen")
    else:
        return render_template('index.html')

if __name__=="__main__":
    app.run(debug=True)

