from flask import Flask, render_template, request, redirect
app = Flask(__name__)  

@app.route('/')         
def index():
    return render_template("index.html")

@app.route('/checkout', methods=['POST'])         
def checkout():
    import datetime
    print(request.form)
    sberry = request.form['strawberry']
    bberry = request.form['blackberry']
    rberry = request.form['raspberry']
    afruit = request.form['apple']
    fname = request.form['first_name']
    lname = request.form['last_name']
    sID = request.form['student_id']
    count= int(sberry) + int(bberry) + int(rberry) + int(afruit)
    date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return render_template("checkout.html", strawberry=sberry, blackberry=bberry, raspberry=rberry, apple=afruit, firstName=fname, lastName=lname, studentID=sID, count=count, date=date)

@app.route('/fruits')         
def fruits():
    return render_template("fruits.html")

if __name__=="__main__":   
    app.run(debug=True)    