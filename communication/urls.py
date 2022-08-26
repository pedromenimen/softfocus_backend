from django.urls import path

import communication.views as views

urlpatterns = [
    path("communication/", views.ListCreateCommunicationView.as_view()),
    path("communication/list/<owner_cpf>/", views.ListFilteredCommunicationView.as_view()),
    path(
        "communication/<id>/", views.RetrieveUpdateDestroyCommunicatrionView.as_view()
    ),
    path("communication/places/", views.ListCommunicationView.as_view()),
]
