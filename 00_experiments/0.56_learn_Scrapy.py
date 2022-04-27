import os
from scrapy.selector import Selector
from scrapy.http import HtmlResponse


if __name__ == '__main__':
    # url = 'https://en.wikipedia.org/wiki/Web_scraping'
    # html = requests.get(url).content
    # sel = Selector(text=html)

    f_name = os.getcwd() + '/0.56_test4.html'
    with open(f_name, 'r') as f:
        html = f.read()
<<<<<<< Updated upstream
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
=======
        selector = Selector(text=html)
        # sel_lst = selector.xpath('//*[contains(@href, "two")]')

        # Create an xpath to the href attribute
        # sel_lst = selector.xpath('//p[@id="p2"]/a/@href')

        sel_lst = selector.xpath('//a/@href')

        # sel_lst = selector.xpath('//p')
    # response = HtmlResponse(url='http://mysite.com')
    # print(response)
    # data = Selector(response=response).xpath('//span').extract()
        data = sel_lst.extract()

    # second_p_data = sel_lst[1].extract()
        # data = sel_lst.extract()

    print(data)
    # print(f'second object in selector list: {data}')
>>>>>>> Stashed changes
