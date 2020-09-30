
from flask import Flask, render_template, request


app = Flask(__name__)

@app.route("/")
def main():
    return render_template('index.html')

@app.route("/result", methods=['POST', 'GET'])
def result():
   if request.method == 'POST':
       query = request.form['query']
       query = int(query)
       searchFib(query)
       response = searchFib(query)
       return render_template("index.html", value=response)

def searchFib(n):
    a=b=1
    while 2*n>a+b:a,b=b,a+b
    return a

if __name__ == "__main__":
    app.run()