from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from polls.models import PollPlugin as PollPluginModel
from django.utils.translation import ugettext as _

class PollPlugin(CMSPluginBase):
		model = PollPluginModel
		name = _("Poll Plugin")
		render_template = "polls/plugin.html"

		def render(self, context, instance, placeholder):
			context.update({'instance':instance})
			return context

plugin_pool.register_plugin(PollPlugin)			