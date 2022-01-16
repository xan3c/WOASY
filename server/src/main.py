from sanic import Sanic
from sanic.response import json, text
from sanic_cors import CORS, cross_origin
import scenario_gen
import uuid

games = dict()

app = Sanic("server")
cors = CORS(app, resources={r"/*": {"origins": "http://localhost:3000"}})


@app.get("/scenario")
async def scenario_handler(request):
    data = scenario_gen.generateScenario()
    gameID = uuid.uuid4().hex
    data["gameID"] = gameID

    games[gameID] = data

    return json(data)


@app.post("/finished")
async def finished_handler(request):
    print(request.json)
    return json({"success": True})


app.run(host="0.0.0.0", port=8000, debug=True)
