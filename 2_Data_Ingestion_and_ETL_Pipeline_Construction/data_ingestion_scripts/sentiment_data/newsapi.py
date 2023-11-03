from newsapi import NewsApiClient
import pandas as pd
from dotenv import load_dotenv
import os


# Load environment variables from .env file
load_dotenv()

# Access environment variables
news_api_key = os.getenv('NEWS_API_KEY')


def fetch_news():
    # Initialize the client
    newsapi = NewsApiClient(api_key='news_api_key')

    # Fetch news articles about Apple Inc.
    articles = newsapi.get_everything(q='Apple Inc',
                                      from_param='2023-10-03',
                                      to='2023-11-01',
                                      language='en',
                                      sort_by='relevancy')

    # Convert the articles to a DataFrame
    df = pd.DataFrame(articles['articles'])

    # Save the DataFrame to a CSV file
    df.to_csv('apple_news.csv', index=False)

if __name__ == "__main__":
    fetch_news()
