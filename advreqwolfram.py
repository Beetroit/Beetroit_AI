import requests
while True:
	url="https://api.wolframalpha.com/v2/query?"
	appid="GU4A4A-AHRUHHWXU3"
	quest= "reset bios password"
	#format="plaintext" #who discovered penicillin"
	output="JSON"
	param={"input":quest,"format":"plaintext","output":"JSON","appid":appid,"includepodid":"Result"}#"reinterpret":"true"}
	r=requests.get(url=url,params=param)
	print(r.url)
	#if r.json().get("queryresult").get("success"):
		#print(r.json().get("queryresult",None)["pods"][0]["subpods"][0]["plaintext"])
	print(r.text)
	break
#https://api.wolframalpha.com/v2/query?input=How+would+you+describe+cancer&format=plaintext&output=JSON&appid=DEMO