# from flask import Flask, render_template, request
# from pymongo import MongoClient
 
# app = Flask(__name__)
 
# client = MongoClient('mongodb://localhost:27017/')
# db = client['TestDB']
# collection = db['Test-Collection']


# @app.route("/")
# def home():
#     return render_template("index.html")

# @app.route("/form")
# def form():
#     return render_template("form.html")

# # Add data to MongoDB route 
# @app.route('/add_data', methods=['POST']) 
# def add_data(): 
#     # Get data from request 
#     data = request.json 
  
#     # Insert data into MongoDB 
#     collection.insert_one(data) 
  
#     return 'Data added to MongoDB'
  
# if __name__ == "__main__":
#     app.run()



from flask import Flask, request 
from pymongo import MongoClient 

app = Flask(__name__) 

# root route 
@app.route('/') 
def hello_world(): 
	return 'Hello, World!'

# Set up MongoDB connection and collection 
client = MongoClient('mongodb://localhost:27017/') 

# Create database named demo if they don't exist already 
db = client['demo'] 

# Create collection named data if it doesn't exist already 
collection = db['data'] 

# Add data to MongoDB route 
@app.route('/add_data', methods=['POST']) 
def add_data(): 
	# Get data from request 
	data = request.json 

	# Insert data into MongoDB 
	collection.insert_one(data) 

	return 'Data added to MongoDB'


if __name__ == '__main__': 
	app.run() 
