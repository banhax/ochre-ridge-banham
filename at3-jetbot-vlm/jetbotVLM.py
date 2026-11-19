# import requests
from flask import Flask, request
import json
import base64
from pathlib import Path

import ollama

MODEL = "llava:7b"
# PROMPT = "Only answer in 'yes' or 'no', do you see a duck in the included image? The duck can be a fake duck, a real duck, a drawn cartoonish duck, a 3D-printed duck, etc. Anything remotely resembling a duck should yield a 'yes' result."
# PROMPT = "You must ONLY respond with either 'Yes' or 'No'. Answer whether or not there is a duck, or duck-shaped object visible within the image. Any type of duck (real, fake, 3d-printed, drawn, crude drawing) should yield a 'Yes' response, otherwise reply with 'No'. Be very generous with answering 'Yes' to potential ducks, look very closely at the image and ensure you are certain there are no ducks before responding."
PROMPT = "Answer whether or not there is a duck, or duck-shaped object visible within the image. Any type of duck (real, fake, 3d-printed, drawn, crude drawing) is allowed. Be very generous with detecting ducks. Format your response into either 'Yes', or 'No' depending on whether or not there were duck(s) found within the image."

# for path in sorted(Path("at3-jetbot-vlm/sample-frames").glob("*.jpg")):
#     image_b64 = base64.b64encode(path.read_bytes()).decode("utf-8")
#     response = ollama.generate(model=MODEL, prompt=PROMPT, images=[image_b64])
#     print(f"{path.name}: {response['response'].strip()}")

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def res():
    req = request.get_json()
    image = req["image"]
    # image_jpg = base64.b64encode(image)
    response = ollama.generate(model=MODEL, prompt=PROMPT, images=[req["image"]])
    print(response['response'])
    return response['response']

    print("blah")
    #print(request.data)
    print(f"req.data = {request.data}")
    #print(request.json)
    print(f"req.json = {request.json}")
    #print(request.get_json(force=True))