#Part 1- given the following list create a program that outputs their names
# students = {
#          {'first_name':  'Michael', 'last_name' : 'Jordan'},
#          {'first_name': 'John', 'last_name' : 'Rosales'},
#          {'first_name': 'Mark', 'last_name' : 'Guillen'},
#          {'first_name': 'KB', 'last_name' : 'Tonel'}
#     }
# print user['students']


# Part 2 - given the folloing dictionar create a program that prints something?
users = {
 'Students': [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
  ],
 'Instructors': [
     {'first_name' : 'Michael', 'last_name' : 'Choi'},
     {'first_name' : 'Martin', 'last_name' : 'Puryear'}
  ]
 }
for key, data in users.items():
     print "\n%s" %key.title()
     counter = 0

     for value in data:
         counter = counter +1
         name = value['first_name'] + " " + value["last_name"]
         name_count = len(value['first_name']) + len(value["last_name"])

         print "%d - %s - %d" %(counter, name, name_count)
