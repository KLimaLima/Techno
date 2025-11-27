import requests
from bs4 import BeautifulSoup
import re

if __name__ == "__main__":

    # url = "https://cikgumall.com/product/special-teega-choco-lava-55g/"
    # url = "https://cikgumall.com/product/teega-machos-cheezy-45g/"
    url = "https://cikgumall.com/product/reevo-chocolate-malt-drink-1kg/"

    response = requests.get(url)

    soup = BeautifulSoup(response.text, 'html.parser')

    title = soup.find(attrs={"class":"product_title entry-title"})
    print(1)
    print(title.text)

    short_desc = soup.find(attrs={"class":"short-description__content"})
    print(2)
    print(short_desc.text)

    long_desc = soup.find(attrs={"class":"motta-dropdown__content"})
    print(3)
    print(long_desc.text)

    img_src = soup.find(attrs={"class":"woocommerce-product-gallery__image"})
    print(4)
    print(img_src)

    print(5)
    pattern = r'data-src="(.*?)"'
    found_src = re.search(pattern, str(img_src))
    print(found_src.group(1))

    img_data = requests.get(found_src.group(1)).content

    with open("image/test_img.jpg", "wb") as f:
        f.write(img_data)