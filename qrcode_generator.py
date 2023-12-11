import qrcode


class MyQrCode:

    def __init__(self, q_size, q_padding):
        self.qr = qrcode.QRCode(box_size=q_size, border=q_padding)

    def create_qrcode(self, file_name, fg_color, bg_color):

        user_input = "https://www.google.com"

        try:
            self.qr.add_data(user_input)
            qr_image = self.qr.make_image(fill_color=fg_color, back_color=bg_color)
            qr_image.save("test_qr.png")

        except Exception as e:
            print(f"Error: {e}")


def generate_qrcode():
    my_qrcode = MyQrCode(10, 2)
    my_qrcode.create_qrcode("test_qr.png", "blue", "white")


if __name__ == '__main__':
    generate_qrcode()

