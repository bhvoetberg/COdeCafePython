import matplotlib.pyplot as plt

year = [1950, 1970, 1990, 2010]
pop = [2519, 3692, 5263, 6972]
# plt.plot(year, pop)
# plt.show()


print(year[-1])
plt.scatter(year, pop)
plt.xlabel('Year')
plt.ylabel('Population')
plt.title('World population')
# plt.yticks([0, 1000, 2000, 3000, 4000, 5000, 6000, 7000])
plt.yticks([0, 1000, 2000, 3000, 4000, 5000, 6000, 7000], ['0', '1 milj.', '2 milj.', '3 milj.', '4 milj.', '5 milj.', '6 milj.', '7 milj.', ])
plt.show()