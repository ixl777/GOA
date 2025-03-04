# Dictionary-ის შექმნა
student_info = {
    "name": "Andria",
    "surname": "Smith",
    "academy": "Tbilisi Academy",
    "fav-color": "Blue",
    "city": "Tbilisi",
    "goa-student": True,
    "age": 14,
    "fav-programming-lang": "Python"
}
for key, value in student_info.items():
    print(f"{key}: {value}")

sample_dict = {
    "name": "Andria",
    "surname": "Gobejishvili",
    "academy": "GOA Academy",
    "fav-color": "Green",
    "city": "Tbilisi"
}
print("Keys:", sample_dict.keys())
print("Values:", sample_dict.values())
print("Key-Value pairs:", sample_dict.items())
for key, value in sample_dict.items():
    print(f"Key: {key} | Value: {value}")

