import random
import trait_gen
import json
import avatar_gen
import uuid
import numpy as np 

def generateCharacter():
    one_hot_trait, _, bio, age = trait_gen.trait_gen()
    x = random.randint(0, 700)
    y = random.randint(0, 700)

    one_hot_avatar, _, features = avatar_gen.avatar_gen()
    person = {
        "x": x + 50,
        "y": y + 50,
        "age": age,
        "bio": bio,
        "options": features
    }

    one_hot = np.concatenate((one_hot_trait, one_hot_avatar), axis=1)

    return person, one_hot


def generateScenario():
    n_people = random.randint(7, 10)
    n_spots = 5

    characters_list = []
    one_hot_list = {}

    for i in range(n_people):
        c, one_hot = generateCharacter()
        hex_id = uuid.uuid4().hex
        c["id"] = hex_id
        characters_list.append(c)
        one_hot_list[hex_id] = one_hot

    life_boat_pos_x = 400  # random.randint(0, 800)
    life_boat_pos_y = 780  # random.randint(0, 800)

    # in seconds
    Time = int(n_people*3)

    scenario = {
        "characters": characters_list,
        "lifeboat": {
            "x": life_boat_pos_x,
            "y": life_boat_pos_y,
            "maxCapacity": 5,
        },
        "maxTime": Time,
    }

    print(one_hot_list)
    return scenario, one_hot_list


if __name__ == "__main__":
    scene = generateScenario()
    avatar = scene[0]
    one_hot_encoding = scene[1]
    json_object = json.dumps(avatar, indent=4)
    print(json_object)
