import segno 

def createqr(id,name,phonenumber,email):
    qrcodename = 'QRs/' + name + '.png'
    message = "id:" + str(id) + "\nname: " + str(name) + "\nMobile: " + str(phonenumber) + "\nemail: " + str(email)
    qrcode = segno.make(message,micro=False)
    qrcode.save(qrcodename)



