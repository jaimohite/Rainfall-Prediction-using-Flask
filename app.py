from flask import render_template, Flask, request
import pickle

app = Flask(__name__)
State = ' '
file = open("model\model.pkl", "rb")
random_Forest = pickle.load(file)
file.close()

file1 = open("model\MADHYA_MAHARASHTRA_model.pkl", "rb")
random_Forest = pickle.load(file1)
file1.close()

file2 = open("model\MATATHWADA.pkl", "rb")
random_Forest = pickle.load(file2)
file2.close()

file3 = open("model\VIDARBHA.pkl", "rb")
random_Forest = pickle.load(file3)
file3.close()

file4 = open("model\Raj_west_model.pkl", "rb")
random_Forest = pickle.load(file4)
file4.close()

file5 = open("model\Raj_east_model.pkl", "rb")
random_Forest = pickle.load(file5)
file5.close()


@app.route('/')
def home():
    return render_template('Front_ Page.html')
@app.route('/predict/',methods=['GET','POST'])
def predict():
    State = request.form.get('State')
    print(str(State))
    return render_template('index.html')


@app.route("/result", methods=["GET", "POST"])
def result():


    if request.method=='POST':
        myDict = request.form
        Month = int(myDict["Month"])
        Year = int(myDict["Year"])
        pred = [Year, Month]
        res = random_Forest.predict([pred])[0]
        res = round(res, 2)
    return render_template('result.html', Month=Month, Year=Year, res=res)
    #return render_template('index.html')



if __name__ == "__main__":
    app.run(debug=True)