from django.urls import path, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from .views import sales_home, plot_and_show, upload_xlsx

app_name = 'sales'

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', sales_home),
    path('upload_xlsx/', upload_xlsx, name='upload_xlsx'),
    path('plot_and_show/', plot_and_show, name='plot_and_show'),
]

urlpatterns += staticfiles_urlpatterns()
