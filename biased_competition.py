
# Neuron activation in response to two competing objects 

Neuron = { 
    'Preference_for_red': 7,
    'Preference_for_green': 10
}


Object1 = { 
    'Salience': 8,
    'Color' : 'red'
}

Object2 = {
    'Salience': 8,
    'Color' : 'green'
}

Excitatory_Drive1 = ( Neuron['Preference_for_red'] * Object1['Salience'] ) #56.0 #red
Excitatory_Drive2 = ( Neuron['Preference_for_green'] * Object2['Salience'] ) #80.0 #green


def compute_competition(Excitatory_Drive1, Excitatory_Drive2, Attention_weight_red, Attention_weight_green):
    sigma = 10.0
    weighted_red = Excitatory_Drive1 * Attention_weight_red
    weighted_green = Excitatory_Drive2 * Attention_weight_green
    total = weighted_red + weighted_green + sigma

    Response_red = weighted_red / total
    Response_green = weighted_green / total
    return Response_red, Response_green
# Divisive normalization simulates lateral inhibition

Activation_red, Activation_green = compute_competition(Excitatory_Drive1, Excitatory_Drive2, 0.7, 0.3)

print ("Neuron's firing rate for red object: ", Activation_red)
print ("Neuron's firing rate for green object: ", Activation_green)

if Activation_red > Activation_green:
     print ("Winner: Red object")
else :
     print ('Winner : Green object') 



import matplotlib.pyplot as plt

# Plotting the results
objects = ['Red Object', 'Green Object']
activations = [Activation_red, Activation_green]
colors = ['red', 'green']

plt.pie(activations,
         labels=objects,
           autopct='%1.1f%%', 
           startangle=140, 
           colors=colors, explode=(0.1,0),shadow=True)

plt.title("Neuron's Activation for Competing Objects")
plt.axis('equal')
plt.show()