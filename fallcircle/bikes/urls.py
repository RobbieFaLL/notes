from django.urls import path
from .views import bikes, bikes_content, API_content, Wheeldataview, Tyredataview, Chaindataview, Groupsetdataview, Bikedataview

urlpatterns = [
    path('bikes', bikes, name='bikes'),
    path('bikes/<int:id>',bikes_content, name='bikes_content'),
    path('bikes/API/Wheels', Wheeldataview.as_view()),
    path('bikes/API/Tyres', Tyredataview.as_view()),
    path('bikes/API/Chains',Chaindataview.as_view()),
    path('bikes/API/Groupsets',Groupsetdataview.as_view()),
    path('bikes/API/Bikes', Bikedataview.as_view()),
    path('bikes/API', API_content, name='APIbikes_content')

]