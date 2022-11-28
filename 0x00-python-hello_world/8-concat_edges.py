#!/usr/bin/python3
str = "Python is an interpreted, interactive, object-oriented programming\
         language that combines remarkable power with very clear syntax"
str = str[39:66] + str[:6] + str[115:119]
str = str[:27] + " " + str[33:37] + " " + str[27:33]
print(str)
