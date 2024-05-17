import pickle
import re # Regular expression
from pathlib import Path

__version__ = "0.1.0" # This assigns the version number "0.1.0" to the __version__ variable

BASE_DIR = Path(__file__).resolve(strict=True).parent

# loads a trained machine learning model
with open(f"{BASE_DIR}/trained_pipeline-{__version__}.pkl", "rb") as f:
    model = pickle.load(f)

# This defines a list called classes, containing the names of different languages or classes that the model can predict
classes = [
    "Arabic",
    "Danish",
    "Dutch",
    "English",
    "French",
    "German",
    "Greek",
    "Hindi",
    "Italian",
    "Kannada",
    "Malayalam",
    "Portugeese",
    "Russian",
    "Spanish",
    "Sweedish",
    "Tamil",
    "Turkish",
]

# prediction function
def predict_pipeline(text):
    text = re.sub(r'[!@#$(),\n"%^*?\:;~`0-9]', " ", text)
    text = re.sub(r"[[]]", " ", text)
    text = text.lower()
    pred = model.predict([text])
    return classes[pred[0]]