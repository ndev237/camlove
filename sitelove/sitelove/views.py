from django.shortcuts import render


def home(request):
    """

    :param request:
    :return:
    """
    return render(request, 'home.html')


def nav(request):
    """

    :param request:
    :return:
    """
    return render(request, 'nav.html')


