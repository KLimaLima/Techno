import requests
from bs4 import BeautifulSoup

def main():
    # print("Hello from techno!")
    pass

if __name__ == "__main__":
    # main()

    url = "https://cikgumall.com/shop-2/"

    # headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
    # response = requests.get(url, headers=headers)
    response = requests.get(url)
    # print(response.text)

    soup = BeautifulSoup(response.text, 'html.parser')
    # print(soup.prettify())  # prints well-formatted HTML

    # product = soup.find_all(attrs={"class":"products product-card-layout-3 columns-4 mobile-col-2 product-list-no-desc-mobile mobile-featured-icons--load"})
    # product = soup.find_all(attrs={"class":"product type-product post-32090 status-publish first outofstock product_cat-biscuits-snacks product_cat-lava-snacks product_tag-lava product_tag-new-arrivals product_tag-snacks product_tag-teega has-post-thumbnail sale shipping-taxable purchasable product-type-simple"})
    product = soup.find_all(attrs={"class":"products product-card-layout-3 columns-4 mobile-col-2 product-list-no-desc-mobile mobile-featured-icons--load"})
    # product = soup.find_all('ul')
    # print(product[0].prettify())
    # print(product[0])
    tag_li = product[0].find_all('li')
    count = 0
    for li in tag_li:
        count += 1

    print(count)

    # product_title = product[0].find_all(attrs={"class":"woocommerce-LoopProduct-link woocommerce-loop-product__link"})
    # print(product_title[2].text)

    for product_iter in tag_li:
        product_title = product_iter.find_all(attrs={"class":"woocommerce-LoopProduct-link woocommerce-loop-product__link"})
        # print(product_title[2].text)
        print(product_title[0].get('href'))

    # product_title = tag_li[0].find_all(attrs={"class":"woocommerce-LoopProduct-link woocommerce-loop-product__link"})
    # print(product_title[0].get('href'))
    # for title in product_title:
    #     print(title.text)
    # print(product_title[2].text)
    
    # for i in product_title:
    #     print("here")
    #     print(i)

    # n = 0
    # for i in product:
    #     n += 1
    #     print(f"list_number_{n}")
    #     print(i.prettify())