from django import template
from django.contrib.auth.forms import AuthenticationForm

register = template.Library()

@register.filter
def field_type(field):
	return field.field.widget.__class__.__name__

@register.filter
def input_class(field):
	css_class = ''
	bulma_input_class = 'textarea' if field_type(field) == 'Textarea' else 'input'
	if field.form.is_bound:
		if field.errors:
			css_class = 'is-danger'
		elif field_type(field) != 'PasswordInput':
			css_class = 'is-success'

	return f'{bulma_input_class} {css_class}'