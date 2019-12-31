# Python QR Code Reader
---
Python program built using [pyzbar](https://pypi.org/project/pyzbar/) and [imutils](https://pypi.org/project/imutils/) while following this [tutorial](https://www.pyimagesearch.com/2018/05/21/an-opencv-barcode-and-qr-code-scanner-with-zbar/).

The program is fairly simple: using your webcam it will detect barcodes and save them to a CSV file without storing any duplicates.

When a barcode is found it'll be printed as an output then saved to file.

To run the program you simply type: ```python3 main.py``` although you do need to install some modules.
* need to install **zbar** via Brew (MacOS), apt-get (Linux) or for Windows using the [installer](http://zbar.sourceforge.net/download.html)
  * Brew: ```brew install zbar```
  * apt-get: ```sudo apt-get install libzbar0```
* ```pip3 install pyzbar```
* ```pip3 install imutils```
