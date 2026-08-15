import cv2

image = cv2.imread("my_qr.png")

if image is None:
    print("QR image not found")
else:
    detector = cv2.QRCodeDetector()
    data, points, _ = detector.detectAndDecode(image)

    if data:
        print("QR Data:", data)
    else:
        print("QR Code not detected")