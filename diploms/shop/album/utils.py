from .models import Card
from django.db.models import Q


def search_projects(request):
    search_query = ''

    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')

        # tags = Tag.objects.filter(name__icontains=search_query)

    pr = Card.objects.distinct().filter(Q(title__contains=search_query.lower()) |
                                        Q(seller__contains=search_query.lower()))

    # pr = Card.objects.distinct().filter(Q(title__iregex=r"(а-Я|0-9)$") |
    #                                     Q(seller__iregex=r"(а-Я|0-9)$"))
    return pr, search_query
