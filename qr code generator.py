import qrcode

#taking upi id from the user
#upi://pay?pa=UPI_ID&pn=NAME&am=AMOUNT&cu=CURRENCY&tn=MESSAGE ( format for upi id )

upi_id = input("Enter your UPI ID ")

#defining the payment url , it is adjustable according to different payment apps

phone_pe = f'upi://pay?id={upi_id}&pn=Recipient%20Name&mc=1234'
google_pe=f'upi://pay?id={upi_id}&pn=Recipient%20Name&mc=1234'
paytm_url = f'upi://pay?id={upi_id}&pn=Recipient%20Name&mc=1234'

#qrcode for each payment app

phonepe_qr = qrcode.make(phone_pe)
googlepe_qr = qrcode.make(google_pe)
paytm_qr = qrcode.make(paytm_url)

phonepe_qr.show()
googlepe_qr.show()
paytm_qr.show()
