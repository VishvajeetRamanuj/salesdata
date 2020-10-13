from django.shortcuts import render
from django.http import HttpResponse
from .functions import create_plot_from_xlsx

# Create your views here.
def index_view(request):
    # return render(request, )
    return HttpResponse("<h1>this is project homepage</h1>")

def sales_home(request):
    return HttpResponse("<h1>this is sales app homepage</h1>")

def upload_xlsx(request):
    return render(request, 'sales/plot_data.html')

def plot_and_show(request):
    # processing csv file and createing images
    filename = request.FILES['sales_data_file'].name
    print(filename)
    create_plot_from_xlsx(filename, "Sheet1")

    # showing images
    return render(request, 'sales/plot_and_show.html')
