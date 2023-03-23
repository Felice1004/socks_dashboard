from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import bs4
from bs4 import BeautifulSoup

def product_loc_filter(urls):
    result = []
    is_product = 0
    for item in urls:
        loc = item.find('loc')
        if '/products/' not in loc.text:
            is_product = 0
        else:
            is_product = 1
            element = dict()
            element = {'loc':'','lastmod':''}

        if is_product:
            # for page_info in sitemap_url:
            #     key = page_info.tag.replace('{http://www.sitemaps.org/schemas/sitemap/0.9}','')
            element['loc'] = loc.text
            element['lastmod'] = item.find('lastmod').text
            result.append(element)
    return result

if __name__ == "__main__":
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    driver = webdriver.Chrome("webdriver/chromedriver", options=chrome_options)

    driver.get("https://www.oh9.com.tw/sitemap.xml")
    page_source = driver.page_source
    soup = BeautifulSoup(page_source, 'xml')
    urls = soup.find_all('url')
    
    result = product_filter(urls)
    driver.get(result[1]['loc']) #開啟產品頁面

    driver.quit()
