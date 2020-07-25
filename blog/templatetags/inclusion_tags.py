from django import template

register = template.Library()

@register.inclusion_tag('inclusion_tags/category_tag.html')
def render_tag(category):
	css_class = f'tag {category.get_tag_color_display()} is-light is-lowercase'
	context = {'class': css_class, 'category': category}
	return context

@register.inclusion_tag('inclusion_tags/field_errors.html')
def field_errors(field):
	context = {'field': field}
	return context