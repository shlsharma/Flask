from flask import Flask, request, render_template

app = Flask(__name__) #__name__ where to look for resources 

@app.route("/") # path for the below function of activity in the page
def hello_world():
    return "<h1>Welcome to Flask Application!</h1>"

@app.route("/welcome") # path for the below function of activity in the page
def Welcome():
    return "<h2>Welcome Navigation</h2>"

@app.route("/welcome/<user>") # path for the below function of activity in the page
def Welcome_user(user):
    return f"<h2>Welcome {user} to Flask Application</h2>"

@app.route('/square', methods=['GET'])
def squarenumber():
    if request.method == 'GET':
        if (request.args.get('num') == None): # when user request first time, it will be none
            return render_template('square.html')
        elif (request.args.get('num') == ''):
            return "<html><body> <h1> Invalid Input </h1></body></html>"
        else:
            number = request.args.get('num')
            square = int(number)*int(number)
            return render_template('solution.html', squareofnum=square, num=number)

if __name__ == '__main__':
    app.run()