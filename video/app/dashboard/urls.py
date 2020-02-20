from django.urls import path
from .views.base import Index
from .views.auth import Login, AdminManager, Logout, UpdateAdminStatus
from .views.video import ExternalVideo, VideoSubView, VideoStarView, DeleteStarView

urlpatterns = [
    path('', Index.as_view(), name='dashboard_index'),
    path('login/', Login.as_view(), name='dashboard_login'),
    path('admin/manager/', AdminManager.as_view(), name='admin_manager'),
    path('logout/', Logout.as_view(), name='dashboard_logout'),
    path('admin/manager/update/status/', UpdateAdminStatus.as_view(), name='update_admin_status'),
    path('video/external/', ExternalVideo.as_view(), name='external_video'),
    path('video/videosub/<int:video_id>/', VideoSubView.as_view(), name='video_sub'),
    path('video/star', VideoStarView.as_view(), name='video_star'),
    path('video/star/delete/<int:video_id>/<int:star_id>/', DeleteStarView.as_view(), name='star_delete')
]