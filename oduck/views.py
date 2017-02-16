from django.shortcuts import render


def chatting(request):
    return render(request, 'oduck/basee.html', {})
