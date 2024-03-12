from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Traveller
from .forms import TravellerForm

# Create your views here.
def home_page(request):
    """
    Displays a landing page for the site
    """

    return render(
        request,
        "travellerprofile/home.html",
        {},
    )

class TravellerList(generic.ListView):
    """
    Returns all Traveller profiles in :model:`travellerprofile:Traveller`
    and displays them in a page of six posts.
    **Context**

    ``queryset``
        All published instances of :model:`travellerprofile:Traveller`

    **Template:**

    :template:`travellerprofile/index.html`
    """
    queryset = Traveller.objects.all()
    print(queryset.first())
    template_name = "travellerprofile/index.html"

def view_traveller(request):
    """
    Display an individual :model: travellerprofile.Traveller

    **Context**
    ``traveller``
        An instance of travellerprofile.Traveller

    **Template**
    :template: ``travellerprofile/view_traveller.html``
    """
    queryset = Traveller.objects.all()
    traveller = get_object_or_404(queryset, user=request.user)

    return render(
        request,
        "travellerprofile/view_traveller.html",
        {
            "traveller": traveller,
        },
    )

def create_traveller(request):
    """
    Display form to allow user creation of a .models:Traveller instance
    """
    context = {}
    if request.method == "POST":
        form = TravellerForm(request.POST, request.FILES)
        if form.is_valid():
            traveller = form.save(commit=False)
            traveller.user = request.user
            traveller.save()
    else:
        form = TravellerForm()
    context['form'] = form
    return render( request, "travellerprofile/create_traveller.html", context)

