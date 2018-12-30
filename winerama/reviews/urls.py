from django.urls import path
from . import views

app_name = 'reviews'

urlpatterns = [
  # Page 14
  path('', views.review_list, name='review_list'),
  path('review/<int:review_id>', views.review_detail, name='review_detail'),
  # Page 20
  path('wine/', views.wine_list, name='wine_list'),
  path('wine/<int:wine_id>/', views.wine_detail, name='wine_detail'),
  # Page 24
  path('wine/<int:wine_id>/add_review/', views.add_review, name='add_review'),
]
