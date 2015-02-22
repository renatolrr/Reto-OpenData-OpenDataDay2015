#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Uso:
python procesadorPremios.py <nombre fichero entrada> <nombre fichero salida>
"""

import csv
import re
import sys

reader=csv.reader(open(sys.argv[1],'rb'), delimiter=',')
f=open(sys.argv[2], 'w')


for row in reader:
    #Si no está la palabra DNI
    if row[0].find('DNI')==-1:
        #Si no está la palabra ÁREA:
        if row[0].find('ÁREA')==-1:
            #Si la cadena son mayúsculas:
            if row[0].isupper():
                #Si la cadena no tiene el primer campo vacío:
                    if len(row[0])>1:
                        f.write(row[0]+','+row[1]+','+row[2]+','+row[3])
                        f.write('\n')

f.close
