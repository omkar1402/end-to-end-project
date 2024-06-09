from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient
import logging

app = Flask(__name__)

# Setup logging
logging.basicConfig(level=logging.DEBUG)

# MongoDB connection
try:
    client = MongoClient('localhost', 27017)
    logging.info("Connected successfully to MongoDB!")
except Exception as e:
    logging.error(f"Could not connect to MongoDB: {e}")

# Access the database and collection
db = client['ProjectDB']
form_data = db['form1']

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

        try:
            form_data.insert_one(document)
            logging.info("Document inserted successfully")
        except Exception as e:
            logging.error(f"Error inserting document: {e}")

        return redirect(url_for('form'))

    all_form = form_data.find()
    return render_template("form.html", form_data=all_form)

@app.route('/submit', methods=['POST'])
def submit():
    return render_template("submit.html")

if __name__ == "__main__":
    app.run(debug=True)
