from django.urls import path
from .views import render_pdf_view,customer_render_pdf_view,CustomerListView

app_name = 'customers'

urlpatterns = [
    path('',CustomerListView.as_view(),name='customer-list-view'),
    path('test/',render_pdf_view,name='test-view'), 
    path('pdf/<pk>',customer_render_pdf_view,name='customer-pdf-view'),   

]