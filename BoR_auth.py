#!/usr/bin/python
# coding: utf8

import json

class BoR_User:

    def __init__ (self, file = 'user.json'):
        Dev_File_Conf = open (file)
        Dev_Conf = json.load (Dev_File_Conf)

        self.Member_ID = Dev_Conf['Member_ID']
        self.Member_Key = Dev_Conf['Member_Key']
        self.Dev_ID = Dev_Conf['Dev_ID']
        self.Dev_Key = Dev_Conf['Dev_Key']
