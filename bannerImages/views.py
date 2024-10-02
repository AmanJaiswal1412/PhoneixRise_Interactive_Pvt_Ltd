from django.shortcuts import render
from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from cms.models.pluginmodel import CMSPlugin
from django.utils.translation import gettext_lazy as _


@plugin_pool.register_plugin
class PageBannerPlugin(CMSPluginBase):
    model = CMSPlugin
    render_template = "PageBanner_plugin.html"
    cache = False

# Create your views here.
