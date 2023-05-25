from django.contrib import admin
from django.urls import path

from webapp.views import auth, openai

urlpatterns = [
    path("correction", openai.correction, name="correction"),
    path("creation", openai.creation, name="creation"),
    path("general", openai.general, name="general"),
    path("historic", openai.historic, name="historic"),
    path("historic_delete/<id>", openai.historic_delete, name="historic_delete"),
    path("signin", auth.signin, name="signin"),
    path("signout", auth.signout, name="signout"),
    path("signup", auth.signup, name="signup"),
]
