import time
import re
import requests
from bs4 import BeautifulSoup



def trends_retriever(country_code):
    url = f"https://trends.google.com/trends/trendingsearches/daily/rss?geo={country_code}"
    response = requests.get(url)
    xml_document = response.content
    soup = BeautifulSoup(xml_document, "html.parser")
    titles = soup.select("title")
    approximate_traffic = soup.find_all("ht:approx_traffic")
    return {title.text: (traffic.text)for title, traffic in zip(titles[1:], approximate_traffic)}

if __name__ == '__main__':
    trends = trends_retriever("KR")  
    print(trends)