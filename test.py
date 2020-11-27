import requests

from bs4 import BeautifulSoup

word = input()
url_inpt = input()
def get_html(url):
    result = requests.get(url)
    return result.text

def get_data(html):
    soup = BeautifulSoup(html, "html.parser")
    h2 = soup.find_all('p')
    for p in h2:
        if word in p.text:
            print(p.text)    
    
def main():
    html = get_html(url_inpt)
    get_data(html)

    

if __name__ == "__main__":
    main()

