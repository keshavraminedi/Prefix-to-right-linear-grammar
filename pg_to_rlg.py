# -*- coding: utf-8 -*-
"""
Created on Tue Jul 14 21:58:09 2020

@author: Keshav Raminedi
"""

def parser(productions):
    '''prints the Right linear grammar for legibility
    input:dictonary
    output: returns nothing
    '''
    for i in productions: 
        for j in productions[i]:
         if (j[0]!='' and j[0]!='e') and (j[1]=='' or j[1]=='e'):
             #print(1)
             print('<'+i.upper()+'>'+' --> '+'<'+j[0].upper()+'>'),
         elif (j[0]==''or j[0]=='e') and (j[1]!='' and j[1]!='e'):
            #print(2) 
            print('<'+i.upper()+'>'+' --> '+j[1])
         elif (j[0]==''or j[0]=='e') and (j[1]=='' or j[1]=='e'):
            #print(3)  
            print('<'+i.upper()+'>'+' --> '+'e') 
         else:
           #print(4)     
           print('<'+i.upper()+'>'+' --> '+j[1]+'<'+j[0].upper()+'>'),
############################################################################################           
def cleaning(dic):
  '''cleans the grammar
  dic:dictonary
  returns:dictonary'''
  for i in dic:
      for j in dic[i]: 
       if j[1]=='':
           if j[0]==i:
               dic[i].remove(j)         
  return dic             
############################################################################################              
def cstack(l):
 '''returns the copy of a list
 l: list
 returns:list'''   
 p=[]
 for i in l:
  p.append(i)  
 return p         
def prefix(s,s1):
 '''checks if s is a prefix of s1
 s:string
 s1:string
 return:tuple(boolean,string)''' 
 prefixes=[s1]   
 for i in range(0,len(s1)):
   prefixes.append(s1[0:i])
 prefixes.remove('')  
 if s in prefixes:
       return (True,s1[len(s):])# returning true when it is a prefix with the suffix
 return (False,'')#return false when not a prefix with an empty string
 
#################################################################################################
def inf_loop(l):
    '''checks if the main function is paring through a infinite loop that is going nowhere
    l:list
    return:boolean'''
    dic={}
    for i in l:
        if i[0] not in dic:
            dic[i[0]]=[]
        if (i[1],i[2]) not in dic[i[0]]: # if in dic then it is an infinite loop  
         dic[i[0]].append((i[1],i[2]))
        else:
           return True  
    return False   
############################################################################################# 
def main(stack,start,dic,target,finaltarget,path):
 '''produces rules other than Ginit
 Ginit:initial rules after 
 stack:list
 dic:dictonary
 target:string
 finaltarget:string
 path=list
 path1=list
 returns:dictonary'''   
 done=False
 stack1=cstack(stack)
 #start1=start
 target1=target
 finaltarget1=finaltarget
 path.append((start,target,finaltarget))
#inifite loop check 
 if inf_loop(path):
     done=True
 '''non-terminal start: P...for each rule in stack of form A->xB.......'''
 while(not done):
     tuple1=stack1.pop()
     if tuple1[1]=='':#if x=='e'
         if tuple1[0] in dic:  
          main(cstack(dic[tuple1[0]]),tuple1[0],dic,target1,finaltarget1,path)#recursive call
     elif prefix(target1,tuple1[1])[0]:# if P is prefix of x         
         if finaltarget1 not in dic:
           dic[finaltarget1]=[] 
         if (tuple1[0],prefix(target1,tuple1[1])[1]) not in  dic[finaltarget1]: 
          dic[finaltarget1].append((tuple1[0],prefix(target1,tuple1[1])[1]))
     elif prefix(tuple1[1],target1)[0]:# if x is prefix of P
        if tuple1[0] in dic: 
         target2=prefix(tuple1[1],target1)[1]   
         main(cstack(dic[tuple1[0]]),tuple1[0],dic,target2,finaltarget1,path)#recursive call
     if not stack1:# when stack is empty end the loop
      done=True     
 return dic 
      
 ###############################################################################################        
def change(p,q):
    '''returns false if there is no difference between two dictonaries
    p=dictonary
    q=dictonary
    return:boolean'''
    if p.keys()!=q.keys():
        return True
    for i in p.keys():
        if p[i]!=q[i]:
            return True #return true no change
    return False 
