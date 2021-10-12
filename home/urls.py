
from django.urls import path
from .views import homepage,contents

urlpatterns = [
   path('',homepage),
   path('contents/',contents),

]