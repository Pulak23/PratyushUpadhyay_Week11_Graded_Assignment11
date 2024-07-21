from flask import Flask
import joblib


# Initialize App
app = Flask(__name__)

# Load models
model = joblib.load(r"model/model_binary.dat.gz")
