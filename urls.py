from django.urls import path
from employee import views

urlpatterns = [
    path('emp',views.emp),
    path('show',views.show),
    path('edit/<int:id>/',views.edit),
    path('updata/<int:id>/',views.updata),
    path('delete/<int:id>/',views.destory)
]