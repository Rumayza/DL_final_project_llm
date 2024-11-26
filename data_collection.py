import os
import requests
from bs4 import BeautifulSoup
import wikipediaapi
import zipfile
import io
import tarfile

def download_articles():
    articles_dir = "data/articles"
    os.makedirs(articles_dir, exist_ok=True)
    urls = [
        "https://www.bbc.com/news/technology-61262269",
        "https://www.bbc.com/news/world-asia-57268111",
        "https://edition.cnn.com/2023/03/20/tech/ai-ethics-explained/index.html",
        "https://www.theguardian.com/science/2023/mar/01/artificial-intelligence-research-ethics",
        "https://www.theguardian.com/world/2023/may/01/the-rise-of-ai-international-impacts",
        "https://www.nytimes.com/2023/03/15/technology/ai-chatbots-ethics.html",
        "https://www.nytimes.com/2023/04/25/science/artificial-intelligence-impacts.html",
        "https://www.forbes.com/sites/bernardmarr/2023/05/10/the-impact-of-ai-on-education/",
        "https://www.forbes.com/sites/forbestechcouncil/2023/05/05/top-ai-tools-you-should-know/",
        "https://www.wired.com/story/ai-research-moral-conundrums/",
        "https://www.wired.com/story/the-future-of-technology/",
        "https://www.reuters.com/technology/artificial-intelligence-threatens-human-jobs-2023-05-10/",
        "https://www.reuters.com/science/ethics-technology-and-artificial-intelligence-2023-04-20/",
        "https://www.scientificamerican.com/article/artificial-intelligence-and-climate-change/",
        "https://www.scientificamerican.com/article/ai-and-space-exploration-2023/",
        "https://techcrunch.com/2023/05/01/ai-and-healthcare-new-frontiers/",
        "https://techcrunch.com/2023/04/15/ai-and-automation-threats-to-jobs/",
        "https://www.aljazeera.com/news/2023/05/01/the-role-of-ai-in-modern-conflicts/",
        "https://www.aljazeera.com/news/2023/05/10/how-ai-is-transforming-education-worldwide/",
        "https://www.bbc.com/news/world-us-canada-57268119"
    ]
    for i, url in enumerate(urls):
        response = requests.get(url)
        with open(f"{articles_dir}/article_{i + 1}.txt", "w", encoding="utf-8") as file:
            soup = BeautifulSoup(response.text, "html.parser")
            file.write(soup.get_text())
    print("Articles downloaded successfully.")

def download_books():
    books_dir = "data/books"
    os.makedirs(books_dir, exist_ok=True)
    book_urls = [
        "https://www.gutenberg.org/files/1342/1342-0.txt",  # Pride and Prejudice
        "https://www.gutenberg.org/files/84/84-0.txt",      # Frankenstein
        "https://www.gutenberg.org/files/11/11-0.txt",      # Alice's Adventures in Wonderland
        "https://www.gutenberg.org/files/1080/1080-0.txt",  # A Modest Proposal
        "https://www.gutenberg.org/files/74/74-0.txt"       # The Adventures of Tom Sawyer
    ]
    for i, url in enumerate(book_urls):
        response = requests.get(url)
        with open(f"{books_dir}/book_{i + 1}.txt", "w", encoding="utf-8") as file:
            file.write(response.text)
    print("Books downloaded successfully.")

def download_wikipedia_articles():
    import requests
    import wikipediaapi

    wiki_dir = "data/wikipedia"
    os.makedirs(wiki_dir, exist_ok=True)

    # Specify a proper user agent according to Wikipedia's policy
    user_agent = "CoolBot/0.0 (https://github.com/Rumayza; rumayza.n@gmail.com)"
    
    wiki_wiki = wikipediaapi.Wikipedia(
        language='en',
        extract_format=wikipediaapi.ExtractFormat.WIKI,
        user_agent=user_agent
    )

    topics = [
        "Artificial intelligence", "Machine learning", "Deep learning", "Natural language processing",
        "Reinforcement learning", "Computer vision", "ChatGPT", "Neural networks",
        "Data science", "Big data", "Technology ethics", "Quantum computing", "Cybersecurity",
        "Self-driving cars", "Automation", "Internet of Things", "Digital transformation", "Cloud computing",
        "Space exploration", "Renewable energy", "Climate change", "Global warming", "Sustainable development",
        "Health technology", "Vaccines", "Mental health", "COVID-19", "Blockchain technology", "Cryptocurrency",
        "Economic policies", "E-commerce", "Digital privacy", "Education technology", "Social media",
        "Robotics", "Mars exploration", "Satellite technology", "3D printing", "Smart cities",
        "Genomics", "Biotechnology", "Agricultural technology", "Fossil fuels", "Nuclear energy",
        "Philosophy of AI", "Ethics in AI", "History of computing", "Evolution of the internet",
        "Hacking and cybersecurity", "Augmented reality", "Virtual reality", "Biometrics"
    ]

    for i, topic in enumerate(topics):
        page = wiki_wiki.page(topic)
        if page.exists():
            with open(f"{wiki_dir}/wiki_{i + 1}.txt", "w", encoding="utf-8") as file:
                file.write(page.text)
    print("Wikipedia articles downloaded successfully.")


import os
import subprocess

def download_custom_dataset():
    """
    Downloads the Hacker News dataset from Kaggle and extracts it into the `data/custom` folder.
    """
    custom_dir = "data/custom"
    os.makedirs(custom_dir, exist_ok=True)

    try:
        subprocess.run(["pip", "install", "kaggle"], check=True)

        # Download the dataset using Kaggle API
        print("Downloading dataset from Kaggle...")
        subprocess.run(
            [
                "kaggle",
                "datasets",
                "download",
                "-d",
                "hacker-news/hacker-news-posts",
                "-p",
                custom_dir
            ],
            check=True
        )

        dataset_zip = os.path.join(custom_dir, "hacker-news-posts.zip")
        with zipfile.ZipFile(dataset_zip, "r") as zip_ref:
            zip_ref.extractall(custom_dir)
        print("Custom dataset extracted successfully.")

        os.remove(dataset_zip)
        print("Temporary dataset archive removed.")

    except Exception as e:
        print(f"An error occurred while downloading the custom dataset: {e}")

if __name__ == "__main__":
    download_articles()
    download_books()
    download_wikipedia_articles()
    download_custom_dataset()
    print("All data collection tasks completed!")
