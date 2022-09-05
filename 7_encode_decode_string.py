"""
This problem was asked by Facebook.

Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, count the number of ways it can be decoded.

For example, the message '111' would give 3, since it could be decoded as 'aaa', 'ka', and 'ak'.

You can assume that the messages are decodable. For example, '001' is not allowed.
"""

def find_decode_count(input_string):
    print("\n")
    print(input_string)
    string_length = len(input_string)
    decode_count = 1
    if input_string[0] == '0':
        print("Message Not Decodable")
        return -1
    for i in range(string_length):
        if i + 1 < string_length:
            given_int = int(input_string[i] + input_string[i+1])
            if given_int <= 26:
                print(given_int)
                decode_count += 1
    return decode_count


if __name__ == "__main__":
    input_string = '111'
    print(find_decode_count(input_string))

    input_string = '001'
    print(find_decode_count(input_string))

    input_string = '926'
    print(find_decode_count(input_string))

    input_string = '968'
    print(find_decode_count(input_string))

