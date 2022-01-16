import random
import trait_gen
import json
import avatar_gen
import uuid


def generateCharacter():
    _, _, bio, age = trait_gen.trait_gen()
    x = random.randint(0, 700)
    y = random.randint(0, 700)

    _, _, features = avatar_gen.avatar_gen()
    person = {
        "x": x + 50,
        "y": y + 50,
        "age": age,
        "bio": bio,
        "options": features,
    }

    return person


def generateScenario():
    n_people = random.randint(7, 10)
    n_spots = 5

    characters_list = []

    for i in range(n_people):
        c = generateCharacter()
        c["id"] = uuid.uuid4().hex
        characters_list.append(c)

    life_boat_pos_x = 400  # random.randint(0, 800)
    life_boat_pos_y = 780  # random.randint(0, 800)

    # in seconds
    Time = 10

    scenario = {
        "characters": characters_list,
        "lifeboat": {
            "x": life_boat_pos_x,
            "y": life_boat_pos_y,
            "maxCapacity": 5,
        },
        "maxTime": Time,
    }

    return scenario


if __name__ == "__main__":
    json_object = json.dumps(generateScenario(), indent=4)
    print(json_object)
