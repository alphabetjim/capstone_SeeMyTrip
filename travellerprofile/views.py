from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Traveller
from .forms import TravellerForm

# Create your views here.
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

# def uploadToCloudinary(request_files):
#     """
#     Function to upload user photo to cloudinary
#     """


# def create_traveller(request):
#     """
#     Display form to allow user creation of a .models:Traveller instance
#     """
#     traveller_form = TravellerForm()
#     print(TravellerForm)
#     if request.method == "POST":
#         traveller_form = TravellerForm(request.POST, request.FILES)
#         print(request.FILES)
#         if traveller_form.is_valid():
#             traveller = traveller_form.save(commit=False)
#             traveller.user = request.user
#             traveller.profile_photo = request.FILES['profile_photo']
#             traveller.save()
#             # messages.add_message(
#             #     request, messages.SUCCESS,
#             #     'Comment submitted and awaiting approval'
#             # )

#     return render(
#         request,
#         "travellerprofile/create_traveller.html",
#         {
#             "traveller_form": traveller_form,
#         }
#     )

def create_traveller(request):
    """
    Display form to allow user creation of a .models:Traveller instance
    """
    context = {}
    if request.method == "POST":
        form = TravellerForm(request.POST, request.FILES)
        if form.is_valid():
            firstname = form.cleaned_data.get("firstname")
            lastname = form.cleaned_data.get("lastname")
            bio = form.cleaned_data.get("bio")
            img = form.cleaned_data.get("profile_photo")
            obj = Traveller.objects.create(
                                 user = request.user,
                                 firstname = firstname, 
                                 lastname = lastname, 
                                 bio = bio, 
                                 profile_photo = img
                                 )
            obj.save()
            print(obj)
    else:
        form = TravellerForm()
    context['form'] = form
    return render( request, "travellerprofile/create_traveller.html", context)

