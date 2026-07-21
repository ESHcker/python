from bs4 import BeautifulSoup
import requests

def main():
    url = "https://www.bbc.com/news"
    print(get_headlines(url))

    
def parse_HTML(url) -> BeautifulSoup:
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    response.close()
    return soup

def get_headlines(url) -> Tag:
    parsed_HTML = parse_HTML(url)
    all_title_news = parsed_HTML.find_all('h2')
    headlines = []
    for new in all_title_news:
        headline = {
            "headline" : new.string,
            "url" : new.url
        }
        headlines.append(headline)
    return headlines


if __name__ == "__main__":
    main()