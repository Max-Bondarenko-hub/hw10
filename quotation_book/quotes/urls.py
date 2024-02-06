from django.urls import path
from . import views

app_name = "quotes"

urlpatterns = [
    path("", views.main, name="main"),
    path("author/", views.author, name="author"),
    path("tag/", views.tag, name="tag"),
    path("quote/", views.quote, name="quote"),
    path("<int:page>", views.main, name="root_paginate"),
    path("author/<str:author_name>/", views.about_author, name="about_author"),
    path("tag/<str:tag_name>/", views.quotes_by_tag, name="quotes_by_tag"),
]
