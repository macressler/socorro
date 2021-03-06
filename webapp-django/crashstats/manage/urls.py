from django.conf.urls import patterns, url

from . import views


urlpatterns = patterns(
    '',
    url('^$',
        views.home,
        name='home'),
    url('^featured-versions/$',
        views.featured_versions,
        name='featured_versions'),
    url('^featured-versions/update/$',
        views.update_featured_versions,
        name='update_featured_versions'),
    url('^fields/$',
        views.fields,
        name='fields'),
    url('^fields/lookup/$',
        views.field_lookup,
        name='field_lookup'),
    url('^skiplist/$',
        views.skiplist,
        name='skiplist'),
    url('^skiplist/add/$',
        views.skiplist_add,
        name='skiplist_add'),
    url('^skiplist/data/$',
        views.skiplist_data,
        name='skiplist_data'),
    url('^skiplist/delete/$',
        views.skiplist_delete,
        name='skiplist_delete'),
    url('^users/$',
        views.users,
        name='users'),
    url('^users/data/$',
        views.users_data,
        name='users_data'),
    url('^users/(?P<id>\d+)/$',
        views.user,
        name='user'),
    url('^groups/$',
        views.groups,
        name='groups'),
    url('^groups/(?P<id>\d+)/$',
        views.group,
        name='group'),
    url('^analyze-model-fetches/$',
        views.analyze_model_fetches,
        name='analyze_model_fetches'),
    url('^graphics-devices/$',
        views.graphics_devices,
        name='graphics_devices'),
    url('^graphics-devices/lookup/$',
        views.graphics_devices_lookup,
        name='graphics_devices_lookup'),
    url('^symbols-uploads/$',
        views.symbols_uploads,
        name='symbols_uploads'),
    url('^supersearch-fields/$',
        views.supersearch_fields,
        name='supersearch_fields'),
    url('^supersearch-fields/missing/$',
        views.supersearch_fields_missing,
        name='supersearch_fields_missing'),
    url('^supersearch-field/$',
        views.supersearch_field,
        name='supersearch_field'),
    url('^supersearch-field/create/$',
        views.supersearch_field_create,
        name='supersearch_field_create'),
    url('^supersearch-field/update/$',
        views.supersearch_field_update,
        name='supersearch_field_update'),
    url('^supersearch-field/delete/$',
        views.supersearch_field_delete,
        name='supersearch_field_delete'),
    url('^products/$',
        views.products,
        name='products'),
    url('^releases/$',
        views.releases,
        name='releases'),
)
