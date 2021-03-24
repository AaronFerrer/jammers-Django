from django.urls import path
from . import views

#urlpatterns = [
#	path('', views.index, name='index')
#]
'''
urlpatterns = [
	path('', views.test,name='')
]

'''
urlpatterns = [
    path('', views.index, name='index'),
   # path('braceconfig/',include('braceconfig.urls')),
    path('patients/', views.PtListView.as_view(), name='patients'),
    path('patient/<int:pk>', views.PtDetailView.as_view(), name='patient-detail'),
]

urlpatterns += [
    path('patient/<uuid:pk>/calculate/', views.calculate_surgeon, name='calculate_surgeon'),
]	