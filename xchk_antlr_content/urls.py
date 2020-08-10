from django.urls import path

from . import contentviews

urlpatterns = [
    path('xchk_antlr_content_demo', contentviews.DemoANTLRView.as_view(), name=f'{contentviews.DemoANTLRView.uid}_view'),
]
