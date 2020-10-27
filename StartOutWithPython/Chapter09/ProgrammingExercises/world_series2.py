def readfile():
    infile = open('WorldSeries.txt','r')
    timeswon = dict()
    teamwon = dict()
    year = 1903
    team = infile.readline()
    dontskip = True
    while team != '':
        team = team.rstrip('\n')
        if team in timeswon:
            timeswon[team] += 1
        elif team.startswith('World'):
            dontskip = False
        else:
            timeswon[team] = 1
        if dontskip:
            teamwon[year] = team
        year += 1
        team = infile.readline()
        dontskip = True
    return teamwon,timeswon
def main():
    teamwon, timeswon = readfile()
    selection = int(input('Choose a year between 1903 and 2009: '))
    while selection == 1904 or selection == 1994:
        print('There was no world cup in',selection)
        selection = int(input('Choose another year:'))
    print(teamwon[selection],'won the World Cup in',selection)
    print('In total they won,',timeswon[teamwon[selection]],'times.')
main()