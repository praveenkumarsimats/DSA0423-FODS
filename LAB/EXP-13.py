import pandas as pd
from collections import Counter
import re

# Sample dataset (replace with your actual dataset)
data = {
    'review': [
        "This product is very good",
        "Good quality and good service",
        "Very bad experience",
        "Product quality is good"
    ]
}

df = pd.DataFrame(data)

# Combine all reviews into one text
all_reviews = " ".join(df['review'])

# Convert to lowercase and remove special characters
clean_text = re.sub(r'[^a-zA-Z ]', '', all_reviews.lower())

# Split into words
words = clean_text.split()

# Count word frequency
word_freq = Counter(words)

# Convert to DataFrame for better display
freq_df = pd.DataFrame(word_freq.items(), columns=['Word', 'Frequency'])
freq_df = freq_df.sort_values(by='Frequency', ascending=False)

print(freq_df)
