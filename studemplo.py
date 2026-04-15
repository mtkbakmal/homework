students = {"Tom", "Bob", "Sam"}
employees = {"Tom", "Bob", "Alex", "Mike"}
print("Все:", students | employees)

print("Учатся и работают:", students & employees)

print("Только учатся:", students - employees)

print("Либо только учатся либо только работают:", students - employees, employees - students)