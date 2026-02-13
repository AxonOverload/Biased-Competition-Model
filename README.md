# Biased-Competition-Model
Computational model of visual attention and biased competition

# Usage : run the script to see a pie chart visualization of the competition outcome


This model simulates how top-down signals from the prefrontal cortex (PFC) override bottom-up drives and neuronal preferences. It showcases how the Pulvinar modulates V4 activity by sending alpha-wave signals, which are triggered by goal-directed instructions from the PFC.
The code demonstrates how attending to the color red makes the neuron more likely to fire in response to the red object rather than the green object.
This works by mutual suppression in the neuron, where each object supresses the other according to the top down signals the neuron receives.
(by using Divisive Normalization)

The code demonstrates how attending to a specific feature (e.g., the color red) biases the neuron to fire in response to the red object over the green one. This is achieved through mutual suppression and divisive normalization, where top-down signals determine which stimulus the neuron prioritizes.

# Based on :
Dismone & Duncan (1995) - Biased competition theory
Heeger (1992) - Divisive normalization
Reynolds et al. (1999) - V4 attention mechanisms

