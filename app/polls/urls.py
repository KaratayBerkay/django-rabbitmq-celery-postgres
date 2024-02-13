from django.urls import path
from .views import index, detail, results, vote, other, responser


app_name = "polls"

urlpatterns = [
    path("", index, name="index"),
    path("<int:question_id>/", detail, name="detail"),
    path("<int:question_id>/results/", results, name="results"),
    path("<int:question_id>/vote/", vote, name="vote"),
    path("other/", other, name="other"),
    path("responser/", responser, name="responser"),
]
