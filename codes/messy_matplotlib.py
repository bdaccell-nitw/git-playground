import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# test data
np.random.seed(42)
x = np.linspace(0, 10, 100)
y = np.sin(x) + np.random.normal(0, 0.2, 100)
df = pd.DataFrame({'x': x, 'y': y, 'group': np.random.choice(['grpA','grpB','grpC'], 100)})

# === TASK 1: Create a proper figure and axis object ===
# Replace None with correct syntax
# Expected: Figure with single axis, size 10x5
fig, ax = None  

# === TASK 2: Plot a line with proper styling ===
# Expected: Blue dashed line with legend label "Sine Wave"
# ax.plot(None)

# === TASK 3: Add proper axis labels and title ===
# Replace None with correct syntax
ax.set(None) 

# === TASK 4: Add a legend at best location ===
ax.legend(None)

# === TASK 5: Create a professional scatter plot ===
# Expected: Color by 'group' column, add colorbar and viridis colormap

scatter = ax.scatter(
    x=df['x'],
    y=df['y'],
)
plt.colorbar(None)  

# === TASK 6: Save plot as high-quality PNG ===
#Uncomment the line below and call the right function
#fig._______  

# === TASK 7: Create subplots properly ===
# Expected: 2x1 grid of plots
# Replace None with correct syntax
fig, axes = None  
axes[0].plot(x, y)
axes[1].scatter(x, y)