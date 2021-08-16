import schedule
import json


with open('data.json', 'r') as openfile:
    # Reading from json file
    annees = json.load(openfile)
    

def plannification(annee='2021',moi='',jour='',heure='',minute='',action=1):
    annees[annee][moi][jour][heure][minute] = action
    with open('data.json', 'w') as outfile:
        json.dump(annees, outfile)

def une_minute_tache():
    a = schedule.datetime.datetime.now()
    print(annees[str(a.year)][str(a.month)][str(a.day)][str(a.hour)][str(a.minute)])

plannification(annee='2021',moi='8',jour='9',heure='12',minute='19')

schedule.every(1).minutes.do(une_minute_tache)

while True:
    schedule.run_pending()
