#!/usr/bin/env python
# -*- coding:utf8 -*-
# This script will merge all json bookmarks files from current directory
#

import json
import os

def ParseChildren(children,folder=[]):
    for child in children:
        if not "children" in child.keys():
            merge(child,folder)
        else:
            if not foldercopy(child):
                ParseChildren(child)

def foldercopy(folder):

def merge(child, folder):
    while dir in folder:
        for element


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
