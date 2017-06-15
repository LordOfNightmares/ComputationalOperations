from math import ceil

# Stations Names
STATIONS = ['eminescu', 'kogalniceanu', 'puskin',
            'casaPresei', 'eminescuTheatre', 'licurici',
            'stefan', 'asem', 'circul',
            'vladimirescu', 'centralTypoghraphy', 'kiev']

# Stations specs
STATIONS_STRUCT = {
    "eminescu": {"capacity": 2370,
                 "trolleybuses": [2, 3, 10, 24]},
    "kogalniceanu": {"capacity": 2370,
                     "trolleybuses": [2, 3, 10, 24]},
    "puskin": {"capacity": 490,
               "trolleybuses": [3]},
    "casaPresei": {"capacity": 1890,
                   "trolleybuses": [2, 10, 24]},
    "eminescuTheatre": {"capacity": 630,
                        "trolleybuses": [2]},
    "stefan": {"capacity": 2240,
               "trolleybuses": [7, 10, 24, 25]},
    "licurici": {"capacity": 980,
                 "trolleybuses": [7, 25]},
    "asem": {"capacity": 2240,
             "trolleybuses": [7, 10, 24, 25]},
    "circul": {"capacity": 2100,
               "trolleybuses": [7, 10, 24, 25]},
    "centralTypoghraphy": {"capacity": 520,
                           "trolleybuses": [25]},
    "vladimirescu": {"capacity": 300,
                     "trolleybuses": [7]},
    "kiev": {"capacity": 1300,
             "trolleybuses": [10, 24]}
}

# Some Important Variables
numTrols = {}
oneTrol = []
optimizedTrols = []

def subtract(array, stationsList):
    for i in array:
        for station_name in stationsList:
            station_specs = STATIONS_STRUCT[station_name]
            if i in station_specs["trolleybuses"]:
                station_specs["capacity"] -= numTrols[i]


for station in STATIONS:
    station_data = STATIONS_STRUCT[station]
    if len(station[1]) <= 2:
        for i in station_data["trolleybuses"]:
            trolNum = station_data["trolleybuses"][0]
            numTrols[i] = ceil(station_data["capacity"] / len(station_data["trolleybuses"]))
            if i not in oneTrol:
                oneTrol.append(i)

subtract(oneTrol, STATIONS)


for station in STATIONS:
    station_data = STATIONS_STRUCT[station]
    if station_data["capacity"] > 0 and len(station_data["trolleybuses"]) == 2:
        result = ceil(station_data["capacity"] / len(station_data["trolleybuses"]))
        for i in station_data["trolleybuses"]:
            if i not in optimizedTrols:
                optimizedTrols.append(i)
                numTrols[i] += result



for troll_num, totalNumber in sorted(numTrols.items()):
    print("Route", troll_num, "needs", ceil(totalNumber / 70), "troleybuses")

