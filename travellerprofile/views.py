from django.shortcuts import render
from django.views import generic
from .models import Traveller

# Create your views here.
class TravellerList(generic.ListView):
    """
    Returns all Traveller profiles in :model:`travellerprofile:Traveller`
    and displays them in a page of six posts.
    **Context**

    ``queryset``
        All published instances of :model:`blog.Post`
    ``paginate_by``
        Number of posts per page.

    **Template:**

    :template:`blog/index.html`
    """
    queryset = Traveller.objects.all()
    template_name = "travellerprofile/index.html"