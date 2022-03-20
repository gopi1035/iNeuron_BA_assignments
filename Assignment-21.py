#!/usr/bin/env python
# coding: utf-8

# #### Q1. Write a function that takes a list and a number as arguments. Add the number to the end of the list, then remove the first element of the list. The function should then return the updated list.

# In[8]:


def listd(lt,num):
    if len(lt) > 1:
        lt.append(num)
        lt.pop(0)
        return lt
    else:
        print("No list has been selected")


# In[9]:


listd([6, 9, 3, 6, 5], 5)


# #### Q2. Create the function that takes a list of dictionaries and returns the sum of people & budgets.

# In[27]:


def get_budget(dt):
    if type(dt) == list:
        sum = 0
        for i in dt:
            sum += i["budget"]
        return sum
    else:
        print("Not a list")


# #### Q3. Create a function that takes a string and returns a string with its letters in alphabetical order.

# In[44]:


def alphabet_soup(t):
    t1 = ""
    x= sorted(t)
    for i in x:
        t1 += i
    return t1


# In[46]:


alphabet_soup("edabit")


# #### Q4. Create a function that accepts the principal p, the term in years t, the interest rate r, and the number of compounding periods per year n. The function returns the value at the end of term rounded to the nearest cent.

# In[185]:


def compound_interest(**kwrgs):
    """ p = principal, r = rate of interest, t = term in year(s), n = Number of Compound in given period"""
    p = kwrgs['p']
    r = kwrgs['r']/100
    t = kwrgs['t']
    n = kwrgs['n']

    return round(p*((1+r/n)**(n*t)),2)


# In[186]:


compound_interest(p = 100000, t = 20, r = 15, n = 365)


# #### Q5. Write a function that takes a list of elements and returns only the integers.

# In[177]:



def return_only_integer(lt):
    global l1
    if type(lt) == list:
        for i in lt:
            if type(i) == int:
                l1.append(i)
            elif type(i) == list:
                return_only_integer(i)
    return l1


# In[152]:


return_only_integer([10, "121", 56, 20, "car", 3, "lion",[5,6,3,[5,96,"Gopi"]]])


# In[ ]:




