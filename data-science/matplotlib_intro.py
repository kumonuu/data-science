import matplotlib.pyplot as plt

x = [1,2,3,4,5]
y = [1,4,9,16,25]

plt.figure(figsize=(5,5))
plt.title("graph")
plt.scatter(x,y,label="quadratic")
plt.scatter([1,2,3,4,5],[1,8,27,64,125],label="cubic")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()

plt.savefig("figure.png")
