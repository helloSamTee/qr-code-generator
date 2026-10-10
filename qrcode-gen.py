# import modules
import qrcode
from PIL import Image
import argparse

parser = argparse.ArgumentParser(description='Generate a QR code with an optional logo in the center.')
parser.add_argument('--logo', type=str, help='Path to the logo image file')
parser.add_argument('--url', required=True, type=str, help='URL to be encoded in the QR code')
parser.add_argument('--color', type=str, default='black', help='Color of the QR code')
parser.add_argument('--destination', type=str, default='qrcode', help='Destination file name for the QR code (excluding extension like .png)')
args = parser.parse_args()

# taking image which user wants 
# in the QR code center
logo_file_path = args.logo
# taking url or text
url = args.url
# taking color name from user
QRcolor = args.color
destination_file = args.destination

QRcode = qrcode.QRCode(
	error_correction=qrcode.constants.ERROR_CORRECT_H
)

# adding URL or text to QRcode
QRcode.add_data(url)

# generating QR code
QRcode.make()

# adding color to QR code
QRimg = QRcode.make_image(
	fill_color=QRcolor, back_color="white").convert('RGB')

if logo_file_path:
	logo = Image.open(logo_file_path)

	# taking base width
	basewidth = 100

	# adjust image size
	wpercent = (basewidth/float(logo.size[0]))
	hsize = int((float(logo.size[1])*float(wpercent)))
	logo = logo.resize((basewidth, hsize), Image.LANCZOS)

	# set size of QR code
	pos = ((QRimg.size[0] - logo.size[0]) // 2,
		(QRimg.size[1] - logo.size[1]) // 2)
	QRimg.paste(logo, pos)

# save the QR code generated
QRimg.save(destination_file + '.png')

print('QR code generated!')
