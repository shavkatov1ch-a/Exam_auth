from django.urls import path
from .views import TagAPIView, CategoryAPIView, CityAPIView

urlpatterns = [
    path('city/', CityAPIView.as_view(), name='city'),
    path('tag/', TagAPIView.as_view(), name='tag'),
    path('category/', CategoryAPIView.as_view(), name='category')
]