##############################################################################################   
def pgtorlg(symbols,strings,productions): 
    ''' produces Ginit and calls the main function which produces the remainig rules 
    symbols:tuple of symbols in prefix grammar
    strings:list of strings
    productions:dictonary
    returns:dictonary (right linear grammar )'''
    print('The prefix grammar is ')
    print(symbols,strings,productions)
    productions_rlg_initial={'S':[]}
    '''....................................................................................'''
    for i in strings: #adds the base strings to right linear grammar
     if i=='e':   
      productions_rlg_initial['S'].append(('',''))
     else: 
      productions_rlg_initial['S'].append(('',i)) 
    '''......................................................................................'''   
    for i in productions.keys():#adds the initial productions of type S->xA
      for j in productions[i]:  
           
       if j=='e': 
          
        productions_rlg_initial['S'].append((i,''))
       else:
        productions_rlg_initial['S'].append((i,j))  
    '''...................................................................................'''    
    p=productions_rlg_initial
    changed=False
    while(not changed):#continously checking for new rules for each nonterminal except 'S'
        q=p.copy()
        for i in productions.copy():
            p=main(cstack(p['S']),'S',p,i,i,[]) #call to main function for rules of type A->xB
        if not change(p,q):# if  no new rule can be added 
            changed=True #end the while loop
    #print(p)  
    print('The Right-linear grammar is:')       
    parser(cleaning(p))  
################################################################################################### 
def space():
  print('---------------------------------------------------')                        
##############################################################################################        
if  __name__ == '__main__':
    
    pgtorlg(('a','b'),['ab'],{'a':['aab'],'ab':['abb']})
    space()

    pgtorlg(('a','b'),['ab'],{'a':['aab'],'aababb':['ab','abb']}) 
    space()   
                
    pgtorlg(('a','b','c'),['aa'],{'a':['ab'],'aa':['c']})
    space()
    pgtorlg(('a','b'),['ab'],{'a':['aab'],'aababb':['ab','abb'],'ab':['b']})
    space()
    pgtorlg(('a','b','c','d'),['abcd'],{'a':['cdd'],'cd':['abb']})
    space()
    pgtorlg(('a','b','c','d'),['ab','cd'],{'a':['b'],'b':['a'],'ab':['bba'],'c':['d'],'d':['c']})
    space()
    pgtorlg(('a','b'),['ba'],{'b':['bab'],'ba':['a'],'a':['bb']})
    space()
    pgtorlg(('a','b'),['ab'],{'a':['e'],'b':['ab'],'ab':['e ']})
    space()
    pgtorlg(('a','b','c'),['abc'],{'a':['e'],'bc':['ab'],'b':['c'],'c':['a']})
    space()
    pgtorlg(('a','b'),['ab'],{'a':['aab'],'aa':['aabba'],'aabba':['e']})
    space()
    pgtorlg(('a','b','c'),['bcb'],{'b':['a','e'],'ac':['e'],'c':['e']})
    space()
    pgtorlg(('a','b','c'),['c'],{'c':['ab'],'a':['e'],'b':['c']})
    space()
    pgtorlg(('a','b','c'),['bc'],{'b':['e'],'c':['abab'],'aba':['b'],'bb':['e']})
    space()
    pgtorlg(('a','b'),['ab'],{'b':['e'],'a':['b'],'bb':['b']})
    space()
    pgtorlg(('a','b'),['a'],{'a':['bab'],'ba':['a'],'ab':['e'],'bab':['b']})
    space()
    pgtorlg(('a','b'),['abab'],{'aba':['e'],'b':['a'],'ab':['b']})
    space()
    pgtorlg(('a','b'),['ababa'],{'a':['e','bb'],'bab':['e'],'b':['aba']})
    space()
    pgtorlg(('c','b'),['bc'],{'b':['bc','c','e'],'ccc':['bc'],'c':['e']})
    space()
    pgtorlg(('a','d','c','b'),['abcd'],{'b':['acd','e'],'a':['bcd','e'],'c':['e','abd'],'d':['abc','e']})
    space()
    pgtorlg(('a','g'),['aga'],{'ag':['a'],'a':['ag'],'aga':['e'],'aa':['e']})
    space()
    pgtorlg(('c','b'),['bccb'],{'b':['bc'],'bc':['bccc'],'bccc':['b'],'bb':['e']})