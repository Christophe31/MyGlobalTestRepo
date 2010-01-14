#!/usr/bin/env python
# -*- coding:utf8 -*-
# This script will merge all json bookmarks files from current directory
#

import json
import os

def ParseChildren(children,folder=[]):
    for child in children:
        if not "children" in child.keys():
            elementCopy(child,folder)
        else:
            folder.append(child["title"])
            if not elementCopy(child):
                ParseChildren(child)


def elementCopy(child,folder):
    """return true if it works, false if not"""
    s="mainjson"
    for dir in folder:
        s+='["children"]'
        tmp=[ i for i in range(len(eval(s))) if eval(s)[i]["title"]==folder[0]]
        if not tmp:
            eval(s).append(child)
            return True
    return False

def merge(child, folder):
    while dir in folder:
        for element

def refreshIds():
    pass

bookmarks_files=[]
for file in os.listdir("."):
    if file.endswith(".json"):
        bookmarks_files.append(file)

mainjson={}
for file in bookmarks_files:
    currentjson = None
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
