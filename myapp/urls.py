from django.urls import path

from .views import EmployeeDetailMixinAPIView,EmployeeMixinAPIView,EmployeeDetailView,EmployeeList,EmployeeGenericsAPIView,EmployeeGenericsDetailView



# app_name will help us do a reverse look-up latter.
urlpatterns = [
    # path('employee/', EmployeeList.as_view()),
    # path('employee/<int:pk>',EmployeeDetailView.as_view()),
    # path('employee/',EmployeeGenericsAPIView.as_view()),
    # path('employee/<int:id>',EmployeeGenericsDetailView.as_view()),
    path('api/',EmployeeMixinAPIView.as_view()),
    path('api/<int:pk>',EmployeeDetailMixinAPIView.as_view()),
]
