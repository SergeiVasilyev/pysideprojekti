import requests

import random

API_OSOITE = "https://opentdb.com/api.php?amount=10&type=multiple&difficulty=easy"

def lataa_kysymys_netista():
    vastaus = requests.get(API_OSOITE)
    tiedot = vastaus.json()
    kysymykset_ja_vastaukset = []
    for juttu in tiedot["results"]:
        kysymys = juttu["question"]
        oikea_vastaus = juttu["correct_answer"]
        vaarat_vastaukset = juttu["incorrect_answers"]
        vastaukset = ["*" + oikea_vastaus] + vaarat_vastaukset
        random.shuffle(vastaukset)
        kysymykset_ja_vastaukset.append([kysymys] + vastaukset)

    import pprint
    pprint.pprint(kysymykset_ja_vastaukset)
    
    return kysymykset_ja_vastaukset

    


# lataa_kysymys_netista()
if __name__ == "__main__":
    import pprint
    pprint.pprint(lataa_kysymys_netista())





