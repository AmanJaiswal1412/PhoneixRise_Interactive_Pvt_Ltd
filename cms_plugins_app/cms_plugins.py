from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.utils.translation import gettext_lazy as _
from .models import *
from django.db import models


@plugin_pool.register_plugin  # Registers the plugin in the CMS
class PageBannerPlugin(CMSPluginBase):
    model = PageBannersModel
    render_template = "PageBanner_plugin.html"
    cache = False
    name = _("Page Banners")

    def render(self, context, instance, placeholder):
        context['instance'] = instance
        context['page_title'] = instance.page.get_title()  # Pass page title to the template
        return context


@plugin_pool.register_plugin  # Registers the plugin in the CMS
class ProductTechPlugin(CMSPluginBase):
    model = ProductTechnologyModel
    render_template = "productTech_plugin.html"
    cache = False
    name = _("Product Technology")

    def render(self, context, instance, placeholder):
        # Get the current page from the context
        current_page = context['request'].current_page

        # Retrieve all objects associated with the current page
        techproducts = ProductTechnologyModel.objects.filter(associated_page=current_page)

        context['techproducts'] = techproducts
        context['current_page'] = current_page
        return context
