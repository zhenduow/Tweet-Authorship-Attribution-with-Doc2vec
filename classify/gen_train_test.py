# -*- coding:utf-8 -*-  
# file: FileMerage.py  
#  
  
import os  
import random

lines=[]
for line in open('random_subset_of_corpus.txt'):  
	lines.append(line)			
	
random.shuffle(lines)

all_data=[]
datasize=len(lines)
group_num=5
group_size=datasize/group_num
for i in range(group_num):
	group = lines[(i)*group_size:(i+1)*group_size]
	all_data.append(group)

for i,group in enumerate(all_data):
	output = open( 'group_'+str(i+1)+'.txt','w')
	for line in group:
		output.writelines(line)
	output.close()
