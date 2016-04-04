#!/usr/bin/python
# coding: utf8

import json
import requests
import re

from BoR_auth import BoR_User

User = BoR_User ()
url = 'http://api.blackoutrugby.com/'

def BoR_Request(params):
    resp = requests.get(url=url, params=params)
    data = json.loads(resp.text)
    return data

def BoR_Players_By_Team (ID_Team, Nat=0, U20=0):
    params = dict (d = User.Dev_ID,
                   m = User.Member_ID,
                   mk = User.Member_Key,
                   dk = User.Dev_Key,
                   r = 'p',
                   teamid = ID_Team,
                   json = '1'
                   )
    return BoR_Request (params)

def BoR_Players_By_Fixture (Fixture_ID):
    params = dict (d = User.Dev_ID,
                   m = User.Member_ID,
                   mk = User.Member_Key,
                   dk = User.Dev_Key,
                   r = "fs",
                   fixtureid = Fixture_ID,
                   json = '1'
                   )
    return BoR_Request (params)

def BoR_Team_Name (Team_ID):
    params = dict (d = User.Dev_ID,
                   m = User.Member_ID,
                   mk = User.Member_Key,
                   dk = User.Dev_Key,
                   r = 't',
                   teamid = Team_ID,
                   json = '1'
                   )

    data = BoR_Request (params)
    return data['teams'][Team_ID]['name']

def BoR_Fixture_Info (Fixture_ID):
    params = dict (d = User.Dev_ID,
                   m = User.Member_ID,
                   mk = User.Member_Key,
                   dk = User.Dev_Key,
                   r = "f",
                   fixtureid = Fixture_ID,
                   json = '1'
                   )
    return BoR_Request (params)
