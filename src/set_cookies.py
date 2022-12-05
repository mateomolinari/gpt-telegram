def set_cookies(driver):
	driver.add_cookie({
		'name': '__Host-next-auth.csrf-token',
		'value': '',
		'domain': 'chat.openai.com',
		'path': '/',
		'secure': True,
		'httpOnly': True,
		'sameSite': 'Lax',
		'expires': 2633040000
	})
	driver.add_cookie({
		'name': '__Secure-next-auth.callback-url',
		'value': 'https%3A%2F%2Fchat.openai.com%2F',
		'domain': 'chat.openai.com',
		'path': '/',
		'secure': True,
		'httpOnly': True,
		'expires': 2633040000,
		'sameSite': 'Lax'
	})
	driver.add_cookie({
		'name': '__Secure-next-auth.session-token',
		'value': '',
		'domain': 'chat.openai.com',
		'path': '/',
		'secure': True,
		'httpOnly': True,
		'sameSite': 'Lax',
		'expires': 2633040000
	})
	driver.add_cookie({
		'name': '',
		'value': '',
		'domain': '.openai.com',
		'path': '/',
		'secure': False,
		'httpOnly': False,
		'sameSite': 'None',
		'expires': 2633040000
	})

	