class Converter():
    @staticmethod
    def to_ascii(h):
        s = []

        for i in range(0, len(h), 2):
            s.append(chr(int(h[i:i+2], 16)))

        return ''.join(s)

    @staticmethod
    def to_hex(s):
        s = list(s)

        for i in range(0, len(s)):
            s[i] = hex(ord(s[i])).lstrip('0x')

        return ''.join(s)