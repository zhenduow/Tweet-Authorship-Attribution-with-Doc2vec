# -*- coding:utf-8 -*-  
# file: FileMerage.py  
#  
'''
Split the docvec set into a training set and a test set.
This step is equivalent to one test of manual cross validation.

From the authorship attribution set, sample a set with customized (author_num*text_num).
Then use 20% of the set as test, 80% as training.
'''

import os  
import random
import re

# customize the size of test size
author_num = 50
text_num = 1000

mergefiledir = os.getcwd()+'\\'+'clean_embedding'
foldernames = os.listdir(mergefiledir)  

author_list=[]
for foldername in foldernames:
	author_list.append(foldername)

random_author_list = random.sample(author_list, author_num)

output = open( 'random_subset.txt','w')  
for author_name in random_author_list:
	filepath = mergefiledir+'\\'+author_name  
	count=0
	for line in open(filepath):  
		count+=1	
		if count<=text_num:
			m = re.match('(\S+) (.+)', line)
			author = m.group(1)
			output.write(str(random_author_list.index(author_name)))
			output.write(' ')
			output.write(m.group(2)) 
			output.write('\n')				

output.close()  


lines=[]
for line in open('random_subset.txt'):  
	lines.append(line)			
	
random.shuffle(lines)

all_data=[]
datasize=len(lines)
group_num=5
group_size=datasize/group_num
for i in range(group_num):
	group = lines[(i)*group_size:(i+1)*group_size]
	all_data.append(group)
	
output_train = open( 'clf_train.txt','w')
output_test = open( 'clf_test.txt','w')	
for i,group in enumerate(all_data):
	if (i+1) <= 0.8*group_num:
		for line in group:
			output_train.writelines(line)
	else:
		for line in group:
			output_test.writelines(line)
output_train.close()
output_test.close()
