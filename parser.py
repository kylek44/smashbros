import serial
import sys

args = sys.argv
packet_size = 64
single_bit = 1


def update_0th_or_1st_byte(b):
    return b[3:]


def update_left_stick(b1, b2):
    sideways = update_2nd_byte(b1)
    if sideways == 0:
        sideways = update_3rd_byte(b2)
    return '{:03b}'.format(sideways)


def update_2nd_byte(b):
    print(b)
    if b[0] == '0' and b[1:] != '1111111':
        return 1
    if b[0] == '1' and b[1:] != '0000000':
        return 2
    return 0


def update_3rd_byte(b):
    print(b)
    if b[0] == '1':
        return 3
    if b[0] == '0' and b[1:] != '1111111':
        return 4
    return 0


def update_4th_byte(b):
    print(b)
    if b[0] == '0' and b[1:] != '1111111':
        return '{:02b}'.format(1)
    if b[0] == '1' and b[1:] != '0000000':
        return '{:02b}'.format(2)
    return '{:02b}'.format(0)


def update_5th_byte(b):
    print(b)
    if b[0] == '1' and b[1:] != '0000000':
        return '{:02b}'.format(1)
    if b[0] == '0' and b[1:] != '1111111':
        return '{:02b}'.format(2)
    return '{:02b}'.format(0)


def update_6th_or_7th_byte(b):
    print(b)
    if b != '00000000':
        return '1'
    return '0'


def split_bytes(b):
    i_bytes = []
    s = ''
    for i in range(len(b)):
        if i > 0 and i % 8 == 0:
            i_bytes.append(s[:])
            s = ''
        s += b[i]
    return i_bytes


# def reduce_bytes(b):
#     n = update_0th_or_1st_byte(b[0]) + update_0th_or_1st_byte(b[1])
#     n += update_left_stick(b[2], b[3])
#     n += update_4th_byte(b[4])
#     n += update_5th_byte(b[5])
#     n += update_6th_or_7th_byte(b[6])
#     n += update_6th_or_7th_byte(b[7])
#     return n
def reduce_bytes(b):
    return [update_0th_or_1st_byte(b[0]), update_0th_or_1st_byte(b[1]), update_left_stick(b[2], b[3]), update_4th_byte(b[4]), update_5th_byte(b[5]), update_6th_or_7th_byte(b[6]), update_6th_or_7th_byte(b[7])]


if len(args) > 2:
    input_file_name = args[1]
    output_file_name = args[2]
    input_file = open(input_file_name, 'r')
    output_file = open(output_file_name, 'w')

    for line in input_file:
        line = line.strip()
        input_bytes = line.split(' ')
        new_bytes = reduce_bytes(input_bytes)
        print(' '.join(new_bytes))

    input_file.close()
    output_file.close()

    # with open(args[2]) as out:
    #     bit = arduino.read(single_bit)
    #     while bit[0] != ' ':
    #         bit = arduino.read(single_bit)
    #     while True:
    #         bits = arduino.read(packet_size)
    #         bits = bits.decode('utf-8', errors='ignore')
    #         input_bytes = split_bytes(bits)
    #         new_bytes = reduce_bytes(input_bytes)
    #         print(' '.join(input_bytes))
    #         # for x in input_bytes:
    #         #     print(x, end=' ')
    #         # print()
    #         print(' '.join(new_bytes))
    #         out.write(new_bytes)
    #         out.write('\n')
