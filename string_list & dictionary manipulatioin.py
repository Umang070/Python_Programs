#!/usr/bin/env python
# coding: utf-8

# ### String Manipulation

# In[1]:


st = "umang"

type(st)


# In[2]:


#how many methods and functions are associated with string class
dir(st)


# In[10]:


ste = "umang    "

ste.strip() #both side
ste.rstrip() #right side

ste.startswith('u')
ste.find("g",2)   #find "g" start with 2


# In[59]:


file_content_obj = open(r"C:\Users\UMANG PATEL\Desktop\Data Science\DS.txt")
cnt = 0
# file_content = file_content_obj.read()  #we read whole file in a single string including spaces and "\n"
# file_content
for content in file_content_obj:
#     cnt+=1
       
    #   if content.startswith("import"):
       if not 'pd' in content:
           print(content, end="")
    
# print("There are {} lines in file".format(cnt))


# ### List  & Dictionary Manipulation

# In[77]:


l1 = [1,20,3]
l2 = [4,50,6]
# print(l1+l2)
# dir(l1)

l2.extend([10,11])#insert element not list
l2.append([1,2])#insesrt as a list
l1.sort()


# In[78]:


friends = [ 'Joseph', 'Glenn', 'Sally' ]
friends.sort()
print(friends[0])


# In[1]:


stuff = dict()
# stuff['candy']=0 
# print(stuff['candy']) #this gives errors
# print(stuff.get('candy',-1))   #this gives o/p 1

stuff['one'] = 1
stuff['two'] = 2
for i,j in stuff.items():  #if not items then it print only key
    print(i,j)


# In[ ]:




