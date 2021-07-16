#!/usr/bin/env python3

from flask import Flask, jsonify, request

from hw import readem, get_colorz, get_dobz, get_namez, addrec, RecRead

import json



app = Flask(__name__)

readem()
colorz = get_colorz()
dobz = get_dobz()
assert len(colorz) > 0
namez = get_namez()
for n in namez:
    print(n)



    
@app.route('/records/', methods=['POST'])
def create_record():
   
    rawrecord = request.get_data()
    print('rawrecord: ', rawrecord)
    
    addrec(rawrecord)
    return jsonify(str(rawrecord))


@app.route('/records/color')
def colorrec():
    for c in colorz:
        print(c)
    j = jsonify(colorz)
    return j

@app.route('/records/birthdate')
def dobeez():
    j = jsonify(dobz)
    return j


@app.route('/records/name')
def donames():
    j = json.dumps(namez)
    return j

