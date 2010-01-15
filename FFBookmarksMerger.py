#!/usr/bin/env python
# -*- coding:utf8 -*-
# This script will merge all json bookmarks files from current directory
#

import json
import os
mainjson={}
bookmarks_files=[]

def merge(source,target=[]):
    for child in source["children"]:
        if not "children" in child.keys():
            addChild(child,target)
        else:
            #ntarget=[e for e in target["children"] if e["title"]==child["title"]][0]
            if not addChild(child,target):
                merge(child,[e for e in target["children"] if e["title"]==child["title"]][0])

def addChild(child,target):
    """return true if it works, false if not"""
    print child["title"]
    if not [i for i in target["children"] if i["title"]==child["title"]]:
        target["children"].append(child)
        return True
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
    merge(currentjson,mainjson)
#refreshid
print "writing file ./a.out.json",
with open("./a.out.json","w") as f:
    json.dump(mainjson, f, indent=2)
print "done"
