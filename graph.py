import pandas as pd
import matplotlib.pyplot as plt

# Sample data
data = {
    'Dataset (Images per Alphabet)': [200, 300, 400, 500, 600],
    'Accuracy': [100.0, 100.0, 99.90314769975787, 99.96136012364761, 99.93504384540435]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Plot the data
plt.figure(figsize=(10, 6))
plt.plot(df['Dataset (Images per Alphabet)'], df['Accuracy'], marker='o')

# Add labels and title
plt.xlabel('Dataset (Images per Alphabet)')
plt.ylabel('Accuracy (%)')
plt.title('Accuracy vs. Dataset (Images per Alphabet)')

# Show the grid
plt.grid(True)

# Display the plot
plt.show()
