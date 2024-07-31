from django.urls import path
from hotels.infraestructure.views.get_hotels.get_hotel_view import GetHotelView
from hotels.infraestructure.views.webhook_reviews.webhook_reviews_view import WebhookReviewsView

urlpatterns = [
    path("reviews/", WebhookReviewsView.as_view(), name="reviews"),
    path("",GetHotelView.as_view(), name="hotel"),

]