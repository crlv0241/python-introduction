students = [
  {"name":"Carl","id":"19-2136"},
  {"name":"Masha","id":"19-2137"},
  {"name":"Rizal","id":"19-2111"}
]

def f(person):
  return person["id"]

#sort by id using function
students.sort(key = f)
print("Sort by id using function")
print(students)

#sort by name using lambda(1 line function)
print("Sort by name using lambda(1 line function)")
students.sort(key = lambda person : person["name"])
print(students)
