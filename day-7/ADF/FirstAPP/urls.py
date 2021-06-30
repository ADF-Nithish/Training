from django.urls import path
from FirstAPP.views import FormView

urlpatterns = [
    path('', FormView.as_view(),name='RequestForm')
]