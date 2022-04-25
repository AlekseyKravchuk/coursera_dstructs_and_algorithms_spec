import os
from scrapy import Selector
import requests


if __name__ == '__main__':
    # url = 'https://en.wikipedia.org/wiki/Web_scraping'
    # html = requests.get(url).content
    # sel = Selector(text=html)

    f_name = os.getcwd() + '/0.56_test.html'
    with open(f_name, 'r') as f:
        html = f.read()
        # print(html)
        sel = Selector(text=html)
        sel_lst = sel.xpath("//p")

        second_p_data = sel_lst[1].extract()
        data = sel_lst.extract()
        print(data)
        print(f'second object in selector list: {second_p_data}')
