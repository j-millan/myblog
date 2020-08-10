from django.core.exceptions import ValidationError
import re

def validate_facebook_url(value):
	if not 'facebook' in value:
		raise ValidationError(f'{value} is not a valid facebook url.')

def validate_instagram_url(value):
	if not 'instagram' in value:
		raise ValidationError(f'{value} is not a valid instagram url.')

def validate_twitter_url(value):
	if not 'twitter' in value:
		raise ValidationError(f'{value} is not a valid twitter url.')