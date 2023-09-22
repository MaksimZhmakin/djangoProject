from django.urls import path, include
from .views import lessons_list, product_lessons_list, statistic
from rest_framework.routers import SimpleRouter
from .views import ProductViewset, AccessViewset, LessonViewset, UsersViewset

router = SimpleRouter()
router.register('products', ProductViewset, basename='products')
router.register('lessons', LessonViewset, basename='lessons')
router.register('users', UsersViewset, basename='users')
router.register('access', AccessViewset, basename='access')

urlpatterns = [
    path('lessons/<str:username>', lessons_list),
    path('lesson/<str:username>/<str:product_title>/', product_lessons_list),
    path('statistic/', statistic),
    path('', include(router.urls)),
    
]
