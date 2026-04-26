patients = ["Zain", "Rabia", "Sadia", "Fajar", "Hadia"]

# Now add weights list here
weights = [98, 78, 65, 82, 70]

# Now write your for loop here
for i in range(len(patients)):
    if weights[i] > 70:
        print(patients[i], "needs diet plan")
    else:
        print(patients[i], "weight is normal")
