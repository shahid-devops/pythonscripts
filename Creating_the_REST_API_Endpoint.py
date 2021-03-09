#!/usr/bin/python
#main.py

#Import the Flask module that has been installed
from flask import Flask, jsonify

#Creating a "books" JSON / dict to emulate data coming from a database

books = [
	{
		"id": 1,
		"title": "Wings of fire",
		"Author": "APJ abdul kalam sir",
		"isbn": "12345678"
	},

	{

		"id": 1,
		"title": ";Bio of apj abdul kalam",
		"Author": "APJ abdul kalam sir",
		"isbn": "12345678"
	}

]
# Creating a new "app" by using the Flask constructor. Passes __name__ as a parameter.
app = Flask(__name__)

#Annotation that allows the function to be hit at the specific URL.
@app.route("/")

#Generic Python function that returns simple message
def index():
  return "Simple API project"
# Annotation that allows the function to be hit at the specific URL. Ind
@app.route("/test/api/works/great/library", methods=["GET"])

#Function that will run when the endpoint is hit

def retrieve_books():
  return jsonify({"bookjson": books})


if __name__=="__main__":
  app.run()


