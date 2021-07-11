#!/usr/bin/env python3

class RecRead(object):
    def __init__(self, delim):
        self.delim = delim

    def parse(self, record):
        (self.lastname, self.firstname, self.email, self.dob, self.favcolor) = record.split(self.delim)

blanks = []
commas = []
pipes = []

rex = {' ' : ('blanks.txt', blanks),
       ',' : ('commas.txt', commas),
       '|' : ('pipes.txt', pipes)
       }

for d in rex.keys():
    (val,lyst) = rex[d]
    
    records = open(val)
    for r in records:
        reader = RecRead(d)
        reader.parse(r)
        lyst.append(reader)

    lyst.sort(key = lambda reader: reader.lastname)
    for r in lyst:
        print(r.lastname)
        


        
