def get_avatar(backend, strategy, details, response, user=None,
				*args, **kwargs):

	url = None
	if backend.name == 'facebook':
		url = 'http://graph.facebook.com/%s/picture?type=large'%response['id']
	if backend.name == 'twitter':
		url = response.get('profile_image_url','').replace('normal','')

	if url:
		print '='*90
		print url
		print '='*90
		user.avatar = url
		user.save()