from flask import render_template, Flask, request
import pickle
app = Flask(__name__)

MADHYA_MAHARASHTRA= pickle.load(open('./model/MADHYA_MAHARASHTRA_model.pkl','rb'))
MATATHWADA= pickle.load(open('./model/MATATHWADA.pkl','rb'))
VIDARBHA= pickle.load(open('./model/VIDARBHA.pkl','rb'))
E_raj= pickle.load(open('./model/raj_east_model.pkl','rb'))
W_Raj= pickle.load(open('./model/raj_west_model.pkl','rb'))
Tam= pickle.load(open('./model/model.pkl','rb'))
#random_Forest = pickle.load(MADHYA_MAHARASHTRA,MATATHWADA,VIDARBHA,E_raj,W_Raj,Tam)
#random_Forest=pickle.load(MADHYA_MAHARASHTRA)
print('Model loaded sucessfully')


def result():
    if request.method == "POST":
        myDict = request.form
        Month = int(myDict["Month"])
        Year = int(myDict["Year"])
        pred = [Year, Month]
        res = Tam.predict([pred])[0]
        res = round(res, 2)
        return render_template('result.html', Month=Month, Year=Year, res=res)
    return render_template('index.html')

