from django.urls import path
from . import views


urlpatterns = [
    path('viewbox<int:boxID>', views.viewbox, name='box_view.html'),
    # ex: planner/15
    path('<int:clID>', views.updateCharacter, name='update_character'),
    path('newbox', views.newbox, name='addbox'),
    path('deletebox', views.deletebox, name='deletebox'),
    path('boxlist', views.boxList, name='box_list'),
    path('viewbox<int:boxID>/add_character', views.addCharacter, name='add_character'),
    path('viewbox<int:boxID>/remove_character', views.removeCharacter, name='remove_character')
]
