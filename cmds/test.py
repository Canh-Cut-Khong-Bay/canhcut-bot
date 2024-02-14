config = {
  "cmd": "test",
}
"""
permission in next update...

input: /test1 11 11 11
output: bonk !!! ('11', '11', '11')

that's with args
or not args

def main(api, dataFB, replyToID):
	a="bonk !!!"
	b=api.send(dataFB, a, replyToID)
	
input: /test1 11 11 11
output: bonk !!!
"""

def main(api, dataFB, replyToID, *args):
	a=f"bonk !!! {args}"
	b=api.send(dataFB, a, replyToID)