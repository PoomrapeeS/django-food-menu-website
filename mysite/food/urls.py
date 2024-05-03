from . import views
from django.urls import path

app_name = "food"
urlpatterns = [
    path("", views.IndexClassView.as_view(), name="index"),
    path("item/", views.item, name="item"),
    # /food/1
    path("<int:pk>/", views.FoodDetail.as_view(), name="detail"),
    # add items
    path("add", views.CreateItem.as_view(), name="create_item"),
    # Edit items
    path("update/<int:item_id>", views.update_item, name="update_item"),
    # Delete item
    path("delete/<int:item_id>", views.delete_item, name="delete_item"),
]
