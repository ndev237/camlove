from django.shortcuts import render


def about(request):
    """

    :param request:
    :return:
    """
    return render(request, 'vitrine/about.html')


def contact(request):
    """

    :param request:
    :return:
    """
    return render(request, 'vitrine/contact.html')


