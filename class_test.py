class Top(object):
    def __init__(self, a, b, c):
        print("class Top init")
        print(a, b, c)
        self.aa = a
        self.bb = b
        self.cc = c


class First(Top):
    def __init__(self, a, b, c, ):
        super(First, self).__init__(a, b, c)
        print(self.aa, self.bb, self.cc)


class Second(Top):
    def __init__(self, d, e, f):
        super(Second, self).__init__(d, e, f)
        print(self.aa, self.bb, self.cc)


class Bot(First, Second):
    def __init__(self, a=1, b=2, c=3):
        super(Bot, self).__init__(a, b, c)


class Foo(object):
    def __init__(self):
        print('FOO')

    def func1(self):
        print('func1')
        print(self)
        print(id(self))

    def func2():
        print('func2')


class Ho(Foo):
    def __init__(self):
        print(id(super()))
        print(super)
        print(super())


print(help(super))
bot = Bot()

from icrawler.builtin import GoogleImageCrawler
from icrawler.builtin.google import GoogleFeeder
from icrawler.parser import Parser
from bs4 import BeautifulSoup

# google_feeder = GoogleFeeder(thread_num=4, signal=None, session=None)
# google_feeder.feed(keyword='megumin', offset=0, max_num=100,
#                    date_min=None, date_max=None)

google_crawler = GoogleImageCrawler(parser_threads=2, downloader_threads=1,
                                    storage={'root_dir': '/home/ryu/Projects/chatBot/'})

google_crawler.crawl(keyword='megumin', max_num=1,
                     date_min=None, date_max=None,
                     min_size=(200, 200), max_size=None, get_url=True)
