
Note:
that Twitter has changed its name to Platform X.
I want the report to look like an academic writer so that it cannot be verified that it was written by an AI.

Purpose

The purpose of this project is to analyze global sentiment and reactions towards the Saudi Horse Cup by collecting and classifying Twitter comments. This will help in understanding the event’s impact, identifying prevailing opinions, and examining how these sentiments vary geographically. By training an AI model on this data, we aim to categorize the sentiments into negative, positive, or neutral, providing insights into public perception.



# The World’s Opinions on the Saudi Cup



## Index

### Chapter 1: Introduction
1.1 Project Overview  
1.2 Saudi Horse Cup
1.3 Objectives  
1.4 Scope of the Study  
1.4 Significance of the Study  

### Chapter 2: Data Collection
2.1 Data Sources  
2.2 Data Collection Methods  
2.3 Twitter API Integration  
2.4 Data Sampling Strategy  
2.5 Ethical Considerations  

### Chapter 3: Data Visualization and Preprocessing
3.1 Data Exploration and Cleaning
3.2 Data Visualization  
3.3 Data Preprocessing
3.4 Data Sampling and Balancing
 

### Chapter 4: Sentiment Analysis
4.1 Sentiment Analysis Overview  
4.2 Model Selection  
4.3 Training the Sentiment Analysis Model  
4.4 Model Evaluation  
4.5 Sentiment Categorization  


### Chapter 6: Conclusion and Future Work
6.1 Summary of Findings  
6.2 Implications of the Study  
6.3 Limitations  
6.4 Recommendations for Future Research  
6.5 Closing Remarks  

### References

### Appendices
A.1 Code Samples and Scripts  
A.2 Data Dictionary  
A.3 Glossary of Terms


































i am write this code in  Visualization and Preprocessing

"""## **Data Visualization and Preprocessing**

"""



import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from textblob import TextBlob
from wordcloud import WordCloud


df = pd.read_csv('/content/tweets5000Latest (2).csv')

df.head()

df.describe()

df.dtypes

# Data Visualization : Pie chart of tweet languages
lang_counts = df['lang'].value_counts()
plt.figure(figsize=(8, 8))
plt.pie(lang_counts, labels=lang_counts.index, autopct='%1.1f%%')
plt.title('Tweet Languages')
plt.show()

# Data Preprocessing: Keep only English language tweets
df = df[df['lang'] == 'en']
lang_counts = df['lang'].value_counts()
plt.figure(figsize=(8, 8))
plt.pie(lang_counts, labels=lang_counts.index, autopct='%1.1f%%')
plt.title('Tweet Languages')
plt.show()

# Removing unnecessary columns
columns_to_drop = ['User Profile Banner URL', 'User Description URLs', 'User URLs', 'User Pinned Tweet IDs']
df = df.drop(columns=columns_to_drop, axis=1)

#  Histogram of tweet lengths
tweet_lengths = df['text'].str.len()
plt.figure(figsize=(10, 6))
plt.hist(tweet_lengths, bins=20)
plt.xlabel('Tweet Length')
plt.ylabel('Frequency')
plt.title('Distribution of Tweet Lengths')
plt.show()

#  Line plot of tweet count over time
df['created_at_datetime'] = pd.to_datetime(df['created_at_datetime'])
tweet_counts = df.resample('D', on='created_at_datetime').size()
plt.figure(figsize=(12, 6))
plt.plot(tweet_counts.index, tweet_counts)
plt.xlabel('Date')
plt.ylabel('Tweet Count')
plt.title('Tweet Count Over Time')
plt.xticks(rotation=45)
plt.show()

#  Word cloud of hashtags
from wordcloud import WordCloud

hashtags = df['hashtags'].str.cat(sep=' ')
wordcloud = WordCloud(width=800, height=400, background_color='white').generate(hashtags)
plt.figure(figsize=(12, 6))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.title('Word Cloud of Hashtags')
plt.show()

# Perform sentiment analysis using TextBlob
df['sentiment'] = df['text'].apply(lambda x: TextBlob(x).sentiment.polarity)
df['sentiment_label'] = df['sentiment'].apply(lambda x: 'Positive' if x > 0 else ('Negative' if x < 0 else 'Neutral'))

# Data Visualization : Pie chart of sentiment distribution
sentiment_counts = df['sentiment_label'].value_counts()
plt.figure(figsize=(8, 8))
plt.pie(sentiment_counts, labels=sentiment_counts.index, autopct='%1.1f%%')
plt.title('Sentiment Distribution')
plt.show()

#  Bar plot of sentiment distribution by language
language_sentiment = df.groupby(['lang', 'sentiment_label']).size().unstack()
language_sentiment.plot(kind='bar', figsize=(12, 6))
plt.xlabel('Language')
plt.ylabel('Count')
plt.title('Sentiment Distribution by Language')
plt.legend(title='Sentiment')
plt.xticks(rotation=45)
plt.show()

# Data Visualization : Scatter plot of sentiment vs. retweet count
plt.figure(figsize=(10, 6))
plt.scatter(df['sentiment'], df['retweet_count'], alpha=0.5)
plt.xlabel('Sentiment')
plt.ylabel('Retweet Count')
plt.title('Sentiment vs. Retweet Count')
plt.show()

# Standardize column names
df.columns = df.columns.str.lower().str.replace(' ', '_')

# Data Visualization : Horizontal bar plot of top 10 countries by user count
user_country_counts = df['user_location'].value_counts().nlargest(10)
plt.figure(figsize=(10, 8))
plt.barh(user_country_counts.index, user_country_counts)
plt.xlabel('Number of Users')
plt.ylabel('Country')
plt.title('Top 10 Countries by User Count')
plt.show()

# Data Visualization : Bar plot of top 10 users by follower count
top_users = df.nlargest(10, 'user_followers_count')
plt.figure(figsize=(12, 6))
plt.bar(top_users['user_screen_name'], top_users['user_followers_count'])
plt.xlabel('User Screen Name')
plt.ylabel('Followers Count')
plt.title('Top 10 Users by Follower Count')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()



Now I want to write the report in the third chapter
plrase explain  explaining the results and explaining the diagrams.
in ur anwser suppose images like :
make ![alt text for screen readers](images/diagram.png "Text to show on mouseover").








Explain that the previous sensitivity classification was done by the Twitter platform and that another classification will now be done using bert, then explain why this is so.

### Chapter 5: Sentiment Analysis
5.1 Sentiment Analysis Overview  
5.2 Model Selection  
5.3 Training the Sentiment Analysis Model  
5.4 Model Evaluation  
5.5 Sentiment Categorization  