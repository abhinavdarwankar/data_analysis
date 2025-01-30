import matplotlib .pyplot as plt
 
subjects= ["DSA","Web development","SAD","AI"]
marks=[90,80,70,60]
plt.pie(marks,labels=subjects,)
plt.title("marks in different subject")
plt.show()