from django.urls import path
from . import views

urlpatterns = [
    path('BCourt/', views.Court, name='court'),
    # path('BCourt/', views.San, name='san'),

    path('', views.home, name='home'),
    path('search/', views.search, name='search'),
    path('login/', views.user_login, name='login'),
    path('register/', views.user_register, name='register'),
    path('logout/', views.user_logout, name='logout'),

    # path('datsan', views.datSan, name='datsan'),
   

    path('role/', views.role, name='role'),
    path('filter/', views.courtFilter, name='filter'),
    path('his/', views.history, name='his'),
    path('deleteHis/<str:maVe>/', views.deleteHistory, name='deleteHis'),
    path('detail/<str:maCourt>/', views.chiTiet, name='detail'),


    path('xetduyetnhanvien/', views.xetduyetNhanVien, name='xetduyetNhanVien'),
    path('staffList/', views.staffList, name='staffList'),
    path('chamcong/', views.chamCong, name='chamCong'),
    path('payment/', views.payment, name='payment'),
    path('revenue/', views.Revenue, name='Revenue'),
    path('approveStaff/<int:staff_id>/', views.approveStaff, name='approveStaff'),
    path('rejectStaff/<int:staff_id>/', views.rejectStaff, name='rejectStaff'),
]