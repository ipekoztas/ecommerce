from django.urls import path

from . import views

app_name = 'sales'
urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("products", views.products, name="products"),
    path("products/<int:pk>", views.ItemView.as_view(), name="show_product"),
    path("editproducts/addProduct", views.addProductView.as_view(), name="products-add"),
    path("updateProduct/<int:pk>", views.updateProduct, name="products-update"),
    path("editproducts/deleteProduct/<int:pk>", views.deleteProduct, name="products-delete"),
    path("editproducts/", views.editProduct, name="products-edit"),
    path("editproducts/unlistProduct/<int:pk>", views.unlist, name="products-unlist"),
    path("editproducts/listProduct/<int:pk>", views.list, name="products-list"),
    path("editproducts/deleteItem/<int:pk>", views.deleteItem, name="products-deleteitem"),

]