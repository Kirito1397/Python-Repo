from flask import Flask, render_template
import random

app = Flask(__name__)

# list of cat images
images = [
   "https://img.freepik.com/free-photo/indian-mountain-skyscape-travel-destination-attractive_53876-31063.jpg?w=740",
   "https://img.freepik.com/free-photo/blue-morning-natural-mountains-bamboo_1417-32.jpg?w=740",
   "https://img.freepik.com/free-photo/alpine-village-alps_53876-130892.jpg?w=826"]

@app.route('/')
def index():
    url = random.choice(images)
    return render_template('index.html', url=url)

if __name__ == "__main__":
    app.run(host="0.0.0.0")