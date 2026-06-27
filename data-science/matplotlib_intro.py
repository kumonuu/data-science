import matplotlib.pyplot as plt

x = [1,2,3,4,5]
y = [1,4,9,16,25]

plt.figure(figsize=(5,5))
plt.title("graph")
plt.plot(x,y,'b--',label="quadratic")
plt.plot([1,2,3,4,5],[1,8,27,64,125],'r-.',label="cubic")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()


#plt.savefig("figure.png")

plt.figure(figsize=(5,5))
plt.title("bar graph")
#plt.bar([1,3,5,7,9],[2,4,6,8,10])
plt.bar(["Male","Female"],[23,41])
plt.show()