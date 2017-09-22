# -*- coding:utf-8 -*-  
# file: FileMerage.py  
#  
  
import os  
import random
output = open( 'train.txt','w')

for line in open('group_1.txt'):
	output.writelines(line)

for line in open('group_2.txt'):
	output.writelines(line)

for line in open('group_3.txt'):
	output.writelines(line)

for line in open('group_4.txt'):
	output.writelines(line)
	
output.close()