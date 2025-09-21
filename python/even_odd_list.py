# list = [1, 2, 3, 4, 5, 6, 7, 8, 9 ]
# even = []
# odd = []

# def solution(data):
#   for num in data:
#     if num%2==0:
#       even.append(num)
#     else:
#       odd.append(num)

#   return even+odd

# # print(solution(list))

# list = 'my23name45is'
# output=''
# alphabet=[char for char in reversed(list) if char.isalpha()]
# print(alphabet)
# i=0
# for char in list:
#     if char.isalpha():
#        output=output + alphabet[i]
#        i=i+1
#     else:
#         output=output+char
# print (output)

#!/bin/bash
# src_dir= "/var/log"

# backup_dir="/backup/logs"

# filename="backup_log_$(date +'%d/%m/%Y_%H:%M:%S').tar.gz"

# tar -cvfz $backup_dir/$filename $src_dir

# echo "backup completed: $filename"

# def FindComplement(num):
#   binary=bin(num)[2:]
#   complement=''
#   for bit in binary:
#       if bit =='1':
#          complement+='0'
#       else:
#          complement+='1'
#   return int(complement, 2)

# n=int(input("enter a number: "))
# print(FindComplement(n))

# list1="sky is blue"
# mylist=list1.split()
# print(mylist)
# mylist=mylist[::-1]
# print(mylist)
# list2=" ".join(mylist)
# print(list2)

#!/bin/bash

# service="apache2"

# if ! systemctl is-active --quiet apache2; 
# then
#     echo "$service is not running, restarting..."
#     systemctl start $service
# else
#     echo "Apache is running."
# fi


# #!/bin/bash
# input="$1"
# while IFS= read -r line 
# do 
# sudo useradd $line
# echo "user $line created"
# done < "$input"

# list=[1,2,2,2,3,3,3,4,5,5,5,]  #output [1,4]
# mylist=[]
# for num in list:
#   if list.count(num)==1:
#     mylist.append(num)

# print(mylist)

# listing="a,a,a,b,b,c,c,c"
# list=listing.split(',')
# visited=[]
# final_list=[]
# for ch in list:
#     if ch not in visited:
#         final_list.append(f"{ch}:{list.count(ch)}")
#         visited.append(ch)
# print(final_list) 
# print(",".join(final_list)) 

# listing = "a,a,a,b,b,c,c,c"
# list = listing.split(',')

# char_count = {}
# for ch in list:
#     if ch in char_count:
#         char_count[ch] = char_count[ch]+ 1
#     else:
#         char_count[ch] =  1        

# final_list = [f"{char}:{count}" for char, count in char_count.items()]

# print(",".join(final_list))

# list=[4,12,43.5,19,100]
# # print(max(list))
# # list.sort(reverse=True)
# # print(list[0])
# # max=list[0]
# # for ele in list:
# #     if ele>max:
# #         max=ele
# # print(max)        

# min=list[0]
# for ele in list:
#     if ele<min:
#         max=ele
# print(min)        

# lang1=['marathi', 'hindi', 'gujrati', 'urdu']
# lang2=['english', 'french', 'japanese']

# for ele in lang2:
#     lang1.append(ele)
# print(lang1)

#OR

# lang1.extend(lang2)
# print(lang1)

# list=[3,5,8,12,15]
# sq=[]
# for ele in list:
#     sq.append(ele*ele)
# print(sq)

# #OR
# print([ele*ele for ele in list])

# list=[3,5,8,12,15]
# sq=[]
# for ele in list:
#     if ele%2==0:
#      sq.append(ele*ele)
# print(sq)

# #OR
# print([ele*ele for ele in list if ele%2==0])

# list=[3,5,8,12,15]
# sq=[]
# for ele in list:
#     if ele%2!=0:
#      sq.append(ele*ele)
# print(sq)

# #OR
# print([ele*ele for ele in list if ele%2!=0])

# list=[3,5,8,12,15]
# even=[]
# odd=[]
# for ele in list:
#     if ele%2==0:
#      even.append(ele*ele)
#     else:
#        odd.append(ele*ele)
# print(even)
# print(odd)

