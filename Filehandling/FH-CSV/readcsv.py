import csv

fp=open('emp.csv','r')
emp_data=csv.reader(fp)
print(emp_data)            #<_csv.reader object at 0x0000018A04BAEC80>
print(type(emp_data))      #<class '_csv.reader'>

for emp in emp_data:
    print(emp)              #['eid', 'name', 'esal']
                            #['101', 'rahul', '45000.45']
                            #['102', 'sonia', '34000.45']
                            #['103', 'priyanka', '56000.45']

