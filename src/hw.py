#!/usr/bin/env python3

from datetime import datetime
import copy
import requests
import threading
import time

class RecRead(object):
    def __init__(self, delim):
        self.delim = delim.encode()

    def parse(self, record):
        try:
            bytesrec = record.encode()
        except AttributeError:
            bytesrec = record

        (self.lastname, self.firstname, self.email, self.dobtext, self.favcolor) = bytesrec.rstrip().split(self.delim)
        self.dob = datetime.strptime(self.dobtext.decode(),'%m/%d/%Y').date()
        self.colorname = self.favcolor + self.lastname

    
        
blanks = []
commas = []
pipes = []

rex = {' ' : ('blanks.txt', blanks),
       ',' : ('commas.txt', commas),
       '|' : ('pipes.txt', pipes)
       }

def stringize(dob):
    return dob.strftime("%m/%d/%Y")


colorz = None
dobz = None
namez = None

def get_colorz():
    color2 = []
    for c in colorz:
        color2.append((c.lastname.decode(),c.firstname.decode(),c.email.decode(),stringize(c.dob),c.favcolor.decode()))
    return color2

def get_dobz():
    dobz2 = []
    for c in dobz:
        dobz2.append((c.lastname.decode(),c.firstname.decode(),c.email.decode(),stringize(c.dob),c.favcolor.decode()))
    return dobz2

def get_namez():
    namez2 = []
    for c in namez:
        namez2.append((c.lastname,c.firstname,c.email,stringize(c.dob),c.favcolor))
    return namez2

biglyst = []

def loadem():

   global colorz, dobz, namez, biglyst
   print('loading em')
        
   biglyst.sort(key = lambda reader: reader.colorname)
   for r in biglyst:
       print(r.lastname, r.colorname)
   colorz = copy.deepcopy(biglyst)

   biglyst.sort(key = lambda reader : reader.dob)
   for r in biglyst:
       print(r.dob)
   dobz = copy.deepcopy(biglyst)
   biglyst.sort(key = lambda reader : reader.lastname, reverse = True)
   for r in biglyst:
       print(r.lastname)
   namez = copy.deepcopy(biglyst)


   for r  in colorz:        
       print(r.colorname, r.lastname)


def readem():
    global biglyst
    
    for d in rex.keys():
        (val,xlyst) = rex[d]

        records = open('../data/' + val)
        for r in records:
            reader = RecRead(d)
            reader.parse(r)
            xlyst.append(reader)
        biglyst += xlyst

    loadem()


def addrec(onerec):
    global biglyst
    
    
    reader = RecRead(',')
    reader.parse(onerec)

    biglyst.append(reader)
    print('after record added:', len(biglyst))
