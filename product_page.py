import requests
from bs4 import BeautifulSoup

if __name__ == "__main__":

    # url = "https://cikgumall.com/product/special-teega-choco-lava-55g/"
    url = "https://cikgumall.com/product/teega-machos-cheezy-45g/"

    response = requests.get(url)

    soup = BeautifulSoup(response.text, 'html.parser')

    product = soup.find(attrs={"class":"product_title entry-title"})

    print(product.text)