patients = ["Ali", "Sara", "Ahmed", "Fatima"]

ages = [25, 32, 45, 28]

total = 0

for age in ages:
    total = total + age

average_age = total / len(ages)

print("Total patients:", len(patients))
print("Average age:", average_age)

patients = ["Ali", "Sara", "Ahmed", "Fatima"]
ages = [25, 32, 45, 28]

for i in range(len(patients)):
    if ages[i] > 30:
        print(patients[i], "needs senior checkup")
    else:
        print(patients[i], "is young and healthy")
patients = ["Zain", "Rabia", "Sadia", "Fajar", "Hadia"]

# Now add weights list here
weights = [98, 78, 65, 82, 70]

# Now write your for loop here
for i in range(len(patients)):
    if weights[i] > 70:
        print(patients[i], "needs diet plan")
    else:
        print(patients[i], "weight is normal")
