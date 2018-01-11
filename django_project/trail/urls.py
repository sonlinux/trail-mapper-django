from __future__ import absolute_import
# coding=utf-8
"""URI Routing configuration for this apps."""
from django.conf.urls import url

from .api_views.trail import TrailListApiView
from .api_views.trail_section import TrailSectionListApiView
from .api_views.trail_sections import TrailSectionsListApiView
from .api_views.category import CategoryListApiView
from .api_views.grade import GradeListApiView, GradeUpdateAPIView
from .api_views.point_of_interest import PointOfInterestListApiView

urlpatterns = [

    url(
        r'^api/list_trail/',
         TrailListApiView.as_view(),
        name='api-get-trail-list'),
    url(
        r'^api/list_trail_section/',
        TrailSectionListApiView.as_view(),
        name='api-get-trail-section'),
    url(
        r'^api/list_trail_sections/',
        TrailSectionsListApiView.as_view(),
        name='api-get-trail-sections'),
    url(
        r'^api/list_category/',
        CategoryListApiView.as_view(),
        name='api-get-category'),
    url(
        r'^api/list_grade/',
        GradeListApiView.as_view(),
        name='api-get-grade'),
    url(
        r'^api/(?P<slug>[\w-]+)/list_grade-update/',
        GradeUpdateAPIView.as_view(),
        name='api-get-grade-update'),
    url(
        r'^api/list_poi/',
        PointOfInterestListApiView.as_view(),
        name='api-get-poi')
]
