from django.conf.urls import url, include
from HemAuctionSystem.views import IndexView


urlpatterns = [
    url(r'^$', IndexView.as_view()),
]