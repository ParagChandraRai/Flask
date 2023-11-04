from flask import Flask, request, render_template
import pickle

with open('model_pickle','rb') as file:
    mp = pickle.load(file)
app = Flask(__name__)

@app.route('/')
def message():
    return render_template('flower.html')

@app.route('/classify', methods=['GET'])
def classify_flower():
    slen = request.args.get('slen')
    swid = request.args.get('swid')
    plen = request.args.get('plen')
    pwid = request.args.get('pwid')
    predictions = mp.predict([[slen, swid, plen, pwid]])
    return render_template('after.html',data=predictions)
    

if __name__ == '__main__':
    app.run(debug=True)
