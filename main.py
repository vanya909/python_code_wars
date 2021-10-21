from sixth_kyu import ASCII_hex_converter

if __name__ == '__main__':
    s = ASCII_hex_converter.Converter.to_hex("Hello, this is my app!")
    s = ASCII_hex_converter.Converter.to_ascii(s)

    print(s)
