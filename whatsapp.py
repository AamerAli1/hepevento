from heyoo import WhatsApp

def sendWhatsapp(name,phonenumber):
    messenger = WhatsApp("EAALRZBE7YAZCUBAGvtPRSVM6K1pyZBrgHjavqQcY5hivhrzHq0iZBHjkEJA5Kd1zQz7Svr9WOTxFPtOMOthETyREZAXVXzK2kUG19PtcMLxlw0btZCZBO2K21jAZChWTweCtWL2AJZCBYZCPAy8SUXUi3WEClIBfurwHyEf6BNyzqrILIzrDtcZBmaUmhqZC9LgAxsUqvJjZAuH4kwwZDZD", '110395828445215')
    name=name
    phonenumber=phonenumber
    message= 'Dear ' + name + ', here is your qr code '
    image= "QRs/ " + name + '.png'
    
    messenger.send_message(message, phonenumber)
    messenger.send_image(image,phonenumber)
    
    

