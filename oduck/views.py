from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render_to_response


from icrawler.builtin import GoogleImageCrawler
import json


def crawl_image(request):
    return render(request, 'oduck/crawl_image_base.html', {})


def search_crawl_image(request):
    if request.method == 'POST' and request.is_ajax():
        search_keyword = request.POST.get('keyword')

        # google_crawler = GoogleImageCrawler(parser_threads=4, downloader_threads=1,
        #                                     storage={'root_dir': '/home/ryu/Projects/GoogleImageDownloader/images'})
        #
        # urls = google_crawler.crawl(keyword=search_keyword, max_num=5,
        #                             date_min=None, date_max=None,
        #                             min_size=(200, 200), max_size=None)

        return HttpResponse(json.dumps({'success': 'true', 'urls': crawl(search_keyword)}),
                            content_type="application/json")
    else:
        return render_to_response('oduck/crawl_image_base.html', locals())


def crawl(keyword):
    google_crawler = GoogleImageCrawler(parser_threads=2, downloader_threads=1,
                                        storage={'root_dir': '/home/ryu/'})

    urls = google_crawler.crawl(keyword='megumin', max_num=100,
                                date_min=None, date_max=None,
                                min_size=(200, 200), max_size=None)

    return urls
