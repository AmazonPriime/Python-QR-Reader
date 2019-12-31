from imutils.video import VideoStream
from pyzbar import pyzbar
import imutils, os

filename = "barcodes.csv"

# turn on the webcam and if there's a barcodes.csv load them into the found set
# otherwise use an empty set and then load the CSV so we can append to it
print("Turning on webcam...")
vs = VideoStream(src = 0).start()
print("Webcam ready:")

found = ()
if os.path.exists(filename):
	with open(filename) as f: found = set(f.readlines())

csv = open(filename, "a", buffering = 1)

# load each frame from the webcam and try and find barcodes, if some
# are found then go through them all decoding to UTF-8 and if they are
# not in the found set then add them to the CSV and the found set
while True:
	frame = vs.read()
	frame = imutils.resize(frame, width = 400)

	barcodes = pyzbar.decode(frame)

	barcodeData = ""
	for barcode in barcodes:
		barcodeData = barcode.data.decode("utf-8") + "\n"
		if barcodeData not in found:
			print("FOUND: %s" % barcodeData[:-1])
			csv.write("%s" % barcodeData)
			found.add(barcodeData)

csv.close()
vs.stop()
