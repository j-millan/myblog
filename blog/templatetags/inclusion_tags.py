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

@register.inclusion_tag('inclusion_tags/social_icons.html')
def social_icons(author):
	info = list()
	if author.profile.facebook_profile != None:
		facebook_info = {
			'color':'has-text-link', 
			'icon_class': 'fab fa-2x fa-facebook-square', 
			'value': author.profile.facebook_profile, 
			'title': 'Facebook'
		}
		info.append(facebook_info)

	if author.profile.twitter_profile != None:
		twitter_info = {
			'color': 'has-text-info', 
			'icon_class': 'fab fa-2x fa-twitter-square', 
			'value': author.profile.twitter_profile, 
			'title': 'Twitter'
		}
		info.append(twitter_info)

	if author.profile.instagram_profile != None:
		instagram_info = {
			'color': 'has-text-brown', 
			'icon_class': 'fab fa-2x fa-instagram-square', 
			'value': author.profile.instagram_profile, 
			'title': 'Instagram'
		}
		info.append(instagram_info)

	return {'info': info}