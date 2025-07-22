import matplotlib.pyplot as plt

x=(2,2,2,2,4,6,6,6,6)
y=(10,20,30,40,20,40,30,20,10)

plt.plot(x,y, color= "blue", linewidth=4)
plt.scatter(x,y,color="red")
plt.show()
