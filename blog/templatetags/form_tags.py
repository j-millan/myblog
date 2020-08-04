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

@register.inclusion_tag('inclusion_tags/field_errors.html')
def field_errors(field):
	context = {'field': field}
	return context

@register.inclusion_tag('inclusion_tags/field_with_icon.html')
def render_field_with_icon(field, icon_class, placeholder=False, label=True, margin_bottom='mb-4'):
	context = {
		'field': field, 
		'icon_class': icon_class, 
		'placeholder': placeholder,
		'label': label,
		'margin': margin_bottom
	}
	return context