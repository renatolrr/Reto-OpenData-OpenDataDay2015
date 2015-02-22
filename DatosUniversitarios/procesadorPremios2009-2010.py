#!/usr/bin/env python
# -*- coding: utf-8 -*-
import csv
import re

n=0
noEncontrado=-1
titulacion="ninguna"
fila="fila"

reader=csv.reader(open('premios2009-2010.csv','rb'), delimiter=',')
f=open('premios2009-2010-limpio.csv', 'w')


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
