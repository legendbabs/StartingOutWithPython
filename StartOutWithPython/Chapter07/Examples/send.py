def send(name, website=None, verbose=False):
	
	if website != None:
		return f"You are welcome {name}, you have just log on to\n{website}"
	else:
		return f"You are welcome {name}!"
		
	if verbose:
		r = requests.get("https://www.goal.com")
		return r
		
	else:
		return "Website error"
		
		
res = send("Tunde Muhamed", verbose=True)
print(res)
		
		