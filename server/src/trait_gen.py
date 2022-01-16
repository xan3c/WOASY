from sklearn.preprocessing import OneHotEncoder
import random
import numpy as np

def trait_gen():
    wealth = ['rich']*2 + ['middle-class']*5 + ['poor']*3
    criminal = ['innocent']*8 + ['murderer'] + ['robber']
    mental_state = ['happy', 'depressed']
    origin = ['Canadian', 'American', 'immigrant', 'European']
    parenthood = ['parent', 'non-parent']

    enc = OneHotEncoder(categories=[wealth, criminal, mental_state, origin, parenthood])

    x = [['rich', 'innocent', 'happy', 'Canadian', 'non-parent']]
    enc.fit(x)

    categories = [wealth, criminal, mental_state, origin, parenthood]
    traits = []
    for i in categories:
            traits.append(random.choice(i))

    bio = "Currently, this person is {}".format(traits[2])

    if traits[0] == "rich":
        bio += " and wealthy."
    elif traits[0] == 'poor':
        bio += " and living in poverty."
    else:
        bio += "."

    if traits[1] == "robber":
        bio += " They have a criminal record of bank robbery."
    else:
        bio += " They have a criminal record of commiting murder."

    if traits[3] == 'immigrant':
        bio += ' They are an immigrant'
    else:
        bio += " They are {}".format(traits[3])

    if traits[4] == 'parent':
        bio += " and have kids."
    else:
        bio += " and have no kids."

    result = enc.transform([traits]).toarray()  

    age = random.randint(18, 65)

    return result, traits, bio, age
