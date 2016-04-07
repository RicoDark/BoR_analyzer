#!/usr/bin/python
# coding: utf8

import sys
from datetime import timedelta

from BoR_utils import BoR_Time, positions, Lineup
from BoR_request import BoR_Fixture_Info, BoR_Team_Name, BoR_Team_Lineup, BoR_Players_Info

relevant = ['name', 'csr', 'age', 'weight', 'height', 'form', 'energy', 
            'aggression', 'discipline', 'leadership', 'experience', 'stamina',
            'handling', 'attack', 'defense', 'technique', 'strength', 'jumping',
            'speed', 'agility', 'kicking', 'pops']

#players = {}

def Analyze_Fixture (fixture_id):
    data = BoR_Fixture_Info (fixture_id)
    BoR_time = BoR_Time (data['brt'])
    fixture = data['fixtures'][fixture_id]
    fixture_time_start = BoR_Time (fixture['matchstart'])
    home_team_id = fixture['hometeamid']
    guest_team_id = fixture['guestteamid']
    if BoR_time > fixture_time_start:
        print "Fixture already started (and maybe finished)"
    elif BoR_time > fixture_time_start - timedelta (hours = 2):
        print "Lineups and tactics are set"
    elif BoR_time > fixture_time_start - timedelta (hours =  3):
        print "Lineups are set, tactics can be modified"
    else:
        print "Fixture to be played ..."

    Home_Team_Name = BoR_Team_Name (home_team_id)
    #print "Home -> " + home_team_id + " - " + Home_Team_Name
    lineup_home = BoR_Team_Lineup (home_team_id, fixture_id)
    player_lineup = lineup_home['lineups'][0]
    Players_ID = []
    for I in positions:
        Players_ID.append (player_lineup[I])
    players_stats = BoR_Players_Info (Players_ID)
    home_lineup = Lineup (player_lineup, players_stats)
    #home_lineup.Display_Info()
    
    Guest_Team_Name = BoR_Team_Name (guest_team_id)
    #print "Guest -> " + guest_team_id + " - " + Guest_Team_Name
    lineup_guest = BoR_Team_Lineup (guest_team_id, fixture_id)
    player_lineup = lineup_guest['lineups'][0]
    Players_ID = []
    for I in positions:
        Players_ID.append (player_lineup[I])
    players_stats = BoR_Players_Info (Players_ID)
    guest_lineup = Lineup (player_lineup, players_stats)
    #guest_lineup.Display_Info()

    print
    print " "*(22 - len (Home_Team_Name)) + Home_Team_Name + " - " + Guest_Team_Name
    home_lineup.Compare (guest_lineup)



if __name__ == '__main__':
    if len (sys.argv) != 2:
        print "You have to give the fixture ID"
        exit (1)
    fixture_id = sys.argv [1]
    Analyze_Fixture (fixture_id)
