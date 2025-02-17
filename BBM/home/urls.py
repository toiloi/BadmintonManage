from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.user_login, name='login'),
    path('register/', views.user_register, name='register'),
    path('logout/', views.user_logout, name='logout'),
<<<<<<< HEAD

    path('role', views.role, name='role'),
    path('datsan', views.datSan, name='datsan'),
   

    path('role/', views.role, name='role'),
    path('datsan/', views.datSan, name='datsan'),
    path('detail/<str:maCourt>/', views.chiTiet, name='detail'),
    path('xetduyetnhanvien/', views.xetduyetNhanVien, name='xetduyetNhanVien'),
    path('staffList/', views.staffList, name='staffList'),
    path('chamcong/', views.ChamCong, name='chamCong'),
    path('payment/', views.payment, name='payment'),
    path('revenue/', views.Revenue, name='Revenue'),
    



=======
    path('role1', views.role1, name='role1'),
    path('role2', views.role2, name='role2'),
    path('role3', views.role3, name='role3'),
    path('staffManage', views.staffManage,name="staffMange")
>>>>>>> 81997368de2b5ecf98fbd5d5df94dfa39d0fd36d
]