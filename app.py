from flask import Flask
app = Flask(__name__)
@app.route("/")
def hello():
return "Hello from UTA CI/CD Lab!"
