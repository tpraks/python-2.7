import os

file_name=raw_input("Enter File Name :" )
f=open(file_name+".tmp",'w+')
f.write("abcdefghijkl")
f.close()
