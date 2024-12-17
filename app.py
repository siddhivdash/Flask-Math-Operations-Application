from flask import Flask,render_template, request,jsonify
#Here we will keep the core business logic
app = Flask(__name__)
# We will do the operations like add,substraction,division,multiplication
# We will learn how we can integrate how to add functionality to the given HTML CSS file.
@app.route('/' , methods = ['GET' , 'POST'])
def home_page():
    return render_template('index.html') #will render the main HTML page

# WHAT DO WE WANT? Basically whenever we put values in the box and 
# click on calculate,it will send information to the server and give us the value
# As a learner of Flask we will not write the HTML CSS code
 #<form action="/math" method="POST"> this will use the post method(from index.html)
 #GET - Through URL, POST -Through Body
@app.route('/math', methods = ['POST']) #whenever we click on calculate button,whatever functions is there in /math it will execute that
def math_operation1():
    if(request.method == 'POST'):
        ops = request.form['operation'] #Whatever the operation we want to perform will get stored in ops
        num1 = int(request.form['num1']) #<input type="text" name="num1" id="num1"> we are getting it in text form so we will convert it into integer
        num2 = int(request.form['num2']) #<input type="text" name="num2" id="num2">
        if(ops == 'add'):
            r = num1 + num2
            result = 'the sum of  ' + str(num1) + ' and  ' +str(num2) + "  is " +str(r)
        
        if(ops == 'subtract'):
            r = num1 - num2
            result = 'the substraction of  ' + str(num1) + ' and  ' +str(num2) + "  is " +str(r)

        if(ops == 'multiply'):
            r = num1 * num2
            result = 'the multiplication of  ' + str(num1) + ' and  ' +str(num2) + "  is " +str(r)
        
        if(ops == 'divide'):
            r = num1/num2
            result = 'the division of  ' + str(num1) + ' and  ' +str(num2) + "  is " +str(r)
    
        if(ops == 'log'):
            r = num1 % num2
            result = 'the log of  ' + str(num1) + ' and  ' +str(num2) + "  is " +str(r)
        
        return render_template('results.html' ,result = result ) #{{result}} This is a placeholder which keeps the data
if __name__=="__main__":
    app.run(host = "0.0.0.0")



#If we want to pass the data through /postman then in place of form we will use json
#@app.route('/postman_data', methods = ['POST']),use the postman software
#num1 = json(request.form['num1'])
#In-sort, passing the data through distionary file
#return jsonify(result)
#POSTMAN tool used for api testing
