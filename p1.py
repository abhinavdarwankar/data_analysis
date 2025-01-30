import matplotlib.pyplot as plt

fruit = ['apple', 'banana', 'mango']
sales = [100, 200, 300]

plt.bar(fruit, sales)
plt.xlabel('Fruit')
plt.ylabel('Sales')
plt.title('Fruit Sales')  # Optional: Add a title for clarity
plt.show()
