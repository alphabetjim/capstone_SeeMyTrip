from django.shortcuts import render

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