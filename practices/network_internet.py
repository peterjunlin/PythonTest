import urllib.request


def get_content(url):
    request = urllib.request.Request(url)
    response = urllib.request.urlopen(request)
    return response.read()  # .decode('utf-8')


def parse_html(url):
    # Todo: https://www.crummy.com/software/BeautifulSoup/bs4/doc/
    pass


def download_image(url):
    pass


def practice1():
    url = "http://www.google.com/"
    s1 = get_content(url)
    print(s1)


def practice2():
    # url = "http://www.google.com/"
    # s1 = parse_html(url)
    # print(s1)
    pass

