import requests
from bs4 import BeautifulSoup

def get_product_list(page_num: int):

    # page_num = 1
    # url = f"https://cikgumall.com/shop-2/page/{page_num}" # This link is deprecated 27/11/2025

    url = f"https://cikgumall.com/page/{page_num}/?product_cat=0&s&post_type=product" # This one is for "all" category

    # headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
    # response = requests.get(url, headers=headers)
    response = requests.get(url)
    if response.ok:
        print("Got connection!!!")
    else:
        print("No connection!!!")
        exit(1)

    soup = BeautifulSoup(response.text, 'html.parser')

    product = soup.find_all(attrs={"class":"products product-card-layout-3 columns-4 mobile-col-2 product-list-no-desc-mobile mobile-featured-icons--load"})
    tag_li = product[0].find_all('li')
    count = 0
    for li in tag_li:
        count += 1

    print(count)

    with open(f"product_list_{page_num}.txt", "w", encoding="utf-8") as f:
        for product_iter in tag_li:
            product_title = product_iter.find_all(attrs={"class":"woocommerce-LoopProduct-link woocommerce-loop-product__link"})
            # print(product_title[0].get('href'))

            f.write(f"{product_title[0].get('href')}\n")

# with open("file.txt", "r", encoding="utf-8") as f:
#     print(f.read())

if __name__ == "__main__":

    get_product_list(1)