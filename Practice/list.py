lst=[1,3,2,4,'Hello'] #similar to array, but allows heterogenious datatypes 
print(lst) #printing whole list
print(lst[4]) #printing particular index value
print(lst[-1]) #prints index value from end
print(lst[1:3]) #prints range of values
lst[4]=5 #manipulating list values
print("New List:",lst)
lst.insert(5,6) #insert 6 at 5th index value
#lst.appent(6) works the same and appends in the end of list
lst.sort()
print("Sorted List: ", lst)
lst.sort(reverse = True)
print("Reverse Sort: ", lst)
print("Newer List:",lst)
lstap=['q','w','e','r','t','y']
lst.extend(lstap)
print("Extended List: ",lst)
print(len(lst)) #prints list length