'''
Created on Jun 11, 2018

@author: Haoran Yu
'''
import math
def distance(a,b):#a, b are two tuple
   return math.sqrt((b[0]-a[0])**2+(b[1]-a[1])**2)

def left_list(tup, del_index):
   return tuple([i for i in tup if tup[del_index]!=i])

#find all combinations under Set S  
def combinations(N, iterable):
   if not N:
       return [[]]
   if not iterable:
       return []

   head = [iterable[0]]
   tail = iterable[1:]
   new_comb = [ head + list_ for list_ in combinations(N - 1, tail) ]
   return new_comb + combinations(N, tail)

def sellman(nodes,graph):
   A={}
   lst=[i for i in range (0,nodes)]
   res=[[]]
   for n in range(1, len(lst) + 1):
       res+=combinations(n, lst)
   iter_combo_lst=[tuple(i)for i in res ]
   for size in range(1,nodes+1):
       #print("size:",size)
       A[size]={}
       for i_combo in iter_combo_lst:
           if 0 in i_combo and size==len(i_combo):
               A[size][i_combo]={}
               
               if i_combo==(0,):
                    
                   A[size][i_combo][(0,)]=0 
   if nodes>=2:
      
       for two_combo in A[2].keys():
           A[2][two_combo][two_combo]=distance(graph[0],graph[two_combo[1]])
      
   if nodes>=3:   
       for size in range(3,nodes+1):
            for multi_size_combo in A[size].keys():
              
               for del_i in range (1,len(multi_size_combo)):#save which vertex we will end at as the smallest key
                   dict_last_element=A[size-1][left_list(multi_size_combo,del_i)]
                   min=10000.0#magic number for infinity
                   path=tuple()                  
                   for dict_last_element_item in dict_last_element:                      
                       if dict_last_element[dict_last_element_item]+\
distance(graph[dict_last_element_item[len(dict_last_element_item)-1]],graph[multi_size_combo[del_i]])<min:
                           min=dict_last_element[dict_last_element_item]+\
distance(graph[dict_last_element_item[len(dict_last_element_item)-1]],graph[multi_size_combo[del_i]])
                           path=dict_last_element_item
                                            
                   path+=(multi_size_combo[del_i],)
                  
                   A[size][multi_size_combo][path]=min
       min2=10000.0   
       dic_final_temp=A[nodes][tuple( [i for i in range(0,nodes)] )]
       final_path=[]
       for k in dic_final_temp  :
           if  dic_final_temp[k]<min2:
               min2=dic_final_temp[k]
               final_path=list(k)
       return final_path;   
   if nodes==2:  
       for two_combo in A[2].keys():
           return list(list(A[2][two_combo].keys())[0])
