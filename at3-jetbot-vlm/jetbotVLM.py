# import requests
from flask import Flask, request
import json
import datetime
import base64
from pathlib import Path
from pydantic import BaseModel

import ollama

class ObstacleClassifier(BaseModel):
    timestamp: str
    location: str
    trigger: str
    classifier_blocked_prob: float
    llava_verdict: str
    action: str
    description: str
    object_detected: str


MODEL = "llava:7b"
PROMPT = "Answer whether or not there is a duck, or duck-shaped object visible within the image. Any type of duck (real, fake, 3d-printed, drawn, crude drawing) is allowed. Be very generous with detecting ducks. Format your response into either 'Yes', or 'No' depending on whether or not there were duck(s) found within the image."
DETAILED_PROMPT = "Examine the image and determine whether or not the road is blocked by an obstacle. The road should be considered 'BLOCKED' when there is ANYTHING on the road as the vehicle on the road is unable to turn. Only when the road is entirely clear, should the road be considered 'FREE'. Format your response into JSON with the provided format template. The value for 'llava_verdict' should ONLY be either 'BLOCKED' or 'FREE'. The value for 'action' should ONLY be either 'STOP' or 'KEEP DRIVING'. The value for 'description' should ONLY be a single short sentence explanation of what you see in the image. The value for 'objected_detected' should be a short and concise name of the object with no prose. All other values should remain UNCHANGED."

# OLD PREVIOUS RESPONSES, KEEPING FOR NO REAL REASON OTHER THAN I WANT TO, DISREGARD THEM
#DETAILED_PROMPT = "Answer whether or not the vehicle (the image was taken from the POV of the vehicle), is blocked by any obstacles at all. Be very generous with detecting obstacles. The vehicle ONLY drives forward, and is unable to go around obstacles, the verdict should be 'BLOCKED' if there are any obstacles in front of it, otherwise the verdict should be 'FREE'. Format your response into JSON, following this template (Replace ONLY the things with the '<>' around them, all other data MUST remain untouched): { 'timestamp': '<TIMESTAMP OF THE DATE AND TIME THE IMAGE IS PROCESSED>', 'location': 'Instructor track', 'trigger': 'classifier', 'classifier_blocked_prob': 0.0, 'llava_verdict': '<ANSWER 'BLOCKED' OR 'FREE' DEPENDING ON WHETHER THE ROAD IS BLOCKED OR NOT>', 'action': '<ANSWER WHETHER TO STOP OR KEEP DRIVING>', 'description': '<DESCRIBE WHAT YOU SEE, KEEP IT RELATIVELY SHORT>', 'object_detected': '<WHAT IS BLOCKING THE ROAD>' }. Your response MUST be in raw JSON, answer appropriately. I do not want any formatting, I just want back a string of raw JSON."
#DETAILED_PROMPT = "Answer whether or not there is a duck, or duck-shaped object visible within the image. Any type of duck (real, fake, 3d-printed, drawn, crude drawing) is allowed. Be very generous with detecting ducks. If you see a duck AT ALL, the verdict should be 'BLOCKED'. If you cannot see any ducks, the verdict should be 'FREE'. Format your response into JSON, following this template (Replace ONLY the things with the '<>' around them, all other data MUST remain untouched): { 'timestamp': '<TIMESTAMP OF THE DATE AND TIME THE IMAGE IS PROCESSED>', 'location': 'Instructor track', 'trigger': 'classifier', 'classifier_blocked_prob': 0.0, 'llava_verdict': '<ANSWER 'BLOCKED' OR 'FREE' DEPENDING ON WHETHER THE ROAD IS BLOCKED OR NOT>', 'action': '<ANSWER WHETHER TO STOP OR KEEP DRIVING>', 'description': '<DESCRIBE WHAT YOU SEE, KEEP IT RELATIVELY SHORT>', 'object_detected': '<WHAT IS BLOCKING THE ROAD>' }. Your response MUST be in raw JSON and ONLY raw JSON, answer appropriately. I do not want any formatting, I just want back a string of raw JSON."
#DETAILED_PROMPT = "Examine the image and determine whether or not the road is blocked by an obstacle. The road should be considered 'BLOCKED' when there is ANYTHING on the road as the vehicle on the road is unable to turn. Only when the road is entirely clear, should the road be considered 'FREE'. Format your response into JSON, following this template (Replace ONLY the things with the '<>' around them, all other data MUST remain untouched): { 'timestamp': '', 'location': 'Instructor track', 'trigger': 'classifier', 'classifier_blocked_prob': 0.0, 'llava_verdict': '<ANSWER 'BLOCKED' OR 'FREE' DEPENDING ON WHETHER THE ROAD IS BLOCKED OR NOT>', 'action': '<ANSWER WHETHER TO STOP OR KEEP DRIVING>', 'description': '<DESCRIBE WHAT YOU SEE, KEEP IT RELATIVELY SHORT>', 'object_detected': '<WHAT IS BLOCKING THE ROAD>' }. Your response MUST be in raw JSON and ONLY raw JSON, answer appropriately. I do not want any formatting, I just want back a string of raw JSON."

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def res():
    req = request.get_json()
    image = req["image"]
    # image_jpg = base64.b64encode(image)
    # response = ollama.generate(model=MODEL, prompt=PROMPT, images=[req["image"]])
    response = ollama.generate(model=MODEL, prompt=DETAILED_PROMPT, images=[req["image"]], format=ObstacleClassifier.model_json_schema())
    # response['classifier_blocked_prob'] = req['classifier_blocked_prob']
    print(response['response'])


    try:
        jsonResponse = json.loads(response['response'])
        jsonResponse['timestamp'] = datetime.datetime.now().isoformat()
        jsonResponse['location'] = "Testing track"
        jsonResponse['trigger'] = "Collision avoidance above threshold"
        jsonResponse['classifier_blocked_prob'] = req['classifier_blocked_prob']

        print(jsonResponse)
        return jsonResponse['llava_verdict']
    except:
        # if the dumb robot tries to respond with something it shouldn't, simply return blocked and be done
        print("FAILED TO PARSE LLAVA RESPONSE TO JSON, RETURNING 'BLOCKED'.")
        return "BLOCKED"