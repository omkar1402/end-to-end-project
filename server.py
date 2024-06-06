from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient
 
app = Flask(__name__)
 

try: 
	conn = MongoClient() 
	print("Connected successfully!!!") 
except: 
	print("Could not connect to MongoDB") 


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/form")
def form():
    return render_template("form.html")

# # Add data to MongoDB route 
# @app.route('/add_data', methods=['POST']) 
# def add_data(): 
# 	try: 
# 		conn = MongoClient() 
# 		print("Connected successfully!!!") 
# 	except: 
# 		print("Could not connect to MongoDB") 

# 	# database 
# 	db = conn.Test 

# 	# Created or Switched to collection names: my_gfg_collection 
# 	collection = db.test_coll 

# 	data=request.json
# 	collection.insert_one(data)
	
	# emp_rec1 = { 
	# 		"name":"Mr.Geek", 
	# 		"eid":24, 
	# 		"location":"delhi"
	# 		} 

	# # Insert Data 
	# rec_id1 = collection.insert_one(emp_rec1) 

	# print("Data inserted with record ids",rec_id1) 

	# # Printing the data inserted 
	# cursor = collection.find() 
	# for record in cursor: 
	# 	print(record) 
	# 	# Get data from request 
	# 	data = request.json 
	
    # # Insert data into MongoDB 
    # collection.insert_one(data) 
	# return 'Data added to MongoDB'
  

client = MongoClient('localhost', 27017)

db = client.flask_db
todos = db.todos

@app.route('/add_data', methods=('GET', 'POST'))
def index():
    if request.method=='POST':
        content = request.form['content']
        degree = request.form['degree']
        todos.insert_one({'content': content, 'degree': degree})
        return redirect(url_for('index'))

    all_todos = todos.find()
    return render_template('add_data.html', todos=all_todos)

if __name__ == "__main__":
    app.run()


# # Python code to illustrate 
# # inserting data in MongoDB 
# # from pymongo import MongoClient 

# # try: 
# # 	conn = MongoClient() 
# # 	print("Connected successfully!!!") 
# # except: 
# # 	print("Could not connect to MongoDB") 

# # database 
# db = conn.Test 

# # Created or Switched to collection names: my_gfg_collection 
# collection = db.test_coll 

# emp_rec1 = { 
# 		"name":"Mr.Geek", 
# 		"eid":24, 
# 		"location":"delhi"
# 		} 
# # emp_rec2 = { 
# # 		"name":"Mr.Omkar", 
# # 		"eid":14, 
# # 		"location":"delhi"
# # 		} 

# # Insert Data 
# rec_id1 = collection.insert_one(emp_rec1) 
# # rec_id2 = collection.insert_one(emp_rec2) 

# print("Data inserted with record ids",rec_id1) 

# # Printing the data inserted 
# cursor = collection.find() 
# for record in cursor: 
# 	print(record) 
