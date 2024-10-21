

mylist=["heloo","hey","oyeee","nice","hiii"]
print(mylist[-3:-1])


thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)


thislist1 = ["apple", "banana", "cherry"]
thislist1.remove("banana")
print(thislist1)

thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)

thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)


thislist = ["apple", "banana", "cherry"]
mylist = thislist[:]
print(mylist)


PyList=[1,2,3,"HELLO",5,6,["PYTHON"]]
print(PyList)

print(PyList[6][0]) #python
print(PyList[-1])
print(PyList[-1][-1])
print(PyList[-1][-1][-2])

print(PyList[-1][-1][-1][0])

print(PyList[-1][-1][-1][-1])
print(PyList[3][0])
print(PyList[3][-3])




print("--------------------------------------------------------------------------------------------------")
PyList=["Big Data", "Hadoop", "Spark", "IoT"] 
print(PyList[0:2])   
print(PyList[1:2]) 
print(PyList[1:-2])  
print(PyList[:3]) 
print(PyList[:]) 




print("--------------------------------------------------------------------------------------------------")


PyList=["Big Data", "Hadoop", "Spark", "IoT"] 
#Start:Stop
print(PyList[1:3])
#Start:Stop:Step(Increment)
print(PyList[1:3:1])
#Start:Stop:Step(Increment)
print(PyList[1:4:2])#Alternate, Hadoop, IoT
#Start:Stop:Step(Increment)
print(PyList[1:4:3])#TwoElements, Hadoop
#Start:Stop:Step(decrement)
print(PyList[3:1:-1])#IoT, SPARK
#Start:Stop:Step(decrement)
print(PyList[3:2:-2])#IoT


print("--------------------------------------------------------------------------------------------------")



listx=[1, 5, 7, 3, 2, 4, 6]  
print(listx)  
sublist=listx[2:7:2] 
print(sublist)  
sublist=listx[6:4:-3]   
print(sublist)  


print("--------------------------------------------------------------------------------------------------")


listx=[1, 5, 7, 3, 2, 4, 6, 10, 11]  
print(listx[7:1:-3])
print(listx[2:7:2])
print(listx[2:7])
print(listx[:4])
print(listx[3:])





print("--------------------------------------------------------------------------------------------------")

PyList=[1,3,4,6,7,8,9]
print(PyList)
print(PyList[1:5])
print(PyList[1:5:1])
print(PyList[1:5:2])
print(PyList[1:5:3])
print(PyList[1:5:4])
print(PyList[5:1:-1])
print(PyList[5:1:-2])
print(PyList[5:1:-3])
print(PyList[6:0:-4])



print("--------------------------------------------------------------------------------------------------")


#Double Slice Operator:
PyList=[1,2,3,4,5,6,7,8,9,10]
print(PyList)
print(PyList[::1])
print(PyList[::2])
print(PyList[::3])
print(PyList[::4])
print(PyList[::-1])
print(PyList[::-2])
print(PyList[::-3])
print(PyList[::-4])


print("--------------------------------------------------------------------------------------------------")

#append



py_list=["Big Data", "Hadoop", "Spark", "IoT"]  
print(py_list)  
py_list.append("PYTHON")  
print(py_list)



alist = ['a', 'b', 'c']
alist.append(['d', 'e','f'])
print(alist)


py_list=["Big Data", "Hadoop", "Spark", "IoT"]  
print(py_list[0])  
py_list[0]="DataScinece" 
print(py_list)  
print(py_list[0])


py_list=["Big Data", "Hadoop", "Spark", "IoT"]  
print(py_list)  
py_list[2]="PYTHON"
print(py_list) 



print("--------------------------------------------------------------------------------------------------")

PyList=["BigData"]
print(PyList)
PyList.append(("ML","BC"))
print(PyList)
PyList.append({"AI"})
print(PyList)
PyList.append({1:"PYTHON"})
print(PyList)


print("--------------------------------------------------------------------------------------------------")

#extend()


alist1 = ['a', 'b', 'c']
alist1.extend(['d', 'e','f'])
print(alist1)



# Appending two lists
Countries = ["India", "Pakistan", "Sri Lanka"]
African_Countries = ["Egypt", "Kenya", "Namibia", "Zimbabwe"]
Countries.extend(African_Countries)
print(Countries)

