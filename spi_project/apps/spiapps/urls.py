from django.urls import path
from django.conf.urls import url

from . import views          

urlpatterns = [
    url(r'^$', views.index),
    url(r'summ$', views.summ),
    url(r'inputData$', views.inputData),
    url(r'brows$', views.brows),
    url(r'pn$', views.pn),
    url(r'desc$', views.desc),
    url(r'bulk$', views.bulk), 
    url(r'uploadData$', views.uploadData),
    # url(r'bulksearch', views.bulksearch),   
    url(r'NewPart$', views.NewPart),
    url(r'show/(?P<PN_List>\w+)/$', views.show),
    url(r'(?P<pn>\w+)/edit$', views.edit),
    url(r'(?P<pn>\w+)/editPart$', views.editPart),
    url(r'(?P<pn>\w+)/delete$', views.delete),
    url(r'pn_search$', views.pn_search),    
    url(r'desc_search$', views.desc_search),
    # url(r'display$', views.display),
    # path('<int:p_id>/', views.edit,name="edit"),
    # url(r'(?P<p_id>\w+)/editPart$', views.edit),
    url(r'all_data$', views.all_data),
    url(r'edit$', views.edit),   
    url(r'spiinv_show_all$', views.spiinv_show_all),
]