# #OR
# print([ele*ele for ele in list if ele%2==0])
# print([ele*ele for ele in list if ele%2!=0])


# list=input("enter the listing: ")

# print(list[::-1])

# list2=list.split()

# print(list2[::-1])

# my_list=[]
# for ele in list2:
#     my_list.append(ele[::-1])
# print(my_list)

# list=["hello",10,20,40,20,60,40,30]
# list2=[]
# for ele in list:
#     if list.count(ele)==1 and ele not in list2:
#         list2.append(ele)
# print(list2)

# for i in range(len(list)):
#     for j in range(i+1, len(list)):
#         if list[i]!=list[j] and list[i] not in list:
#             list2.append(list[i])
# print(list2)

# my_dict = { "key1": [1, 2, 3],"key2": ["a", "b", "c"],"key3":25}

# count=0
# for i in my_dict:
#     if isinstance(my_dict[i],list):
#         count+=1

# print(count)

# list="I love you"
# count=0
# vowels=['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
# for char in list:
#     if char in vowels:
#       count+=1
# print(count)

# list="codeyug"
# reverse=""

# for char in list:
#     reverse=char+reverse

# print(reverse)

# list=input("enter a listing: ")
# count=int(input("enter count: "))
# list1=list.split()
# dict={}
# for word in list1:
#     if word in dict:
#         dict[word]+=1
#     else:
#         dict[word]=1
# list=[]
# for key in dict:
#     if dict[key]>=count:
#         list.append(key)
# if len(list)>0:
#     print(list)
# else:
#     print("NA")

# list=['apple','apple','cat', 'cat','man']
# dict={}
# for word in list:
#     if word not in dict:
#         dict[word]=1
#     else:
#         dict[word]+=1
# print(dict)

# list="A7B1R3"
# char=[]
# digit=[]
# for ele in list:
#     if ele.isalpha():
#         char.append(ele)
#     else:
#          digit.append(ele)
# result= (sorted(char)+sorted(digit))
# print(''.join(result))
# n=int(input("enter a number: "))
# for i in range(1, n+1):
#     power=len(list(i))
#     sum=0
#     temp=i
#     while temp>0:
#         digit=temp % 10
#         sum=sum+digit**power
#         temp=temp // 10
#     if sum==i:
#         print(i)
        
# a=int(input("enter a number: "))
# b=int(input("enter second number: "))
# a,b=b,a
# print(a,b)

# num=[3,2,4] 
# target=6
# d={}
# for i in range(len(num)):
#     d[num[i]]=i

# for i in range(len(num)):
#    need=target-num[i]
   
#    if (need in d.keys() and d[need]!=i):
#        print(i,d[need])

# list=[5,3,1,4,-8,-8]
# (list.sort())
# print(list)
# x,y=list[-1],list[-2]
# print(x,y)

# def max_product(arr):
#     l=len(arr)
#     if l<2:
#         print("pair not exist")
#         return
#     x=arr[0]
#     y=arr[1]
#     for i in range(len(arr)):
#         for j in range(i+1, len(arr)):
#             if arr[i]*arr[j] > (x*y):
#                 x=arr[i]
#                 y=arr[j]
#     return x,y           
# arr=eval(input("enter array: "))
# print(max_product(arr))

#for one rotation
# nums=[5, -2, 3, 9, 0, 6, 10, 7] 
# n=len(nums)
# temp = nums[n-1]   
# for i in range(n-1,0,-1):
#     nums[i]=nums[i-1]
# nums[0]=temp
# print(nums)

# #for k rotation
# nums=[5, -2, 3, 9, 0, 6, 10, 7] 
# n=len(nums)
# k=eval(input("enter a number:"))
# rotation=k%n
# for i in range(0,rotation):
#     ele=nums.pop()
#     nums.insert(0,ele)
# print(nums)

# str="sky is blue"
# new_str=str.split()

# new_str[::-1]

# str1=" ".join(new_str)
# print(str1)

# list=[1,2,2,2,2,3,3,4,5,5,5]
# mylist=[]
# # for i in list:
# #     if i not in mylist:
# #         mylist.append(i)
# # print(mylist)
# # mylist=set(list)
# # print(mylist)
# for num in list:
#     if list.count(num)==1:
#         mylist.append(num)
# print(mylist)

