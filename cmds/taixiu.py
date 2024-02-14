config = {"cmd": "taixiu"}

# taixiu or big/small

import random as r

money = int(10000) # fake money, bot not have them !!!

def main(api, dataFB, replyToID, *args):
    x1 = r.randint(1, 6)
    
    if len(args) < 2:
        a.send(b, "thiếu kìa, nhớ là tài/xỉu rồi đến tiền cược", c)
        return
    a= args
    # print(a)
    # response for args ('tài', '1000')
    mean = a[0]
    mon= int(a[1])
    if mean == "tài" or mean == "xỉu":
        if x1 <= 3 and mean == "xỉu":
            monn = mon * 1.8
            api.send(dataFB, f"m thắng với {x1} và m nhận được {monn}", replyToID)
        elif x1 >= 4 and mean == "tài":
                monn = mon * 1.8
                api.send(dataFB, f"m thắng với {x1} và m nhận được {monn}", replyToID)
        else:
            monn = money - mon
            api.send(dataFB, f"m thua với {x1} và trừ {monn}", replyToID)
    else:
        api.send(dataFB, f"cak, {mean} là clgt", replyToID)
        
