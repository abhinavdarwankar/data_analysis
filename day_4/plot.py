import matplotlib.pyplot as plt

days=[" sunday","monday","tuesday","wednesday",]
sales=[120,300,567,321]

plt.plot(days,sales,marker='o')
plt.title("sales over days")
plt.xlabel("days")
plt.ylabel("sales")
plt.show()
