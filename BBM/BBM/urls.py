from django.urls import path
from .views import get_vip_customers, get_payments, get_revenue, vip_page, payment_page, report_page

urlpatterns = [
    path("api/vip-customers", get_vip_customers, name="get_vip_customers"),
    path("api/payments", get_payments, name="get_payments"),
    path("api/revenue", get_revenue, name="get_revenue"),
    path("vip", vip_page, name="vip_page"),
    path("payment", payment_page, name="payment_page"),
    path("report", report_page, name="report_page"),
]
