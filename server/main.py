from sanic import Sanic
from sanic.response import json, text
from sanic_cors import CORS, cross_origin
from src import scenario_gen
import uuid

games = dict()
dataset = dict()

app = Sanic("server")
cors = CORS(app, resources={r"/*": {"origins": "http://localhost:3000"}})


@app.get("/scenario")
async def scenario_handler(request):
    data, one_hot_encodings = scenario_gen.generateScenario()
    gameID = uuid.uuid4().hex
    data["gameID"] = gameID

    for key, values in one_hot_encodings.items():
        dataset[key] = [values, False]  # [one_hot encodings, Saved or not]

    print(dataset)
    games[gameID] = data

    return json(data)


@app.post("/finished")
async def finished_handler(request):
    response = request.json
    for player_id in response["saved"]:
        dataset[player_id] = [dataset[player_id], True]
    return json({"success": True})


app.run(host="0.0.0.0", port=8080, debug=True)
