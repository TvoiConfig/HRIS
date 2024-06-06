from django.urls import path

from .views import RecordView, add_orders, DeleteApplicationView, Edit_application

app_name = "request"

urlpatterns = [
    path('', RecordView.as_view(), name="record"),
    path('add_orders', add_orders, name="add_orders"),
    path('delete_application/<int:application_id>/', DeleteApplicationView.as_view(), name="delete_application"),
    path('edit_application/<int:app_id>/', Edit_application, name='edit_application')
]