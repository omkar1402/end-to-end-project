from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient
import logging

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

@app.route("/form", methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        country = request.form.get('country')
        gender = request.form.get('gender')
        subscribe = request.form.get('subscribe', 'no')  # Default to 'no' if not checked

        if not all([name, email, country, gender]):
            logging.warning("Incomplete form submission")
            return redirect(url_for('form'))

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

        return redirect(url_for('form'))

    if collection is not None:
        all_form = collection.find()
    else:
        all_form = []
    return render_template("form.html", form_data=all_form)



@app.route("/get", methods=['GET'])
def fetch_all():
    mongo_data, dict_len = list(), list()
    if collection is not None:
        data = collection.find()
        for document in data:
            logging.info(f"Document: {document}")
            mongo_data.append(document)
            dict_len.append(len(document))
        print(mongo_data)
        return render_template("get.html", mongo_data=mongo_data, dict_len=max(dict_len))
    else:
        logging.error("MongoDB collection is not available.")

if __name__ == "__main__":
    app.run(debug=True)
