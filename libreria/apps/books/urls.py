from django.conf.urls import url, include

from . views import index, listado, detalleLibro, detail
app_name = 'books'
urlpatterns = [
    url(r'^$', index),
    url(r'^listado/$', listado),
    url(r"^listado/(?P<id>\d+)$", detalleLibro, name='detalle'),
    url(r'(?P<slug>[\w-]+)/$', detail),
    #url(r'^detalle/(?P<id_receta>\d+)$','principal.views.detalle_receta'),
    #url(r'^detalle/$', detalleLibro),

    #url(r'^detalle/(?P<id>[0-9]+)/$', detalleLibro),
]
