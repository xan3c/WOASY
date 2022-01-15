from py_avataaars import PyAvataaar
import py_avataaars as pa
import random

avatar = PyAvataaar(style = pa.AvatarStyle.TRANSPARENT, 
                    skin_color = random.choice(list(pa.SkinColor)),
                    hair_color= random.choice(list(pa.HairColor)),
                    facial_hair_type= random.choice(list(pa.FacialHairType)),
                    facial_hair_color= random.choice(list(pa.HairColor)),
                    top_type= random.choice(list(pa.TopType)),
                    hat_color= random.choice(list(pa.Color)),
                    mouth_type= pa.MouthType.SMILE,
                    eye_type= pa.EyesType.DEFAULT,
                    eyebrow_type= random.choice(list(pa.EyebrowType)),
                    nose_type= random.choice(list(pa.NoseType)),
                    accessories_type= random.choice(list(pa.AccessoriesType)),
                    clothe_type= random.choice(list(pa.ClotheType)),
                    clothe_color= random.choice(list(pa.Color)),
                    clothe_graphic_type= random.choice(list(pa.ClotheGraphicType)),
                    
                    )
avatar.render_svg_file('output_file.svg')