#!/usr/bin/env python
import sys

target = sys.stdin

for line in target:
    l = line.split("\t")
    number_tags = len(l)
    if number_tags > 12:
        XS_tag = l[12].strip("\n")
        AS_tag = l[11].strip("\n")
        XS_split = XS_tag.split(":")
    #    XS_int = int(XS_split[-1])
        if str(XS_split[0]) == "XS":
            AS_split = AS_tag.split(":")
            AS_int = int(AS_split[-1])
     #       XS_split = XS_tag.split(":")
            XS_int = int(XS_split[-1])
            if AS_int > XS_int:
                print line.replace("\n", "")
        else:
            print line.replace("\n", "")
    else:
        print line.replace("\n", "")