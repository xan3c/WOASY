import random
from sklearn.preprocessing import OneHotEncoder


def avatar_gen():

    skin = ["tanned", "yellow", "pale", "light", "brown", "darkBrown", "black"]
    # skin = ["tanned"]

    hairColor = [
        "auburn",
        "black",
        "blonde",
        "blondeGolden",
        "brown",
        "brownDark",
        "pastel",
        "pastelPink",
        "platinum",
        "red",
        "gray",
        "silverGray",
    ]

    facialHair = [
        "medium",
        "beardMedium",
        "light",
        "beardLight",
        "majestic",
        "beardMajestic",
        "fancy",
        "moustaceFancy",
        "magnum",
        "moustacheMagnum",
    ]

    facialHairColor = [
        "auburn",
        "black",
        "blonde",
        "blondeGolden",
        "brown",
        "brownDark",
        "pastel",
        "pastelPink",
        "platinum",
        "red",
        "gray",
        "silverGray",
    ]

    top = [
        "longHair",
        "shortHair",
        "eyepatch",
        "hat",
        "hijab",
        "turban",
        "bigHair",
        "bob",
        "bun",
        "curly",
        "curvy",
        "dreads",
        "frida",
        "fro",
        "froAndBand",
        "miaWallace",
        "longButNotTooLong",
        "shavedSides",
        "straight01",
        "straight02",
        "straightAndStrand",
        "dreads01",
        "dreads02",
        "frizzle",
        "shaggy",
        "shaggyMullet",
        "shortCurly",
        "shortFlat",
        "shortRound",
        "shortWaved",
        "sides",
        "theCaesar",
        "theCaesarAndSidePart",
        "winterHat01",
        "winterHat02",
        "winterHat03",
        "winterHat04",
    ]

    hatColor = [
        "black",
        "blue",
        "blue01",
        "blue02",
        "blue03",
        "gray",
        "gray01",
        "gray02",
        "heather",
        "pastel",
        "pastelBlue",
        "pastelGreen",
        "pastelOrange",
        "pastelRed",
        "pastelYellow",
        "pink",
        "red",
        "white",
    ]

    mouth = [
        "concerned",
        "default",
        "disbelief",
        "eating",
        "grimace",
        "sad",
        "scream",
        "screamOpen",
        "serious",
        "smile",
        "tongue",
        "twinkle",
        "vomit",
    ]

    eyes = [
        "close",
        "closed",
        "cry",
        "default",
        "dizzy",
        "xDizzy",
        "roll",
        "eyeRoll",
        "happy",
        "hearts",
        "side",
        "squint",
        "surprised",
        "wink",
        "winkWacky",
    ]

    eyebrow = [
        "angry",
        "angryNatural",
        "default",
        "defaultNatural",
        "flat",
        "flatNatural",
        "raised",
        "raisedExcited",
        "raisedExcitedNatural",
        "sad",
        "sadConcerned",
        "sadConcernedNatural",
        "unibrow",
        "unibrowNatural",
        "up",
        "upDown",
        "upDownNatural",
        "frown",
        "frownNatural",
    ]

    accessories = ["kurt", "prescription01", "prescription02", "round", "sunglasses", "wayfarers"]

    accessoriesColor = [
        "black",
        "blue",
        "blue01",
        "blue02",
        "blue03",
        "gray",
        "gray01",
        "gray02",
        "heather",
        "pastel",
        "pastelBlue",
        "pastelGreen",
        "pastelOrange",
        "pastelRed",
        "pastelYellow",
        "pink",
        "red",
        "white",
    ]

    clothe = [
        "blazer",
        "blazerAndShirt",
        "blazerAndSweater",
        "sweater",
        "collarAndSweater",
        "shirt",
        "graphicShirt",
        "shirtCrewNeck",
        "shirtScoopNeck",
        "shirtVNeck",
        "hoodie",
        "overall",
    ]

    clothesColor = [
        "black",
        "blue",
        "blue01",
        "blue02",
        "blue03",
        "gray",
        "gray01",
        "gray02",
        "heather",
        "pastel",
        "pastelBlue",
        "pastelGreen",
        "pastelOrange",
        "pastelRed",
        "pastelYellow",
        "pink",
        "red",
        "white",
    ]

    clotheGraphics = ["skullOutline", "skull", "resist", "pizza", "hola", "diamond", "deer", "cumbia", "bear", "bat"]

    facialHairChance = 0.5
    accessoriesChance = 0.5
    topChance = 0.5

    enc = OneHotEncoder(
        categories=[
            skin,
            hairColor,
            facialHair,
            facialHairColor,
            top,
            hatColor,
            mouth,
            eyes,
            eyebrow,
            accessories,
            accessoriesColor,
            clothe,
            clothesColor,
            clotheGraphics,
        ]
    )

    enc.fit(
        [
            [
                "tanned",
                "auburn",
                "medium",
                "auburn",
                "longHair",
                "black",
                "concerned",
                "close",
                "angry",
                "kurt",
                "black",
                "blazer",
                "black",
                "bat",
            ]
        ]
    )

    categories = [
        skin,
        hairColor,
        facialHair,
        facialHairColor,
        top,
        hatColor,
        mouth,
        eyes,
        eyebrow,
        accessories,
        accessoriesColor,
        clothe,
        clothesColor,
        clotheGraphics,
    ]
    category_names = [
        "skin",
        "hairColor",
        "facialHair",
        "facialHairColor",
        "top",
        "hatColor",
        "mouth",
        "eyes",
        "eyebrow",
        "accessories",
        "accessoriesColor",
        "clothe",
        "clothesColor",
        "clotheGraphics",
    ]

    traits = []
    dictionary = {}

    for i in range(len(categories)):

        choices = categories[i]
        decision = random.choice(choices)
        traits.append(decision)
        dictionary.update({category_names[i]: decision})

    result = enc.transform([traits]).toarray()

    return result, traits, dictionary
