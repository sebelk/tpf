#! /usr/bin/python3
archivo = open('/etc/resolv.conf','r')
lectura = archivo.readline()
print(lectura,end='')
lectura = archivo.readline()
