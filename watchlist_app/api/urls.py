from django.urls import path, include
from rest_framework.routers import DefaultRouter
from watchlist_app.api.views import (
    ReviewCreate, ReviewList, ReviewDetail, UserReview, WatchListGenericView, WatchListView, WatchListDetailView, StreamPlatformViewset, StreamPlatformView, StreamPlatformDetailView)
# from watchlist_app.api.views import movie_list, movie_details

router = DefaultRouter()
router.register('stream_list', StreamPlatformViewset,
                basename='streamplatform')


urlpatterns = [
    path('list/', WatchListView.as_view(), name='movies_list'),
    path('<int:pk>/', WatchListDetailView.as_view(), name='movie_details'),
    path('movie_list/', WatchListGenericView.as_view(), name='movies_list2'),

    path('', include(router.urls)),

    #     path('stream_list/', StreamPlatformView.as_view(), name='stream'),
    #     path('stream_list/<int:pk>', StreamPlatformDetailView.as_view(),
    #          name='stream_details'),

    # path('reviews/', ReviewList.as_view(), name='review_list'),
    # path('reviews/<int:pk>', ReviewDetail.as_view(), name='review_detail'),

    path('<int:pk>/submit_review/',
         ReviewCreate.as_view(), name='submit_review'),
    path('<int:pk>/reviews/',
         ReviewList.as_view(), name='review_list'),
    path('review/<int:pk>/',
         ReviewDetail.as_view(), name='review_detail'),
    path('reviews/', UserReview.as_view(), name='user_review_detail')
]
