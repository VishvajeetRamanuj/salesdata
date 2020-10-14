from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
from django.views.generic import CreateView
from django.urls import reverse_lazy

from .functions import create_plot_from_xlsx
from .models import UploadFile
from .forms import UploadFileForm


# Create your views here.
def index_view(request):
    # return render(request, )
    return HttpResponse("<h1>this is project homepage</h1>")

def sales_home(request):
    return HttpResponse("<h1>this is sales app homepage</h1>")

def upload_xlsx(request):
    return render(request, 'sales/plot_data.html')

class FileUploadView(CreateView):
    model = UploadFile
    form_class = UploadFileForm
    template_name = 'sales/plot_data.html'
    success_url = reverse_lazy('sales:plot_and_show')

def plot_and_show(request):
    # processing csv file and createing images
    # filename = request.FILES['sales_data_file'].name
    # print(filename)
    # fetching latest file name with path
    file = UploadFile.objects.order_by('-id')[0]
    file_path = settings.BASE_DIR + file.file.url
    # print(settings.BASE_DIR)
    # print(file_path)
    # print(filename)
    create_plot_from_xlsx(file_path, "Sheet1")

    # showing images
    return render(request, 'sales/plot_and_show.html')
