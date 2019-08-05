from django.urls import path
from core.views import GeneratePdf


urlpatterns = [
    path('', GeneratePdf.as_view(), name="Generatepdf"),

]
