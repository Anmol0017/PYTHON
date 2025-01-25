student ={
    "name": "Mark",
    "roll":14,
    "subjects":{
        "maths": 90,
        "science": 85,
        "english": 80
    }
}

print(student.keys())
print(student.values())
print(student.items())
print(student.get("name"))
print(student["name"])
print(student.update({"city":"Delhi"}))
print(student)

student["subjects"].update({"maths": 95})
print(student)