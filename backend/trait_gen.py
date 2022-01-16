from sklearn.preprocessing import OneHotEncoder
import random

def trait_gen():
    wealth = ['rich', 'poor']
    criminal = ['innocent', 'murderer', 'robber']
    mental_state = ['happy', 'depressed']
    origin = ['Canadian', 'American', 'immigrant', 'European']
    parenthood = ['parent', 'non-parent']

    enc = OneHotEncoder(categories=[wealth, criminal, mental_state, origin, parenthood])

    x = [['rich', 'innocent', 'happy', 'canadian', 'non-parent']]
    enc.fit(x)

    categories = [wealth, criminal, mental_state, origin, parenthood]
    traits = []
    for i in categories:
        traits.append(random.choice(i))

    bio = "Currently, this person is {} and {}.".format(traits[0], traits[2]) 
    if traits[1] == 'innocent':
        bio += " They have a clean criminal record"
    elif traits[1] == "robber":
        bio += " They have a criminal record of bank robbery"
    else:
        bio += " They have a criminal record of commiting murder"

    if traits[3] == 'immigrant':
        bio += ', is an immigrant'
    else:
        bio += ", is {}".format(traits[3])

    if traits[4] == 'parent':
        bio += ", and has kids."
    else:
        bio += ", and has no kids."

    result = enc.transform([traits]).toarray()  

    age = random.randint(18, 65)

    return result, traits, bio, age
