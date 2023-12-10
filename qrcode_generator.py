import qrcode


class MyQrCode:

    def __init__(self, q_size, q_padding):
        self.qr = qrcode.QRCode(box_size=q_size, border=q_padding)