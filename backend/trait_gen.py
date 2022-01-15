from sklearn.preprocessing import OneHotEncoder
import random

def trait_gen():
  wealth = ['rich', 'poor']
  criminal = ['innocent', 'murderer', 'robber']
  mental_state = ['happy', 'depressed']
  origin = ['canadian', 'american', 'immigrant', 'european']
  parenthood = ['parent', 'non-parent']

  enc = OneHotEncoder(categories=[wealth, criminal, mental_state, origin, parenthood])

  x = [['rich', 'innocent', 'happy', 'canadian', 'parent']]
  enc.fit(x)



  categories = [wealth, criminal, mental_state, origin, parenthood]
  traits = []
  for i in categories:
    traits.append(random.choice(i))

  result = enc.transform([traits]).toarray()  

  return result, traits, enc
