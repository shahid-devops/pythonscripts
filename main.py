#main.py

#Import the Flask module that has been installed.
from flask import Flask
import flask
import os

#Creating a new "app" by using the Flask constructor. Passes __name__ as a paramter.
app = Flask(__name__)

#Annotation that allows the function to be hit at the specific URL.
@app.route("/")

#Generic Python Function that returns
def index():
  return "This is the simple API creation"

'''
#Checks to see if the name of the package is the run as the main package.
if __name__ == "__main__":
	 # Runs the Flask application only if the main.py file is being run.
  app.run()
'''
print (dir(os.path))