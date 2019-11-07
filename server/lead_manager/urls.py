from rest_framework import routers
from .api import SalesLeadViewSet, UserViewSet, CompanyViewSet
from django.urls import path, include
from . import views

router = routers.DefaultRouter()
router.register('api/leads', SalesLeadViewSet, 'leads')
router.register('api/users', UserViewSet, 'users')
router.register('api/companies', CompanyViewSet, 'companies')

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for accessible API.
urlpatterns = [
    path('', include(router.urls)),
    path('auth_users/', views.auth_users, name='auth_users'),
    path('get_leads/<str:userFk>/', views.get_lead_models, name='get_user_models'),
    path('get_userid/<str:username>/', views.get_userid, name='get_userid'),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

# urlpatterns = router.urls
