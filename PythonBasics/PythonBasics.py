print("Hello")
#this is comment
a=5
print(a)

#print num and string together
print("{}{}".format("value is ",a))
print(type(a))

#print strings together
b="string"
print("value is "+b)

#array/List in python allow all datatypes in one array
arr=[1, "str", 2]
print("{}{}".format("value is ",arr[0]))
arr.insert(1,"str2")
print(arr)

#tuple is immutable
tup=(1, 2, "str", 4.5)

#dictionary
dict={1:"tulip", 3:2, "a":9}
print(dict["a"])

#if-else-elif
age=10
if age<18:
    print("age is less than 18")
elif age>18:
    print("age is greater than 18")
else:
    print("age is equal to 18")