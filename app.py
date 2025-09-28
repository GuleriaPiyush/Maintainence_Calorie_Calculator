from flask import Flask, request,render_template

app=Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')






@app.route('/calorie_calculator', methods=['GET','POST'])
def calculateBmr():
    gender = request.form['gender']
    age = float(request.form['age'])
    weight = float(request.form['weight'])
    height = float(request.form['height'])
    w_unit = request.form['w_unit']

    if w_unit=='Lb':
        weight=weight*2.2
    else:
        weight=weight*1



    if gender.lower()=='m':
        bmr = 10 * weight + 6.25 * height - 5 * age + 5

    elif gender.lower()=='f':
        bmr = 10 * weight + 6.25 * height - 5 * age - 161

    else:
        raise ValueError('Gender must be m or f ')
    
    return render_template("index.html",result=bmr)
    
    

if __name__ == "__main__":
    app.run(debug=True)



