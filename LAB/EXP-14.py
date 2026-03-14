import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter
import re
# Load dataset
df = pd.read_csv(r"C:\Users\reddy\OneDrive\Desktop\EXPERIMENTS\data.csv")
# Combine feedback text
text = " ".join(df["feedback"])
# Convert to lowercase
text = text.lower()
# Remove punctuation
text = re.sub(r'[^\w\s]', '', text)
# Stop words
stop_words = ["the","and","is","in","to","of","for","on","with","a","an"]
# Remove stop words
words = [word for word in text.split() if word not in stop_words]
# Count frequency
word_freq = Counter(words)
# User input
N = int(input("Enter number of top frequent words: "))
# Top N words
top_words = word_freq.most_common(N)
# Display result
print("\nTop Frequent Words:")
for word, count in top_words:
    print(word, ":", count)
# Plot graph
w = [i[0] for i in top_words]
c = [i[1] for i in top_words]
plt.bar(w, c)
plt.xlabel("Words")
plt.ylabel("Frequency")
plt.title("Top Frequent Words in Feedback")
plt.show()
