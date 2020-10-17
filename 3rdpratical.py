#Write a Python program to sum all the items in a list
list1=[1,2,3,4]
y=0
for x in range(0, len(list1)): 
    y= y + list1[x] 
print("sum of all elements in list: ",y)


'''Write a Python program to count the number of strings where the string length is 2 or more and the first and last character are same from a given list of strings
List=['abc', 'xyz', 'aba', '1221']
for x in List:
 if List[0] == List[-1]:
     print("match words are: ") '''


# Write a Python program to remove duplicates from a list
list2=[1,2,3,3,2,2,4,5,66,88,9]
list_items=set()
sorted_items=[]
for x in list2:
    if x not in list_items:
     sorted_items.append(x)
     list_items.add(x)
print(list_items)

#Write a Python function that takes two lists and returns True if they have at least one common member.
def common_element(A,B):
 for i in A:
    for j in B:
        if i==j:
            result=True
print(common_element([1,2,3,4],[2,4,56,6]))