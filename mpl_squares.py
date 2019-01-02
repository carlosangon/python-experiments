import matplotlib.pyplot as plt

squares = [1, 4, 9, 16, 25, 32]
plt.plot(squares, linewidth=5)

# Set chart title and label axes
plt.title("Square Snumbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)

# Set size of tich labels
plt.tick_params(axis='both', labelsize=14)

plt.plot(squares)
plt.show()

