from sanic import Sanic
from sanic.response import json, text
from sanic_cors import CORS, cross_origin

# import scenario_gen
import json as j

app = Sanic("server")
cors = CORS(app, resources={r"/*": {"origins": "http://localhost:3000"}})


@app.get("/scenario")
async def scenario_handler(request):
    # data = scenario_gen.generateScenario()
    with open("test.json") as file:
        data = j.load(file)
        return json(data)


app.run(host="0.0.0.0", port=8000, debug=True)
