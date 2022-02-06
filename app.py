from flask import Flask, render_template, request
import pickle
import numpy as np
from sklearn.preprocessing import LabelEncoder

model = pickle.load(open('iri.pkl', 'rb'))

app = Flask(__name__)

@app.route('/')
def man():
    return render_template('index.html')
@app.route('/ques')
def quest():
    return render_template('home.html')
@app.route('/engg')
def engg():
    return render_template('eng.html')

@app.route('/doc')
def doc():
    return render_template('doct.html')

@app.route('/ep1')
def bnl():
    return render_template('basic.html')

@app.route('/ec1')
def bnll():
    return render_template('basic1.html')

@app.route('/eps1')
def blll():
    return render_template('basic2.html')

@app.route('/ep2')
def az():
    return render_template('adv.html')

@app.route('/eps1')
def bllz():
    return render_template('basic2.html')

@app.route('/ep2')
def al():
    return render_template('adv.html')

@app.route('/ps1')
def docz():
    return render_template('basic3.html')

@app.route('/ei1')
def docc():
    return render_template('basic4.html')

@app.route('/as1')
def doccc():
    return render_template('basic5.html')

@app.route('/ps2')
def doct():
    return render_template('adv3.html')

@app.route('/ei2')
def doctt():
    return render_template('adv4.html')

@app.route('/as2')
def docct():
    return render_template('adv5.html')

@app.route('/ec2')
def all():
    return render_template('adv1.html')

@app.route('/eps2')
def alll():
    return render_template('adv2.html')

@app.route('/bd1')
def bd():
    return render_template('business-decision1.html')

@app.route('/bd2')
def bdd():
    return render_template('business-decision2.html')

@app.route('/bl1')
def bl():
    return render_template('business-leader1.html')

@app.route('/bl2')
def bll():
    return render_template('business-leader2.html')

@app.route('/pd1')
def pd():
    return render_template('police-decision1.html')

@app.route('/pd2')
def pdd():
    return render_template('police-decision2.html')

@app.route('/pm1')
def pm():
    return render_template('police-morality1.html')

@app.route('/CA')
def enggj():
    return render_template('ca1.html')

@app.route('/FD')
def docsdf():
    return render_template('vedios.html')

@app.route('/ca2')
def enggsdfs():
    return render_template('ca2.html')

@app.route('/fd2')
def docaa():
    return render_template('ved2.html')

@app.route('/law1')
def law():
    return render_template('lawyerguidance1.html')

@app.route('/lawmain')
def lawm():
    return render_template('lawyer.html')

@app.route('/policemain')
def policem():
    return render_template('police.html')

@app.route('/fashionmain')
def fashionm():
    return render_template('fashion.html')

@app.route('/CAmain')
def CAm():
    return render_template('CA.html')

@app.route('/docmain')
def docm():
    return render_template('doc.html')

@app.route('/enggmain')
def enggm():
    return render_template('eng1.html')

@app.route('/bussmain')
def bussm():
    return render_template('buss.html')

@app.route('/law2')
def laww():
    return render_template('lawyerguidance2.html')

@app.route('/thank')
def ty():
    return render_template('thankyou.html')

@app.route('/predict', methods=['POST'])
def home():
    to_predict_list = request.form.to_dict()
    to_predict_list = list(to_predict_list.values())
    to_predict_list = list(map(int, to_predict_list))
    to_predict = np.array(to_predict_list).reshape(1,21)
    
    pred = model.predict(to_predict)
    return render_template('after.html', data=pred)

if __name__ == "__main__":
    app.run(debug=True)
