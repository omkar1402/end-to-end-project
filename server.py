from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient
import logging
from bson.objectid import ObjectId

app = Flask(__name__)

# Setup logging
logging.basicConfig(level=logging.DEBUG)

# MongoDB connection
try:
    client = MongoClient('mongodb://localhost:27017')
    logging.info("Connected successfully to MongoDB!")
    db = client['ProjectDB']
    collection = db['form1']
except Exception as e:
    logging.error(f"Could not connect to MongoDB: {e}")
    client = None
    collection = None


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/create", methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        country = request.form.get('country')
        gender = request.form.get('gender')
        subscribe = request.form.get('subscribe', 'no')  # Default to 'no' if not checked

        if not all([name, email, country, gender]):
            logging.warning("Incomplete form submission")
            return redirect(url_for('create'))

        document = {
            'name': name,
            'email': email,
            'country': country,
            'gender': gender,
            'subscribe': subscribe
        }
        logging.info(f"Inserting document: {document}")

        if collection is not None:
            try:
                collection.insert_one(document)
                logging.info("Document inserted successfully")
            except Exception as e:
                logging.error(f"Error inserting document: {e}")
        else:
            logging.error("MongoDB connection is not available.")

        return redirect(url_for('create'))

    if collection is not None:
        all_form = collection.find()
    else:
        all_form = []
    return render_template("form.html", form_data=all_form)



@app.route("/get", methods=['GET'])
def fetch_all():
    mongo_data = []
    if collection is not None:
        data = collection.find()
        for document in data:
            logging.info(f"Document: {document}")
            mongo_data.append(document)
        print("Mongo Data:", mongo_data)
        return render_template("get.html", mongo_data=mongo_data)
    else:
        logging.error("MongoDB collection is not available.")
        return "MongoDB collection is not available", 500


@app.route("/delete/<string:_id>", methods=["GET", "POST"])
def delete(_id):
    try:
        # Convert the _id string to an ObjectId
        object_id = ObjectId(_id)
        collection.delete_one({'_id': object_id})
    except Exception as e:
        logging.error(f"Error deleting document: {e}")
        return "Error deleting document", 500
    mongo_data = []
    if collection is not None:
        data = collection.find()
        for document in data:
            logging.info(f"Document: {document}")
            mongo_data.append(document)
        dict_len = len(mongo_data)  # Correctly calculate the total number of documents
        return render_template("get.html", mongo_data=mongo_data, dict_len=dict_len, str=str)
    else:
        logging.error("MongoDB collection is not available.")
        return "MongoDB collection is not available", 500



@app.route("/edit/<string:_id>", methods=['GET', 'POST'])
def edit(_id):
    try:
        # Convert the _id string to an ObjectId
        object_id = ObjectId(_id)
        document = collection.find_one({'_id': object_id})
        if not document:
            logging.error(f"No document found with _id: {_id}")
            return "No document found", 404
    except Exception as e:
        logging.error(f"Error fetching document: {e}")
        return "Error fetching document", 500

    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        country = request.form.get('country')
        gender = request.form.get('gender')
        subscribe = request.form.get('subscribe', 'no')  # Default to 'no' if not checked

        if not all([name, email, country, gender]):
            logging.warning("Incomplete form submission")
            return redirect(url_for('edit', _id=_id))

        update_data = {
            'name': name,
            'email': email,
            'country': country,
            'gender': gender,
            'subscribe': subscribe
        }
        logging.info(f"Updating document with _id: {_id}, data: {update_data}")

        if collection is not None:
            try:
                collection.update_one({'_id': object_id}, {'$set': update_data})
                logging.info("Document updated successfully")
            except Exception as e:
                logging.error(f"Error updating document: {e}")
        else:
            logging.error("MongoDB connection is not available.")

        return redirect(url_for('fetch_all'))

    return render_template("form.html", form_data=document, is_edit=True, _id=_id)


if __name__ == "__main__":
    app.run(debug=True)
