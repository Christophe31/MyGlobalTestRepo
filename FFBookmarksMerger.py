#!/usr/bin/env python
# -*- coding:utf8 -*-
# This script will merge all json bookmarks files from current directory
#

import json
import os
mainjson={}
bookmarks_files=[]

def parseChildren(children,folder=[]):
    for child in children["children"]:
        if not "children" in child.keys():
            elementCopy(child,folder)
        else:
            nfolder=folder+[child["title"]]
            if not elementCopy(child,nfolder):
                parseChildren(child,nfolder)

def elementCopy(child,folder):
    """return true if it works, false if not"""
    global mainjson
    pt=mainjson
    print child["title"]
    for dir in folder:
        pt=pt["children"]
        #print  dir ,folder
        tmp=[ i for i in range(len(pt)) if pt[i]["title"]==dir]
        if not tmp:
            pt.append(child)
            return True
        else:
            pt=pt[tmp[0]]
    return False

for file in os.listdir("."):
    if file.endswith(".json"):
        bookmarks_files.append(file)

for file in bookmarks_files:
    currentjson = None
    with open(file,"r") as f:
        currentjson=json.load(f)
    print file," as been loaded"
    if not mainjson:
        mainjson=currentjson
        continue
    print "merging ..."
    parseChildren(currentjson)
#refreshid
print "writing file ./a.out.json"
with open("./a.out.json","w") as f:
    json.dump(mainjson, f, indent=2)
