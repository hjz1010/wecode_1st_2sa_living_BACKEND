from django.urls import path
from orders.views import OrderView, OrderListView

urlpatterns = [
    path('', OrderView.as_view()),
    path('/<int:order_id>', OrderView.as_view()),
    path('/list', OrderListView.as_view()),
]
