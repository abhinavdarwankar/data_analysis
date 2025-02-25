import matplotlib.pyplot as plt

colour=["red","yellow","brown","black"]
size=[50,80,60,100]

plt.bar(colour,size)
plt.title("colour vs size")
plt.xlabel(colour)
plt.ylabel(size)
plt.show()