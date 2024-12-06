from django.urls import path
from . import views as view
from . import blog_views as views

urlpatterns = [
    path('', view.home, name='home'),
    path('student-list/', view.student_list, name="student_list"),
    path('student-create/', view.student_create, name="student_create"),
    path('student-update/<int:pk>/', view.student_update, name="student_update"),
    
]

from .class_based_views import ItemListView, ItemDetailView, ItemCreateView, ItemUpdateView, ItemDeleteView

urlpatterns += [
    path('item/', ItemListView.as_view(), name='item-list'),
    path('<int:pk>/', ItemDetailView.as_view(), name='item-detail'),
    path('create/', ItemCreateView.as_view(), name='item-create'),
    path('<int:pk>/update/', ItemUpdateView.as_view(), name='item-update'),
    path('<int:pk>/delete/', ItemDeleteView.as_view(), name='item-delete'),
]
