from django.urls import path
from .views import student_add_update, student_delete, student_list
urlpatterns = [
        path('', student_add_update, name='student_add_update'), # get and post req. for insert operation
        path('<int:id>/', student_add_update, name='student_update'), # get and postreq. for update operation
        path('delete/<int:id>/',student_delete,name='student_delete'),
        path('list/',student_list,name='student_list') # get req. to retrieve anddisplay all records
]