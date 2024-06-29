

### Chapter 3: Data Visualization and Preprocessing

#### 3.1 Data Exploration and Cleaning

In the initial phase of data exploration and cleaning, we gained an understanding of the dataset's structure and identified potential issues that needed to be addressed. By examining the dataset's dimensions, data types, and basic statistical properties, we could assess the quality and completeness of the data.

One crucial step in data cleaning was filtering the dataset to include only English language tweets. This was achieved by analyzing the distribution of tweet languages using a pie chart, as shown in the following figure:

![Pie chart of tweet languages](images/tweet_languages.png "Pie chart of tweet languages")

The pie chart clearly indicated that English was the dominant language in the dataset. To focus our analysis on English tweets, we subset the dataset by retaining only rows with the 'en' language code.

Additionally, we removed unnecessary columns that were not relevant to our analysis, such as 'User Profile Banner URL', 'User Description URLs', 'User URLs', and 'User Pinned Tweet IDs'. This step helped streamline the dataset and focus on the essential features for sentiment analysis and geographical analysis.

#### 3.2 Data Visualization

To gain insights into the dataset and identify potential patterns or trends, we employed various data visualization techniques. These visualizations not only aided in understanding the data but also served as a foundation for further analysis and interpretation.

1. **Tweet Length Distribution**:
We visualized the distribution of tweet lengths using a histogram, as shown below:

![Histogram of tweet lengths](images/tweet_length_distribution.png "Histogram of tweet lengths")

The histogram revealed that a significant portion of tweets in the dataset had lengths between 50 and 150 characters, which is typical for tweets on social media platforms. However, there were also instances of longer tweets, potentially indicating the presence of quoted or retweeted content.

2. **Tweet Count Over Time**:
To understand the temporal dynamics of the tweets, we plotted a line graph showing the tweet count over time:

![Line plot of tweet count over time](images/tweet_count_over_time.png "Line plot of tweet count over time")

This visualization allowed us to identify periods of high or low tweet activity, which could be correlated with significant events or milestones related to the Saudi Horse Cup. For example, we observed a peak in tweet activity around the dates when the event was likely taking place.

3. **Word Cloud of Hashtags**:
We generated a word cloud to visualize the most frequently used hashtags in the dataset:

![Word cloud of hashtags](images/hashtag_wordcloud.png "Word cloud of hashtags")

The word cloud provided insights into the popular topics, themes, or keywords associated with the Saudi Horse Cup event. Hashtags like "#SaudiHorseCup" and "#SaudiArabia" were prominently visible, indicating their widespread use in the conversation.

4. **Sentiment Distribution**:
After performing sentiment analysis using the TextBlob library, we visualized the distribution of sentiment labels (positive, negative, or neutral) using a pie chart:

![Pie chart of sentiment distribution](images/sentiment_distribution.png "Pie chart of sentiment distribution")

This analysis gave us an initial understanding of the overall sentiment towards the Saudi Horse Cup event. In the example shown, a significant portion of tweets were classified as positive, indicating a generally favorable sentiment towards the event.

5. **Sentiment Distribution by Language**:
To explore the potential variations in sentiment across different languages, we created a bar plot showing the sentiment distribution for each language present in the dataset:

![Bar plot of sentiment distribution by language](images/sentiment_by_language.png "Bar plot of sentiment distribution by language")

While our analysis focused on English tweets, this visualization could potentially reveal interesting differences in sentiment across languages, if multiple languages were present in the dataset.

6. **Sentiment vs. Retweet Count**:
We examined the relationship between sentiment and retweet count by plotting a scatter plot:

![Scatter plot of sentiment vs. retweet count](images/sentiment_vs_retweets.png "Scatter plot of sentiment vs. retweet count")

This analysis aimed to identify potential correlations between sentiment and the likelihood of a tweet being retweeted. In the example shown, there appears to be a slightly positive correlation, where more positive tweets tended to have higher retweet counts.

7. **Top Countries by User Count**:
To gain insights into the geographical distribution of users contributing to the Saudi Horse Cup conversation, we created a horizontal bar plot showing the top 10 countries by user count:

