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

import csv
import os
from datetime import datetime

async def main():
    api = API("accounts.db")

    # Initialize CSV file
    csv_file_path = 'new.csv'
    fieldnames = [
        'id',   'created_at', 'lang', 'text', 'reply_count',   'hashtags','view_count', 'user_id', 'user_username', 'user_screen_name','user_followers_count', 'user_location'
   
    ]

    with open(csv_file_path, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        query = '#SaudiCup   since:2024-01-1  lang:en'

        # query = '#SaudiCup   since:2024-02-20 until:2024-03-05 lang:en'
        async for tweet in api.search(query,  limit=5000):
            tweet_data = {
                'id': tweet.id,
               
             
                'created_at': tweet.date.isoformat(),
                'lang': tweet.lang,
                'text': tweet.rawContent,
                'reply_count': tweet.replyCount,
             
                'like_count': tweet.likeCount,
            
                'hashtags': ','.join(tweet.hashtags),
              
                'view_count': tweet.viewCount,
            
                'user_id': tweet.user.id,
                'user_username': tweet.user.username,
                'user_screen_name': tweet.user.displayname,
              
                'user_followers_count': tweet.user.followersCount,
              
                'user_location': tweet.user.location,
             
            }
            writer.writerow(tweet_data)
       

    set_log_level("DEBUG")

if __name__ == "__main__":
    asyncio.run(main())