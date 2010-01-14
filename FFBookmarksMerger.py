#!/usr/bin/env python
# -*- coding:utf8 -*-
# This script will merge all json bookmarks files from current directory
#

import json
import os

def ParseChildren(children,folder=""):
    for child in children:
        if "children" in child.keys():
            return ParseChildren(child)
        return child


bookmarks_files=[]
for file in os.listdir("."):
    if file.endswith(".json"):
        bookmarks_files.append(file)

mainjson={}
currentjson={}
for file in bookmarks_files:
    with open(file,"r") as f:
        currentjson=json.load(f)
    print file," as been loaded"
    if not mainjson:
        mainjson=currentjson
        continue
    print "merging ..."



print "writing file ./a.out.json"
with open("./a.out.json","w") as f:
    json.dump(mainjson, f, indent=2)