class Bits():
    def __init__(self):
        pass

    
    @staticmethod
    def to_bits(msg: str, form='cont') -> str:
        bits8 = []
        
        for letter in msg:
            numeric = ord(letter)
            bits = ''
            while numeric > 0:
                bits = str(numeric % 2) + bits
                numeric //= 2
            bits = bits.zfill(8)
            bits8.append(bits)
        
        if form == 'cont':
            result = "".join(bits8)
        elif form == 'sep':
            result = " ".join(bits8)
        elif form =='list':
            result = bits8
        else:
            raise ValueError('Possible values are: cont, sep, list')
        return result


    @staticmethod
    def from_bits(bits: str) -> str:
        raise NotImplementedError()


    @staticmethod
    def to_base64(msg: str) -> str:
        if msg == '':
            return ''
        bits = Bits.to_bits(msg)
        splitted = []
        prev = 0
        padding = 0
        for i in range(6,len(bits)+1, 6):
            splitted.append(bits[prev:i])
            prev = i
        if prev != len(bits):
            last = bits[prev:]
            while len(last) < 6:
                last += '00'
                padding += 1
            splitted.append(last)

        encoded = ''
        for bit6 in [int(x, 2) for x in splitted]:
            converted = ''
            if bit6 <= 25:
                converted = chr(65+bit6)
            elif bit6 <= 51:
                converted = chr(97+bit6-26)
            elif bit6 <= 61:
                converted = str(bit6-52)
            elif bit6 == 62:
                converted = '+'
            else:
                converted = '/'
            encoded += converted
        for _ in range(padding):
            encoded += '='

        return encoded

    @staticmethod
    def from_base64(msg: str) -> str:
        raise NotImplementedError()
