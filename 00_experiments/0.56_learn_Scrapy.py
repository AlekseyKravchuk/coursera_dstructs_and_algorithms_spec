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
        selector = Selector(text=html)

        # 'xpath(xpath_expression)' method returns a list of selectors, which represents the nodes selected
        # by the xpath expression given as an argument
        sel_lst = selector.xpath("//p")

        # the number of items (selectors of interest)
        N = len(sel_lst)

        # 'extract()' method returns a unicode string along with the selected data.
        data = sel_lst.extract()
        # data = sel_lst.extract()
        print(f'extracted data: {data}')
        print(f'the number of selectors returned: {N}')
