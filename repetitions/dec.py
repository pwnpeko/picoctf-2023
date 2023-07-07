import base64

with open("enc_flag", "r") as f:
    asd = f.read()
    temp = asd
    for i in range(20):
        temp = base64.b64decode(temp)
        print(i, temp)
    # print(base64.b64decode(base64.b64decode(asd)))