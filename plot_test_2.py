# plot_test_2
"""Plotting example from ICPP"""

import matplotlib.pyplot as plt

plt.figure(1)  # create figure 1
plt.plot([1, 2, 3, 4], [1, 7, 3, 5])  # draw on figure 1
plt.figure(2)
plt.plot([1, 4, 2, 3], [5, 6, 7, 8])
plt.savefig('Figure-2')
plt.figure(1)
plt.plot([5, 6, 10, 3])
plt.savefig('Figure-1')

#plt.show()  #show figure on screen
