#!/usr/bin/python
# coding: utf8

from datetime import datetime

positions = ['p1', 'p2', 'p3', 'p4', 'p5', 'p6', 'p7', 'p8', 'p9', 'p10', 'p11', 'p12', 'p13', 'p14', 'p15',
             'b1', 'b2', 'b3', 'b4', 'b5', 'b6', 'b7']

lines = {'Front row' : ['p1', 'p2', 'p3'],
         'Locks' : ['p4', 'p5'],
         'Back row' : ['p6', 'p7', 'p8'],
         'Halves' : ['p9', 'p10'],
         'Centres' : ['p12', 'p13'],
         'Backs' : ['p11', 'p14', 'p15']}

Stats = ['weight', 'height', 'aggression', 'discipline', 'csr', 'experience', 'energy', 'form']

def BoR_Time (brt):
    return datetime(int(brt[0:4]), int(brt[5:7]), int(brt[8:10]),
                    int(brt[11:13]), int(brt[14:16]), int (brt[17:19]))


class Lineup:
    def __init__ (self, lineup, players):
        self.lineup_position = lineup
        self.players_stats = players
        self.lineup_stats = {}

        for I in positions:
            player = self.players_stats [str (lineup[I])]
            player_stat = [player[x] for x in Stats]
            player_stat = [int (x) for x in player_stat]
            self.lineup_stats[I] = player_stat

    def scrum_weight(self):
        W = Stats.index ('weight')
        ret = 100 * (self.lineup_stats['p1'][W] + self.lineup_stats['p3'][W]) + 75 * self.lineup_stats['p2'][W]
        ret = ret + 75 * (self.lineup_stats['p4'][W] +  self.lineup_stats['p5'][W])
        ret = ret + 50 * self.lineup_stats['p8'][W] + 25 * (self.lineup_stats['p6'][W] + self.lineup_stats['p7'][W])
        ret = ret / 525 * 8
        return ret

    def per_line(self, Index):
        ret = {}
        for I in lines:
            ret[I] = 0.0
        for line in lines:
            for I in lines[line]:
                ret[line] = ret[line] + self.lineup_stats[I][Index]
        for line in lines:
            ret[line] = int (ret [line] * 10 / len (lines[line])) / 10.0
        return ret

    def Compare (self, guest):
        print "Self vs Guest"
        print " * Scrum *"
        print "   Weight : " + str (self.scrum_weight()) + " " + str (guest.scrum_weight())

    def Display_Info(self):
        print "Scrum weight (with coef) : " + str (self.scrum_weight())
        print "Aggressivity per lines : "
        print self.per_line(Stats.index ('aggression'))
        print "Discipline per lines : "
        print self.per_line(Stats.index ('discipline'))
        print "CSR per lines : "
        print self.per_line(Stats.index ('csr'))
        print "Experience per lines : "
        print self.per_line(Stats.index ('experience'))
        print "Form per lines : "
        print self.per_line(Stats.index ('form'))
        print "Energy per lines : "
        print self.per_line(Stats.index ('energy'))

        
