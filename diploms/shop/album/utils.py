from .models import Card
from django.db.models import Q


def search_projects(request):
    search_query = ''

    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')

        # tags = Tag.objects.filter(name__icontains=search_query)

    pr = Card.objects.distinct().filter(Q(title__icontains=search_query) |
                                        Q(id__icontains=search_query) |
                                        Q(seller__icontains=search_query))
    return pr, search_query
