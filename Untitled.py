#!/usr/bin/env python
# coding: utf-8

# In[6]:


# High blood pressure     sis_press = sistolic pressure  
# dis_press = diastolic pressure
name1 = "Qodir"
sis_press_1 = 130
dis_press_1 = 75

name2 = "Botir"
sis_press_2 = 140
dis_press_2 = 90

name3 = "Sobir"
sis_press_3 = 180
dis_press_3 = 100

name4 = "Sardor"
sis_press_4 = 140
dis_press_4 = 100


# In[13]:


def high_bp (name, sis_press, dis_press,):
    if sis_press >= 135 or dis_press >= 90 :
        print (name + "has high BP")
        if sis_press >= 140 or dis_press >= 100:
            print  (name + " should take a medicine")
    else:
        print (name + " has normal BP")
            
        


# In[14]:


result1 = high_bp(name1, sis_press_1, dis_press_1)
result2 = high_bp(name2, sis_press_2, dis_press_2)
result1 = high_bp(name3, sis_press_3, dis_press_3)
result1 = high_bp(name4, sis_press_4, dis_press_4)


# In[ ]:




