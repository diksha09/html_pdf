from django.urls import path
from core1.views import GeneratePdf


urlpatterns = [
    path('', GeneratePdf.as_view(), name="Generatepdf"),

]
