from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('wallpapers.views',
    (r'^cate/list/$', 'cate_list'),
    (r'^cate/add/$', 'cate_add'),
    (r'^cate/(?P<cate_id>\d+)/edit/$', 'cate_edit'),
    (r'^cate/(?P<cate_id>\d+)/del/$', 'cate_del'),
)
