#how to exclude csv header using list slicing
import csv
fp=open('emp.csv','r')
emp_data=csv.reader(fp)

for emp in list(emp_data)[1:]:
    print(emp)        #['101', 'rahul', '45000.45']
                      #['102', 'sonia', '34000.45']
                      #['103', 'priyanka', '56000.45']
