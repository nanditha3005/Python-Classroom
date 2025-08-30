employees=[{"eid":1,"ename":"Munroe","gender":"Male"},
{"eid":2,"ename":"Lewes","gender":"Male"},
{"eid":3,"ename":"Lowrance","gender":"Male"},
{"eid":4,"ename":"Yanaton","gender":"Male"},
{"eid":5,"ename":"Sharl","gender":"Female"},
{"eid":6,"ename":"Livia","gender":"Female"},
{"eid":7,"ename":"Marje","gender":"Female"},
{"eid":8,"ename":"Esmaria","gender":"Female"},
{"eid":9,"ename":"Sterling","gender":"Male"},
{"eid":10,"ename":"Mercy","gender":"Female"},
{"eid":11,"ename":"Lutero","gender":"Male"},
{"eid":12,"ename":"Robenia","gender":"Female"},
{"eid":13,"ename":"Cathi","gender":"Female"},
{"eid":14,"ename":"Norbert","gender":"Male"},
{"eid":15,"ename":"Hanni","gender":"Female"},
{"eid":16,"ename":"Gray","gender":"Female"},
{"eid":17,"ename":"Glenna","gender":"Female"},
{"eid":18,"ename":"Tomkin","gender":"Male"},
{"eid":19,"ename":"Davis","gender":"Male"},
{"eid":20,"ename":"Trixy","gender":"Female"},
{"eid":21,"ename":"Robb","gender":"Male"},
{"eid":22,"ename":"Waylin","gender":"Male"},
{"eid":23,"ename":"Evy","gender":"Female"},
{"eid":24,"ename":"Eldredge","gender":"Male"},
{"eid":25,"ename":"Sorcha","gender":"Female"},
{"eid":26,"ename":"Emelyne","gender":"Female"},
{"eid":27,"ename":"Egor","gender":"Male"}]

#print no of male Employees from above source
no_of_male_employees=0
no_of_female_employees=0
for emp in employees:
    if emp['gender']=='Male':
        no_of_male_employees=no_of_male_employees+1
    if emp['gender'] =='Female':
        no_of_female_employees=no_of_female_employees+1

print("No of Male Emplyees:", no_of_male_employees)
print("No of Female Emplyees:", no_of_female_employees)