import ujson
from sanic import Sanic
from sanic.response import json, text
from sanic_cors import CORS, cross_origin


app = Sanic("server")
cors = CORS(app, resources={r"/*": {"origins": "http://localhost:3000"}})


@app.get("/scenario")
async def scenario_handler(request):
    data = None
    with open("test.json") as file:
        data = ujson.load(file)
    return json(data)


app.run(host="0.0.0.0", port=8000, debug=True)
