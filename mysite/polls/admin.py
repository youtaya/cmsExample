from django.contrib import admin
from polls.models import Poll, choice

class ChoiceInline(admin.TabularInline):
	model = choice
	extra = 3

class PollAdmin(admin.ModelAdmin):
	fieldsets = [
	(None, {'fields': ['question']}),
	('Date Information', {'fields': ['pub_date'], 'classes': ['collapse']}),
	]
	list_display = ('question', 'pub_date', 'was_published_recently')
	inlines = [ChoiceInline]
	list_filter = ['pub_date']
	search_fields = ['question']

admin.site.register(Poll, PollAdmin)
