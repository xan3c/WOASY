from py_avataaars import PyAvataaar
import py_avataaars as pa
import random
from sklearn.preprocessing import OneHotEncoder

def avatar_gen():

  style = [name for name in dir(pa.AvatarStyle) if not name.startswith('_')]
  skin_color = [name for name in dir(pa.SkinColor) if not name.startswith('_')]
  hair_color= [name for name in dir(pa.HairColor) if not name.startswith('_')]
  facial_hair_type= [name for name in dir(pa.FacialHairType) if not name.startswith('_')]
  facial_hair_color= [name for name in dir(pa.HairColor) if not name.startswith('_')]
  top_type= [name for name in dir(pa.TopType) if not name.startswith('_')]
  hat_color= [name for name in dir(pa.Color) if not name.startswith('_')]
  mouth_type= [name for name in dir(pa.MouthType) if not name.startswith('_')]
  eye_type= [name for name in dir(pa.EyesType) if not name.startswith('_')]
  eyebrow_type= [name for name in dir(pa.EyebrowType) if not name.startswith('_')]
  nose_type= [name for name in dir(pa.NoseType) if not name.startswith('_')]
  accessories_type= [name for name in dir(pa.AccessoriesType) if not name.startswith('_')]
  clothe_type= [name for name in dir(pa.ClotheType) if not name.startswith('_')]
  clothe_color= [name for name in dir(pa.Color) if not name.startswith('_')]
  clothe_graphic_type= [name for name in dir(pa.ClotheGraphicType) if not name.startswith('_')]

  enc = OneHotEncoder(categories=[style, skin_color, hair_color, facial_hair_type, facial_hair_color,
                                  top_type, hat_color, mouth_type,
                                  eye_type, eyebrow_type, nose_type,
                                  accessories_type, clothe_type,
                                  clothe_color, clothe_graphic_type])

  enc.fit([['TRANSPARENT', 'LIGHT', 'BROWN', 'DEFAULT', 'BLACK', 'SHORT_HAIR_SHORT_FLAT', 'BLACK', 'SMILE', 'DEFAULT', 'DEFAULT', 'DEFAULT', 'DEFAULT', 'GRAPHIC_SHIRT', 'HEATHER','BAT']])


  categories=[
                                  style, skin_color, hair_color,
                                  facial_hair_type, facial_hair_color,
                                  top_type, hat_color, mouth_type,
                                  eye_type, eyebrow_type, nose_type,
                                  accessories_type, clothe_type,
                                  clothe_color, clothe_graphic_type
              ]

  traits = ['TRANSPARENT']

  for i in categories: 
    if i is not style and i is not eye_type:
      traits.append(random.choice(i))
    elif i is eye_type:
      traits.append('DEFAULT')

  result = enc.transform([traits]).toarray()  

  return result, traits

result_array = avatar_gen()[0]
result = avatar_gen()[1]

avatar = PyAvataaar(style = pa.AvatarStyle[result[0]],
                    skin_color = pa.SkinColor[result[1]],
                    hair_color= pa.HairColor[result[2]],
                    facial_hair_type= pa.FacialHairType[result[3]],
                    facial_hair_color= pa.HairColor[result[4]],
                    top_type= pa.TopType[result[5]],
                    hat_color= pa.Color[result[6]],
                    mouth_type= pa.MouthType[result[7]],
                    eye_type= pa.EyesType[result[8]],
                    eyebrow_type= pa.EyebrowType[result[9]],
                    nose_type= pa.NoseType[result[10]],
                    accessories_type= pa.AccessoriesType[result[11]],
                    clothe_type= pa.ClotheType[result[12]],
                    clothe_color= pa.Color[result[13]],
                    clothe_graphic_type= pa.ClotheGraphicType[result[14]],
                    
                    )

avatar.render_svg_file('output_file.svg')
