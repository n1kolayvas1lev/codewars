# he rgb function is incomplete.
# Complete it so that passing in RGB decimal values
# will result in a hexadecimal representation being returned.
# Valid decimal values for RGB are 0 - 255.
# Any values that fall out of that range
# must be rounded to the closest valid value.
# Note: Your answer should always be 6 characters long,
# the shorthand with 3 will not work here.
# The following are examples of expected output values:
# rgb(255, 255, 255) # returns FFFFFF
# rgb(255, 255, 300) # returns FFFFFF
# rgb(0,0,0) # returns 000000
# rgb(148, 0, 211) # returns 9400D3

def rgb(r, g, b):
    rgb_ = [r, g, b]
    for i in range(len(rgb_)):
        if rgb_[i] < 0:
            rgb_[i] = 0
        elif rgb_[i] > 255:
            rgb_[i] = 255

    listofchars = [(hex(i)).lstrip('0x') if i > 9 else str(f'0{i}') for i in rgb_]
    result = ''.join(i for i in listofchars).upper()
    print(result)


if __name__ == '__main__':
    rgb(0, 0, 0)
    rgb(1, 2, 3)
    rgb(10, 20, 30)
    rgb(255, 255, 255)
    rgb(254, 253, 252)
    rgb(-20, 275, 125)
