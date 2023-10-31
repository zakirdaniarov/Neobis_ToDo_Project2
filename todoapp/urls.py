from django.urls import path
from . views import listview, addItem, deleteItem, editItem

urlpatterns = [path('todoapp/', listview),
               path('addItem/', addItem),
               path("deleteItem/<int:i>/", deleteItem),
               path("editItem/<int:i>/", editItem),]

