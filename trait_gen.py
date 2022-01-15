from sklearn.preprocessing import OneHotEncoder
import random

wealth = ['rich', 'poor']
criminal = ['innocent', 'murderer', 'robber']
mental_state = ['happy', 'depressed']
origin = ['canadian', 'american', 'immigrant', 'european']
parenthood = ['parent', 'non-parent']

enc = OneHotEncoder(categories=[wealth, criminal, mental_state, origin, parenthood])

x = [['rich', 'innocent', 'happy', 'canadian', 'parent']]
enc.fit(x)

def trait_gen(enc, *args):
  traits = []
  for i in args:
    traits.append(random.choice(i))

  result = enc.transform([traits]).toarray()  
  return result

trait_gen(enc, wealth, criminal, mental_state, origin, parenthood)