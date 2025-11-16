import requests
import time

if __name__ == "__main__":

    url = "https://cikgumall.com/product/belgian-chocolate-drink-by-choco-albab/aff/lima"

    for i in range(100):
        response = requests.get(url)
        print(response)
        time.sleep(5)