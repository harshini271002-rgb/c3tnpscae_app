import qrcode

# The network URL for the Streamlit app based on the previous output
url = "http://10.159.152.20:8502"

print(f"Generating QR Code for: {url}")

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=4,
)

qr.add_data(url)
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")
img.save("TNPSC_Quiz_QRCode.png")

print("QR Code generated successfully and saved as 'TNPSC_Quiz_QRCode.png'!")
