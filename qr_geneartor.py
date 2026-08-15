import qrcode

data = "https://example.com"

qr = qrcode.make(data)

qr.save("my_qr.png")

print("QR Code generated successfully!")