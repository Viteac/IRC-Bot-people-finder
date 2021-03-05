import json


f = open('d.json')
people = json.load(f)
f.close()


f = open('f.json')
free = json.load(f)
f.close()

for x in people:
    for y in free:
        if people[x]['IP'] == free[y]['IP'] or people[x]['Hostname'] == free[y]['Hostname'] or people[x]['Realname']==free[y]['Realname']:
            print(f'{people[x]}\n{free[y]}\n -------------------------------------------')
