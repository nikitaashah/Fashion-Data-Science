import matplotlib.pyplot as plt
import seaborn as sns

# Define the dominant colors and their proportions (excluding 'Other' for palette mapping)
dominant_colors = {
    "Red": 45,
    "Black": 25,
    "White": 15,
    "Gray": 10
}

# Define custom colors for plotting
color_palette = ["red", "black", "white", "gray"]

# Plot the color distribution as a bar chart
plt.figure(figsize=(8, 5))
sns.barplot(x=list(dominant_colors.keys()), y=list(dominant_colors.values()), palette=color_palette)
plt.xlabel("Colors")
plt.ylabel("Percentage")
plt.title("Dominant Colors in the Outfit")
plt.show()

# Pattern Frequency Visualization (Plaid detected)
pattern_data = {
    "Plaid/Grid": 1,
    "Stripes": 0,
    "Floral": 0,
    "Solid": 0
}

plt.figure(figsize=(6, 6))
plt.pie(pattern_data.values(), labels=pattern_data.keys(), autopct='%1.1f%%', colors=["red", "blue", "green", "gray"])
plt.title("Detected Pattern Frequency")
plt.show()

# Texture Classification Bar Chart
texture_classes = {
    "Smooth (Silk, Cotton)": 0,
    "Medium-textured (Wool, Polyester Blend)": 1,
    "Highly Textured (Tweed, Bouclé)": 0
}

plt.figure(figsize=(8, 5))
sns.barplot(x=list(texture_classes.keys()), y=list(texture_classes.values()), palette="Blues_r")
plt.xlabel("Texture Type")
plt.ylabel("Presence (1 = detected)")
plt.title("Texture Classification of Fabric")
plt.show()
