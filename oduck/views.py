from django.shortcuts import render


def crawl_image(request):
    return render(request, 'oduck/crawl_image.html', {})
