#!/usr/bin/python
# coding: utf8

import sys
from datetime import timedelta

from BoR_utils import BoR_Time
from BoR_request import BoR_Report_By_Fixture,BoR_Team_Name

relevant = ['name', 'csr', 'age', 'weight', 'height', 'form', 'energy', 
            'aggression', 'discipline', 'leadership', 'experience', 'stamina',
            'handling', 'attack', 'defense', 'technique', 'strength', 'jumping',
            'speed', 'agility', 'kicking', 'pops']

#print ';'.join(relevant)
players = {}

if __name__ == '__main__':
    if len (sys.argv) != 2:
        print "You have to give the fixture ID"
        exit (1)
    Fixture_ID = sys.argv [1]
    data = BoR_Report_By_Fixture (Fixture_ID)
    print data
    BoR_time = BoR_Time (data['brt'])
    fixture = data['fixtures'][Fixture_ID]
    #fixture_time_start = BoR_Time (fixture['matchstart'])
    #home_team_id = fixture['hometeamid']
    #guest_team_id = fixture['guestteamid']
    #print "{} - {}".format (home_team_id, BoR_Team_Name (home_team_id))
    #print "{} - {}".format (guest_team_id, BoR_Team_Name (guest_team_id))
    #for player in data['players']:
        #infos = data['players'][player]
        #Pid = int(infos['id'])
        #stats = [infos[x] for x in relevant]
        #stats_unicode = [x.encode('ascii', 'ignore') if type(x) == unicode else str(x) for x in stats]
        #players[Pid] = stats_unicode
        #print ';'.join(stats_unicode)
        
