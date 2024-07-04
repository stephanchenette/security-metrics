import numpy as np

def calculate_detection_probability(technology_prob, people_prob, process_prob):
    # Ensure probabilities are between 0 and 1
    if not (0 <= technology_prob <= 1) or not (0 <= people_prob <= 1) or not (0 <= process_prob <= 1):
        raise ValueError("Probabilities must be between 0 and 1")

    # Calculate overall detection probability
    overall_prob = 1 - (1 - technology_prob) * (1 - people_prob) * (1 - process_prob)
    return overall_prob

# Example probabilities
technology_prob = 0.8  # 80% chance technology detects the event
people_prob = 0.6      # 60% chance people detect the event if technology fails
process_prob = 0.7     # 70% chance process detects the event if technology and people fail

# Calculate overall detection probability
overall_detection_probability = calculate_detection_probability(technology_prob, people_prob, process_prob)

print(f"Overall Detection Probability: {overall_detection_probability:.2f}")

# Simulating different scenarios
technology_probs = np.linspace(0.5, 1, 10)
people_probs = np.linspace(0.5, 1, 10)
process_probs = np.linspace(0.5, 1, 10)

results = []

for t_prob in technology_probs:
    for p_prob in people_probs:
        for r_prob in process_probs:
            prob = calculate_detection_probability(t_prob, p_prob, r_prob)
            results.append((t_prob, p_prob, r_prob, prob))

# Display results
import pandas as pd

df = pd.DataFrame(results, columns=['Technology Probability', 'People Probability', 'Process Probability', 'Overall Probability'])
import ace_tools as tools; tools.display_dataframe_to_user(name="Detection Probability Scenarios", dataframe=df)

# Save results to a file
df.to_csv("detection_probability_scenarios.csv", index=False)
