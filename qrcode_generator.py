import qrcode


class MyQrCode:

    def __init__(self, q_size, q_padding):
        self.qr = qrcode.QRCode(box_size=q_size, border=q_padding)

    def create_qrcode(self, file_name, fg_color, bg_color):

        user_input = input("Enter data: ")

        try:
            self.qr.add_data(user_input)
            qr_image = self.qr.make_image(fill_color=fg_color, back_color=bg_color)
            qr_image.save(file_name)

        except Exception as e:
            print(f"Error: {e}")


def generate_qrcode():
    my_qrcode = MyQrCode(10, 2)
    file_name = input("Enter file name(without file extension): ")
    my_qrcode.create_qrcode(f'{file_name}.png', "blue", "white")


if __name__ == '__main__':
    generate_qrcode()

