
# coding: utf-8

# In[1]:


import pandas as pd
import re


# In[7]:


def seq_to_word(path,char_size):
    data = pd.read_csv(path)
    word = []
    dot = ''
    for i in range(char_size):
        dot = dot + '.'
    for i in range(len(data['0'])):
        temp = []
        for j in range(char_size):
            temp = temp + re.findall(dot, data['0'].iloc[i][j:])
        word.append(temp)
    return word


# In[8]:


def create_dictionary(word_list):
    dic={}
    for i in range(len(word_list)):
        for j in word_list[i]:
            if j in dic.keys():
                dic[j]=dic[j]+1
            else:
                dic[j]=1
    return dic
    


# In[9]:


#fbound is frequency boundary
def frequency_count(dic,fbound):
    Dic={}   
    for keys,values in dic.items():
        if values>fbound:
            Dic[keys]=values
    return Dic        
    


# In[10]:


#argument are file name of text file and Dictionary to store in it
def text_file_for_dict(file,Dic):
    f=open(file,"w")
    for i in Dic.keys():
        f.write(i)
        f.write(',')
    f.close()
    


# In[17]:


path = 'C:/Users/User/protein_project/project_data/train-bp.csv'
char_size = 3
fbound = 1000
text_file_name = '3_gram_1000_fbound.txt'
word = seq_to_word(path,char_size)
dic = create_dictionary(word)
Dic = frequency_count(dic,fbound)
text_file_for_dict(text_file_name,Dic)
print('For %d length word and frequency count %d '%(char_size,fbound))
print('length of dic :'+str(len(dic)))
print('length of Dic :'+str(len(Dic)))


# In[18]:


#file name in list as aargument like file_list = ['file1.txt', 'file2.txt', ...]
def join_file(com_file,file_list):
    filenames = file_list 
    with open(com_file, 'w') as outfile:
        for fname in filenames:
            with open(fname) as infile:
                for line in infile:
                    outfile.write(line)


# In[19]:


file_list = ['3_gram_300_fbound.txt','4_gram_300_fbound.txt','5_gram_300_fbound.txt'] 
com_file = 'com_3_4_5_300_fbound.txt'
join_file(com_file,file_list)

