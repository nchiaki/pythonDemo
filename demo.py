#!/usr/bin/python

import os
import sys
import json

def trans_json_deepdict(pkey,jsndt):
    for key in jsndt:
        vle = jsndt[key]
        #print type(vle)
        if type(vle) is dict:
            nkey = pkey + ':' + key
            trans_json_deepdict(nkey,vle)
        elif type(vle) is list:
            nkey = pkey + ':' + key
            trans_json_deeplist(nkey,vle)
        else:
            print "L15:%s:%s:\t%s" % (pkey,key,vle)

def trans_json_deeplist(pkey,jsndt):
    for key,vle in enumerate(jsndt):
        #vle = jsndt[key]
        if type(vle) is dict:
            nkey = pkey + ':' + str(key)
            trans_json_deepdict(nkey,vle)
        elif type(vle) is list:
            nkey = pkey + ':' + str(key)
            trans_json_deeplist(nkey,vle)
        else:
            print "L27:%s:%s:\t%s" % (pkey,key,vle)

def trans_json_dict(jsndt):
    for key in jsndt:
        vle = jsndt[key]
        #print type(vle)
        if type(vle) is dict:
            trans_json_deepdict(key,vle)
        elif type(vle) is list:
            trans_json_deeplist(key,vle)
        else:
            print "L39:%s:\t%s" % (key,vle)

def trans_json_list(jsndt):
    for key,vle in enumerate(jsndt):
        #vle = jsndt[key]
        if type(vle) is dict:
            trans_json_deepdict(str(key),vle)
        elif type(vle) is list:
            trans_json_deeplist(str(key),vle)
        else:
            print "%s:\t%s" % (str(key),vle)

def trans_json(fnm):
    fl = open(fnm, 'r')

    isJson = False
    try:
        jsndt = json.load(fl)
        isJson = True
    except:
        pass

    fl.close()
    if isJson:
        jsntyp = type(jsndt)
        print "L64:%s type %s" % (fnm, jsntyp)
        if type(jsndt) is dict:
            trans_json_dict(jsndt)
        elif type(jsndt) is list:
            trans_json_list(jsndt)
    else:
        print "Ordinary %s" % (fnm)


for pram in sys.argv:
    #print pram
    if os.path.exists(pram):
        #print "File: %s" % (pram)
        trans_json(pram)
