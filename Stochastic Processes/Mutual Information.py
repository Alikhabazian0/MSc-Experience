from scipy.stats import entropy
import numpy as np

def mutual_information(variable1, variable2):
    # Calculate the joint probability distribution
    joint_prob = np.histogram2d(variable1, variable2, bins=(np.unique(variable1), np.unique(variable2)))[0]
    joint_prob /= np.sum(joint_prob)

    # Calculate marginal probability distributions
    marginal_prob_var1 = np.sum(joint_prob, axis=1)
    marginal_prob_var2 = np.sum(joint_prob, axis=0)

    # Calculate entropies
    entropy_var1 = entropy(marginal_prob_var1)
    entropy_var2 = entropy(marginal_prob_var2)
    joint_entropy_val = entropy(joint_prob.flatten())

    # Calculate mutual information
    mutual_info = entropy_var1 + entropy_var2 - joint_entropy_val
    return mutual_info

# Assuming you have loaded data02, data05, and data08 from your files
print(f"Mutual Information between 0.2.txt and 0.5.txt: {mutual_information(data02, data05)}")
print(f"Mutual Information between 0.8.txt and 0.5.txt: {mutual_information(data08, data05)}")
print(f"Mutual Information between 0.2.txt and 0.8.txt: {mutual_information(data02, data08)}")