# str = "a,a,a,b,b,c,c,c"
# mystr=str.split(",")
# print(str)
# print(mystr)
# visited=[]
# final_list=[]
# for ch in mystr:
#     if ch not in visited:
#         final_list.append(f"{ch}:{mystr.count(ch)}")
#         visited.append(ch)
# print(final_list)
# lower=100
# upper=200

# for num in range(lower, upper+1):
#     for i in range(2, num):
#         if num%i==0:
#             break
#     else:
#         print(num, end=" ")
        
# n=eval(input("enter the number: "))#10
# sum=0
# for i in range(2, n+1):
#    for j in range(2, i):
#       if (i%j==0):
#          break
#    else:
#        print(i)
#        sum+=i
# print(sum)

# list=[5, -2, 3, 9, 0, 6, 10, 7] 
# n=max(list)
# n1=min(list)
# print(n,n1)

# max=list[0]
# min=list[0]
# for ele in list:
#     if ele>max:
#         max=ele
#     if ele<min:
#         min=ele
# print(max, min)
# lang1=['marathi', 'hindi']
# lang2=['english', 'french']
# # for word in lang2:
# #     lang1.append(word)
# # print(lang1)

# lang1.extend(lang2)
# print(lang1)

# std={'ajay':1000, 'raj':1200, 'vijay':1400}
# # # for ele in std:
# # key_list=list(std.keys())
# # print(key_list[-1], std[key_list[-1]] )
# list=list(std.keys())[-1]
# print(f"{list}:{std[list]}" )
# #
# str="python is easy"
# l=str.split()
# l1=[]
# for word in l:
#     l1.append(word[::-1])
# print(l1)

# nums=[3,9,5,6,7,2]
# n=len(nums)#n=6
# k=3
# rotation=k%n
# for i in range(0, rotation):
#     ele=nums.pop()
#     nums.insert(0,ele)
# print(nums)
#0-9


# def get_substring(str, start, end):
#     result=""
#     index=0
#     for char in str:
#       if index>=start and index<=end:
#          result=result+char
#          index=index+1
#     return result
     
# str="i love you my friend"
# start=0
# end=9
# substring=get_substring(str, start, end)
# print(substring)

# def is_palindrom(list):
#     return list==list[::-1]

# print(is_palindrom([1,2,1]))

# def reversed_arraay(nums, start,end):
#     while start<end:
#         nums[start],nums[end]=nums[end],nums[start]
#         start+=1
#         end-=1
#     return nums
    
# nums=[3,9,5,6,7,2]
# n=len(nums)
# num=reversed_arraay(nums,0,n-1)
# print(num)

# num = [1, 2, 3, 1, 2, 4, 5, 3, 6]
# duplicates = []

# for i in num:
#     if num.count(i) < 2 and i not in duplicates:
#         duplicates.append(i)


# print("uniq elements:", duplicates)

# str='my23name45is'
# rvs_str=[char for char in reversed(str) if char.isalpha()]
# output=''
# i=0
# for chr in str:
#     if chr.isalpha():
#         output=output+rvs_str[i]
#         i=i+1
#     else:
#         output=output+chr
# print(output)

# def FindComplement(num):
#   binary=bin(num)[2:]
#   complement=''
#   for bit in binary:
#       if bit =='1':
#          complement+='0'
#       else:
#          complement+='1'
#   return int(complement, 2)

# n=int(input("enter a number: "))
# print(FindComplement(n))
# list=[1,2,3,4,5]
# count=0
# for i in list:
#     count+=1
# print(count)

# def comman_Letter():
#     str1=input("enter first string")
#     str2=input("enter second string")
#     s1=set(str1)
#     s2=set(str2)
#     cmn_letter=s1 &s2
#     print(cmn_letter)

# comman_Letter()

# def count_words():
#     str=input("enter a string ")
#     list=str.split()
#     d={}
#     for i in list:
#         if i in d.keys():
#             d[i]=d[i] + 1
#         else:
#             d[i]=0

#     print(d)
# count_words()


    











     