#day13 [25 june 2024]
# Graphs in  Python
# Bar Charts
import matplotlib.pyplot as plt
categories = ['A', 'B', 'C', 'D']
values = [3, 7, 1, 5]

plt.bar(categories, values, color='blue')

# Add labels and title
plt.xlabel('Categories')
plt.ylabel('Values')
plt.title('Bar Chart')
plt.show()

#Scatter Plots

x = [1, 2, 3, 4, 5, 6]
y = [5, 6, 7, 8, 6, 5]

plt.scatter(x, y, color='green', marker='x')

plt.xlabel('X Axis')
plt.ylabel('Y Axis')
plt.title('Scatter Plot')
plt.show()

#  Histograms
data = [1.5, 2.1, 2.9, 3.2, 3.5, 4.0, 4.3, 4.7, 5.0, 5.1]

plt.hist(data, bins=5, color='orange')

plt.xlabel('Value')
plt.ylabel('Frequency')
plt.title('Histogram')
plt.show()

