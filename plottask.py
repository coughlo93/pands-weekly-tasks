import numpy as np 
import matplotlib.pyplot as plt

# Generate data for normal distribution
mean = 5
std_dev = 2
data = np.random.normal(mean, std_dev, 1000)

# Generate data for the function h(x) = x^3
x = np.linspace(0, 10, 100)
y = x**3

# Plotting
plt.figure(figsize=(10, 6))

# Histogram of normal distribution
plt.hist(data, bins=30, alpha=0.7, label='Normal Distribution')

# Plot of the function h(x) = x^3
plt.plot(x, y, color='red', linewidth=2, label='$h(x) = x^3$')

# Set plot title and labels
plt.title('Normal Distribution and $h(x) = x^3$')
plt.xlabel('x')
plt.ylabel('Frequency / h(x)')
plt.legend()

# Show plot
plt.grid(True)
plt.show()
