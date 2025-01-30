import matplotlib.pyplot as plt

fruit =["apple","mango","banana"]
quantity =[10,34,50]

plt.bar(fruit ,quantity)
plt.title ("fruit vs quantity")
plt.xlabel("fruits")
plt.ylabel("quantity")
plt.show()