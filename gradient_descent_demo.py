"""
# Interactive Gradient Descent Demo for Google Colab

## 🚀 Quick Start Guide

### Step 1: Open Google Colab
1. Go to [Google Colab](https://colab.research.google.com)
2. Click **File → New Notebook**

### Step 2: Copy and Run the Code
1. Copy the entire contents of `gradient_descent_demo.py`
2. Paste it into a code cell in your Colab notebook
3. Click the **Play button** (▶️) or press **Shift+Enter**

### Step 3: Interact!
Interactive sliders will appear below the code. Adjust them to explore:
- **Start Position**: Where the algorithm begins
- **Learning Rate**: Size of each step
- **Iterations**: How many steps to take
- **Function Type**: Different optimization landscapes

---

## 📖 Teaching Guide for Medics

### Concept Overview
Gradient descent is the fundamental optimization algorithm used in machine learning, including:
- Training neural networks for medical image analysis
- Optimizing treatment protocols
- Fitting statistical models to patient data

### Real-World Medical Analogy
Think of gradient descent like adjusting medication dosage:
- **Cost Function**: Patient symptoms (we want to minimize)
- **Parameter**: Medication dosage
- **Gradient**: How symptoms change with dosage
- **Learning Rate**: How aggressively we adjust the dose
- **Iterations**: Follow-up appointments

### Key Concepts to Demonstrate

#### 1. **Starting Position Matters**
- Try starting at x = -5, then x = 5
- Both should reach the same minimum (for quadratic function)
- In complex functions, different starts may reach different local minima

#### 2. **Learning Rate is Critical**
- **Too small (0.01)**: Slow convergence, many iterations needed
- **Just right (0.1)**: Smooth, efficient descent
- **Too large (0.4+)**: Oscillation or divergence (overshooting)

#### 3. **Iterations and Convergence**
- Watch the right plot: Cost should decrease
- After enough iterations, cost plateaus (convergence)
- More iterations ≠ better if already converged

#### 4. **Function Complexity**
- **Quadratic**: Simple, one global minimum (most medical models)
- **Complex**: Multiple local minima (challenging optimization)
- **Noisy**: Realistic with measurement noise

---

## 🎓 Suggested Exercises

### Exercise 1: Finding the Sweet Spot
1. Set start position to 3
2. Try learning rates: 0.01, 0.1, 0.3, 0.5
3. Question: What learning rate works best? Why?

### Exercise 2: The Overshoot Problem
1. Set learning rate to 0.5
2. Set iterations to 50
3. Observe: Does it converge or bounce around?

### Exercise 3: Local vs Global Minima
1. Switch to 'complex' function
2. Try starting positions: -3, 0, 3
3. Question: Do all starting points reach the same minimum?

### Exercise 4: Real Data Application
Ask students to think: "If this were a model predicting patient readmission risk, what would each component represent?"

---

## 🔧 Troubleshooting

### "No module named 'ipywidgets'"
Google Colab should have this installed. If not, add this cell before the main code:
```python
!pip install ipywidgets
```

### Sliders Don't Appear
- Make sure you ran the entire cell
- Try Runtime → Restart Runtime, then run again

### Want to Start Over?
- Just run the cell again
- Or adjust the sliders to reset

---

## 📊 What the Plots Show

### Left Plot: The Optimization Landscape
- **Blue curve**: The cost function we're trying to minimize
- **Red line with dots**: Path taken by gradient descent
- **Green circle**: Starting position
- **Red star**: Final position found

### Right Plot: Learning Progress
- **X-axis**: Iteration number
- **Y-axis**: Cost value
- Shows how quickly the algorithm improves
- Flat line at the end = convergence

---

## 💡 Discussion Points for Class

1. **Why is this important in medicine?**
   - Drug discovery optimization
   - Medical image segmentation
   - Predicting patient outcomes
   - Personalizing treatment plans

2. **What could go wrong?**
   - Wrong learning rate → poor convergence
   - Local minima → suboptimal solution
   - Too few iterations → incomplete training

3. **How does this relate to AI in healthcare?**
   - Neural networks use gradient descent to learn from data
   - Every AI medical diagnostic tool was trained this way
   - Understanding this helps interpret AI decisions

---

## 🎯 Key Takeaways

✅ Gradient descent finds the minimum of a function by following the slope downward

✅ Learning rate controls step size: too big = unstable, too small = slow

✅ Different starting points can lead to different solutions in complex landscapes

✅ This algorithm powers most modern machine learning, including medical AI

✅ Understanding optimization helps interpret and trust AI medical tools

---

## 📚 Next Steps

After mastering this demo, students can explore:
- Stochastic gradient descent (used with real data)
- Momentum and adaptive learning rates
- Applying gradient descent to real medical datasets
- Understanding deep learning optimization

---

## ❓ Common Questions

**Q: Is gradient descent always guaranteed to find the best solution?**  
A: Only for convex functions (like the quadratic). For complex functions, it might find a local minimum instead of the global minimum.

**Q: How is this used in real medical AI?**  
A: When training a neural network to read X-rays, gradient descent adjusts millions of parameters to minimize diagnostic errors.

**Q: What if the function is very noisy?**  
A: Try the 'noisy' function type to see! In practice, we use techniques like mini-batch gradient descent and momentum.

**Q: Can we use this for multiple parameters?**  
A: Yes! This demo shows 1D for visualization, but real models optimize thousands or millions of parameters simultaneously.

Interactive Gradient Descent Demonstration for Google Colab
Perfect for teaching medics with minimal Python experience
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from IPython.display import HTML, display
import ipywidgets as widgets
from ipywidgets import interact, interactive, fixed, interact_manual

# Set up plotting style
plt.style.use('seaborn-v0_8-darkgrid')

class GradientDescentDemo:
    """Interactive demonstration of gradient descent optimization"""
    
    def __init__(self):
        self.history = []
        
    def cost_function(self, x, function_type='quadratic'):
        """Different cost functions to demonstrate gradient descent"""
        if function_type == 'quadratic':
            return x**2 + 2*x + 1  # Simple parabola
        elif function_type == 'complex':
            return 0.1*x**4 - 0.5*x**3 + x**2 + 2*x + 1  # More complex landscape
        elif function_type == 'noisy':
            return x**2 + 2*x + 1 + 0.5*np.sin(5*x)  # Noisy quadratic
        
    def gradient(self, x, function_type='quadratic'):
        """Compute the gradient (derivative) of the cost function"""
        if function_type == 'quadratic':
            return 2*x + 2
        elif function_type == 'complex':
            return 0.4*x**3 - 1.5*x**2 + 2*x + 2
        elif function_type == 'noisy':
            return 2*x + 2 + 2.5*np.cos(5*x)
    
    def run_gradient_descent(self, start_x, learning_rate, n_iterations, function_type='quadratic'):
        """Run gradient descent and store the path"""
        x = start_x
        self.history = [(x, self.cost_function(x, function_type))]
        
        for i in range(n_iterations):
            # Compute gradient
            grad = self.gradient(x, function_type)
            
            # Update x using gradient descent rule: x_new = x_old - learning_rate * gradient
            x = x - learning_rate * grad
            
            # Store history
            self.history.append((x, self.cost_function(x, function_type)))
        
        return x
    
    def plot_descent(self, start_x, learning_rate, n_iterations, function_type='quadratic'):
        """Create an interactive plot showing the gradient descent process"""
        # Run gradient descent
        final_x = self.run_gradient_descent(start_x, learning_rate, n_iterations, function_type)
        
        # Create the plot
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 6))
        
        # Plot 1: Cost function with descent path
        x_range = np.linspace(-5, 5, 300)
        y_range = self.cost_function(x_range, function_type)
        
        ax1.plot(x_range, y_range, 'b-', linewidth=2, label='Cost Function')
        
        # Plot the path taken by gradient descent
        path_x = [point[0] for point in self.history]
        path_y = [point[1] for point in self.history]
        
        ax1.plot(path_x, path_y, 'ro-', markersize=8, linewidth=2, 
                alpha=0.7, label='Gradient Descent Path')
        ax1.plot(path_x[0], path_y[0], 'go', markersize=15, 
                label='Start', zorder=5)
        ax1.plot(path_x[-1], path_y[-1], 'r*', markersize=20, 
                label='Final Position', zorder=5)
        
        ax1.set_xlabel('Parameter Value (x)', fontsize=12, fontweight='bold')
        ax1.set_ylabel('Cost', fontsize=12, fontweight='bold')
        ax1.set_title(f'Gradient Descent Visualization\nFinal x = {final_x:.3f}', 
                     fontsize=14, fontweight='bold')
        ax1.legend(fontsize=10)
        ax1.grid(True, alpha=0.3)
        
        # Plot 2: Cost over iterations
        iterations = list(range(len(self.history)))
        costs = [point[1] for point in self.history]
        
        ax2.plot(iterations, costs, 'b-o', linewidth=2, markersize=6)
        ax2.set_xlabel('Iteration', fontsize=12, fontweight='bold')
        ax2.set_ylabel('Cost', fontsize=12, fontweight='bold')
        ax2.set_title('Cost Reduction Over Time', fontsize=14, fontweight='bold')
        ax2.grid(True, alpha=0.3)
        
        # Add text with final statistics
        initial_cost = costs[0]
        final_cost = costs[-1]
        improvement = ((initial_cost - final_cost) / initial_cost) * 100
        
        stats_text = f'Initial Cost: {initial_cost:.3f}\nFinal Cost: {final_cost:.3f}\nImprovement: {improvement:.1f}%'
        ax2.text(0.98, 0.97, stats_text, transform=ax2.transAxes,
                fontsize=11, verticalalignment='top', horizontalalignment='right',
                bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))
        
        plt.tight_layout()
        plt.show()
        
        # Print summary
        print("\n" + "="*60)
        print("GRADIENT DESCENT SUMMARY")
        print("="*60)
        print(f"Starting position: x = {path_x[0]:.3f}")
        print(f"Final position: x = {final_x:.3f}")
        print(f"Number of iterations: {n_iterations}")
        print(f"Learning rate: {learning_rate}")
        print(f"Cost improvement: {improvement:.1f}%")
        print("="*60)

# Create the demo instance
demo = GradientDescentDemo()

# Create interactive widgets
print("="*70)
print(" INTERACTIVE GRADIENT DESCENT DEMONSTRATION ".center(70, "="))
print("="*70)
print("\n📚 WHAT IS GRADIENT DESCENT?")
print("-" * 70)
print("Gradient descent is like walking down a hill to find the lowest point.")
print("In machine learning, we use it to find the best parameters for our model.")
print("\n🎯 HOW IT WORKS:")
print("1. Start at some position on the hill (initial parameter)")
print("2. Look at the slope (gradient) - which way is down?")
print("3. Take a step downhill (update parameter)")
print("4. Repeat until you reach the bottom (minimum cost)")
print("\n🎮 INTERACTIVE CONTROLS:")
print("-" * 70)
print("• START POSITION: Where we begin on the curve")
print("• LEARNING RATE: How big each step is (too big = overshoot, too small = slow)")
print("• ITERATIONS: How many steps we take")
print("• FUNCTION TYPE: Different landscapes to explore")
print("="*70)
print("\n")

# Create the interactive interface
interact(demo.plot_descent,
         start_x=widgets.FloatSlider(value=3, min=-5, max=5, step=0.5, 
                                     description='Start Position:', 
                                     style={'description_width': 'initial'}),
         learning_rate=widgets.FloatSlider(value=0.1, min=0.01, max=0.5, step=0.01, 
                                          description='Learning Rate:', 
                                          style={'description_width': 'initial'}),
         n_iterations=widgets.IntSlider(value=20, min=5, max=50, step=5, 
                                       description='Iterations:', 
                                       style={'description_width': 'initial'}),
         function_type=widgets.Dropdown(options=['quadratic', 'complex', 'noisy'],
                                       value='quadratic',
                                       description='Function Type:',
                                       style={'description_width': 'initial'}))

print("\n💡 TIPS FOR EXPLORATION:")
print("-" * 70)
print("1. Try different starting positions - does it always find the minimum?")
print("2. Increase learning rate - what happens when it's too large?")
print("3. Decrease learning rate - what happens when it's too small?")
print("4. Try the 'complex' function to see multiple local minima")
print("5. Watch how the cost decreases over iterations")
print("="*70)
