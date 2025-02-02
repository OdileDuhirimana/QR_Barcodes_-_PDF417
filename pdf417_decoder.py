from asposebarcode import BarcodeRecognition
reader = BarcodeRecognition.BarCodeReader("./image01.png", BarcodeRecognition.DecodeType.ALL_SUPPORTED_TYPES)

recognized_results = reader.read_bar_codes()

for barcode in recognized_results:
    print(barcode.code_text)
