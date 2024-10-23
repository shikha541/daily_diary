# day12 [24 june 2024]
# Matplot lib 
#  Importing of  matplot pip install matplotlib
# Plotting of maps
# ploting with single lines 
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [1, 4, 9, 16, 25]

plt.plot(x, y)

plt.xlabel('X Axis')
plt.ylabel('Y Axis')
plt.title('Simple Line Plot')

plt.show()

#Plotting Multiple Lines

x = [1, 2, 3, 4, 5]
y1 = [1, 4, 9, 16, 25]
y2 = [2, 4, 6, 8, 10]

# Plot both lines
plt.plot(x, y1, label='y = x^2', color='blue')
plt.plot(x, y2, label='y = 2x', color='green')


plt.xlabel('X Axis')
plt.ylabel('Y Axis')
plt.title('Multiple Line Plot')
plt.legend()
plt.show()

# Customizing the Plot


x = [1, 2, 3, 4, 5]
y = [1, 4, 9, 16, 25]

plt.plot(x, y, color='red', linestyle='--', marker='o', label='Data')

plt.xlabel('X Axis')
plt.ylabel('Y Axis')
plt.title('Customized Line Plot')
plt.legend()

# Display the plot
plt.show()



