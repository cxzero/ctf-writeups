#!/usr/bin/env python3
import requests

def get_param():
	auth_token = [38, 0, 0, 60, 93, 49, 50, 95, 25, 22, 45, 71, 47, 94, 60, 54, 45, 70]
	salt = bytes("RheO5PB6mfL5N3YBH45e5XuCEaWpvWUFESqTYnZk", 'utf-8')

	param = ''
	for i in range(0, len(auth_token)):
		param += chr(auth_token[i] ^ salt[i % len(salt)])

	return param

def get_user_agent():
	a1 = bytes("RheO5PB6mfL5N3YBH45e5XuCEaWpvWUsdgdedgdrddf", 'utf-8')
	a2 = bytes("Thisnewuseragent", 'utf-8')

	user_agent = ''
	for i in range(0, len(a2)):
		user_agent += chr(a2[i] & a1[i % len(a1)])	

	return user_agent


if __name__ == "__main__":
	param = get_param()
	user_agent = get_user_agent()
	print("param =", param)
	print("user_agent =", user_agent)

	headers = {
		"User-Agent": user_agent
	}

	url = "https://teambounters.com/shapa.php?{param}=givemeflag".format(param = param)
	print(url)

	r = requests.get(url=url, headers=headers)
	print(r.text)
	# Flag{shapitflagXWs4rg0Ld0LrWxThBkwt}
