from heyoo import WhatsApp

def sendWhatsapp(name,phonenumber):
    messenger = WhatsApp("EAALRZBE7YAZCUBADEDZADxFbNw94g1ISHQZA3qDMT8ImbhwmPPB8jP7IOZARAxU2bZBlnb3LQZAZCGZCZAJYFZCeylWW6GclRIP06qFogv5QJ5BsP5cPWe2QKhrzMWjQnhwKwUXHNlMTxqeYVp4ZB56d1CZBof0PwELDMDeKIioclqBZBxjWAkGWHWT5rM7slUkl1EvfIZCqpNErg2ZAeQZDZD", '110395828445215')
    name=name
    phonenumber=phonenumber
    message= 'Dear ' + name + ', here is your qr code '
    image= "QRs/ " + name + '.png'
    
    messenger.send_message(message, phonenumber)
    messenger.send_image(image,phonenumber)
    