![Horizontal bar plot of top 10 countries by user count](images/top_countries_user_count.png "Horizontal bar plot of top 10 countries by user count")

This visualization provided valuable information about the geographical regions with the highest user engagement in the conversation, which could be useful for targeted analysis or marketing efforts.

8. **Top Users by Follower Count**:
We also analyzed the influential users in the dataset by plotting a bar chart of the top 10 users with the highest follower counts:

![Bar plot of top 10 users by follower count](images/top_users_follower_count.png "Bar plot of top 10 users by follower count")

This analysis could potentially reveal the presence of influential voices or opinion leaders in the Saudi Horse Cup discourse, whose tweets may have a significant impact on public perception and sentiment.

These visualizations provided valuable insights into the dataset, enabling us to identify potential patterns, trends, and outliers. The findings from this data visualization phase informed our subsequent data preprocessing steps and guided the development of our sentiment analysis and geographical analysis approaches.

#### 3.3 Data Preprocessing

Effective data preprocessing is crucial for achieving accurate and reliable results in any data analysis task. In this study, we performed several preprocessing steps to ensure the quality and consistency of the dataset.

1. **Standardizing Column Names**:
To maintain a consistent and readable format, we standardized the column names in the dataset by converting them to lowercase and replacing spaces with underscores. This step ensured that the column names were machine-readable and followed a consistent naming convention.

2. **Handling Missing Values**:
We inspected the dataset for missing values and addressed them using appropriate techniques, such as imputation or removal, depending on the nature and extent of the missing data. Missing values can introduce bias and lead to inaccurate results, so it was essential to handle them appropriately.

3. **Text Preprocessing**:
Since our analysis focused on textual data, we applied various text preprocessing techniques to enhance the quality and consistency of the tweet text. These techniques included:
   - Tokenization: Breaking down the text into individual words or tokens.
   - Lowercase conversion: Converting all text to lowercase for consistency.
   - Removing special characters: Eliminating unnecessary special characters or symbols that may introduce noise in the analysis.
   - Stemming or lemmatization: Reducing words to their root forms to improve the accuracy of text analysis.
   - Stop word removal: Eliminating common words (e.g., "the," "and," "is") that do not contribute significantly to the sentiment analysis.

4. **Feature Engineering**:
Depending on the specific requirements of our sentiment analysis and geographical analysis models, we may have performed additional feature engineering steps. These steps could include creating new features, transforming existing features, or selecting a subset of relevant features for the analysis.

By implementing these data preprocessing techniques, we aimed to enhance the quality and consistency of the dataset, ensuring that it was optimally prepared for the subsequent stages of sentiment analysis and geographical analysis.

#### 3.4 Data Sampling and Balancing

In some cases, the collected dataset may be imbalanced, with a disproportionate representation of certain sentiment categories (e.g., a higher number of positive or negative tweets). To address this issue and ensure reliable model training and evaluation, we employed appropriate data sampling and balancing techniques.

1. **Undersampling**:
If the dataset had a significantly larger number of instances from one sentiment category, we could employ undersampling techniques to reduce the size of the majority class. This involved randomly selecting a subset of instances from the majority class to achieve a more balanced distribution.

2. **Oversampling**:
Alternatively, if the dataset had a small number of instances from certain sentiment categories, we could apply oversampling techniques to increase the representation of these minority classes. This could involve duplicating or generating synthetic instances of the minority classes through techniques like the Synthetic Minority Over-sampling Technique (SMOTE).

3. **Stratified Sampling**:
To ensure that the sampling process preserved the overall distribution of sentiment categories, we employed stratified sampling techniques. This approach ensured that the relative proportions of each sentiment category were maintained in both the training and testing datasets.

By addressing potential class imbalances and ensuring a balanced representation of sentiment categories, we aimed to improve the performance and generalization capabilities of our sentiment analysis models, as well as reduce the risk of biased or skewed results.

The data visualization, preprocessing, and sampling steps described in this chapter laid a solid foundation for the subsequent sentiment analysis and geographical analysis phases of our study. By carefully curating and preparing the dataset, we aimed to derive meaningful insights an