print("--------------------------------------------------------------------------------------------------")
#Python List insert()


MyData = ['Big', 'Data', 'Hadoop', 'Spark']
MyData.insert(2, 'TERADATA')
print('Updated List: ', MyData)
print("--------------------------------------------------------------------------------------------------")


#list.index(item[,start][,end])
PyList=[1,2,3,3,2,1,5,4]
print(PyList)
print(PyList.index(1))
print(PyList.index(3))
print(PyList.index(4))
print(PyList.index(3,3))
print(PyList.index(1,3))
print(PyList.index(2,4))
print(PyList.index(4,4,10))




PyList=[1,2,3,1,4,5,2,5,6,1,4]
print(PyList)
print(PyList.index(2))
print(PyList.index(2,2))
print(PyList.index(1,2,7))
print(PyList.index(4,3,9))
print("--------------------------------------------------------------------------------------------------")



PyList=["Big Data", "Hadoop", "Spark", "IoT", "Hadoop"]  
print(PyList.count("Hadoop"))

PyList=[1,2,3,1,2,3,3,3,1,2,33]
print(PyList.count(2))
print(PyList.count(3))
print(PyList.count(1))

print("--------------------------------------------------------------------------------------------------")



PyList=['cc','b','aaa','eeee','ddddddd']
print(PyList)
PyList.sort(key=len)
print(PyList)


PyList=[[1,2],[2,4],[4,5],[3,1]]
print(PyList)
PyList.sort()
print(PyList)
print("--------------------------------------------------------------------------------------------------")




PyList=[[1,2],[2,4],[4,5],[3,1]]
print(PyList)
def SortBySecondValue(item):
    return item[1]
PyList.sort(key=SortBySecondValue)
print(PyList)

print("--------------------------------------------------------------------------------------------------")
#reverse

PyList=["Big Data", "Hadoop", "Spark", "IoT"]  
print(PyList)  
PyList.reverse()  
print(PyList)  



PyList=[1,2,3,1,2,3,3,3,1,2,33]
print(PyList)
PyList.append(333)
print(PyList)
PyList1=PyList.copy()
print(PyList1)
PyList1.append(444)
print(PyList1)

print("--------------------------------------------------------------------------------------------------")



py_list=["Big Data", "Hadoop", "Spark", "IoT"]  
print(py_list)  
py_list.append("DataScinece")  
py_list.append("PYTHON")  
print(py_list)  
py_list.pop()  	
py_list.pop()  
print(py_list)

print("--------------------------------------------------------------------------------------------------")

PyList=[]
for i in range(10):
    if i%2==1:
        PyList.append(i)
        print(PyList)
        
        
s = [1, 1,3, 4, 5]
print(all(s))

s = [0, False]
print(all(s))


s = []
print(all(s))


s =[1, 3, 4, 0]
print(any(s))


s = [0, False]
print(any(s))


s = [0, False, 5]
print(any(s))

s = []
print(any(s))


BigData=['Big Data', 'Hadoop', 'Spark','Data Science']
eData = enumerate(BigData)
print(type(eData))
print(list(eData))


bd = ['Big Data', 'Hadoop', 'Spark','Data Science']
for item in enumerate(bd):
  print(item)
  
  
  bd = ['Big Data', 'Hadoop', 'Spark','Data Science']
for count, item in enumerate(bd, 100):
  print(count, item)

names = ['Bob', 'Alice', 'Guido']
for index, value in enumerate(names):
    print(f'{index}: {value}')
print("--------------------------------------------------------------------------------------------------")
    
    
#Example:
A=[1]*2
print(A)
B=[[1]*2]*5
print(B)
C=[[2,0]*1]*4
print(C)

print("--------------------------------------------------------------------------------------------------")

A=[2]*3
print(A)
B=[[2]*3]*2
print(B)
C=[[1,0]*1]*5
print(C)


Fives = [5]*4
print(Fives)
print("--------------------------------------------------------------------------------------------------")


A=[1,2,3,4,5]
print(A[0]*2)
print(A*2)
print(A[3]*3)
print(A[4]*1)
print(A*3)


