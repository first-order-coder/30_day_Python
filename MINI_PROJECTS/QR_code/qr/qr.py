import qrcode

LINK = input('Enter the Link:>')

features = qrcode.QRCode(version=1, box_size=40, border=3)
features.add_data(LINK)
features.make(fit=True)

# generate_image = qrcode.make('GINURA AMARASENA')
generate_image = features.make_image(fill_color='black', back_color='White')
generate_image.save('2.png')

