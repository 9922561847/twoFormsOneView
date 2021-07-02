from django.shortcuts import render

from .forms import ProfileForm


def home(request):
    form = ProfileForm()
    
    if request.method == 'POST':
        
        if form.is_valid():
            form.save()
    return render(request,'home.html',{'form':form})


def load_cities(request):
    country_id = request.GET.get('country_id')
    cities = City.objects.filter(country_id=country_id).all()
    return render(request, 'persons/city_dropdown_list_options.html', {'cities': cities})