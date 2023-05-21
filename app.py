import replicate
import os
from flask import Flask, jsonify
from flask_cors import CORS

#instantiate app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})

@app.route('/ping', methods=['GET'])
def ping_pong():
    output = replicate.run("salesforce/blip:2e1dddc8621f72155f24cf2e0adbde548458d3cab9f00c0139eea840d0ac4746",
    input={"image": "../my-photo.png",
        "task": "visual_question_answering",
        "question": "What item is this?"})
    os.remove("../my-photo.png")
    return output

if __name__ == '__main__':
    app.run()