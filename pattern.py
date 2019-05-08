import string
import argparse

def main():
    args = input_args()
    if args.query:
        print(f"[!] Pattern found at: {find_offset(args.length, args.query)} bytes")
    else:
        print(create_pattern(args.length))

def input_args():
    parser = argparse.ArgumentParser()

    parser.add_argument('-l',
                        '--length',
                        type=int,
                        required=True,
                        help='Length of pattern to create')

    parser.add_argument('-q',
                        '--query',
                        type=string,
                        required=False,
                        help='Optional: Query string from EIP to locate in pattern')
    
    return parser.parse_args()

def create_pattern(length):
    index_up, index_down, int_index = 0, 0, 0
    int_list = list(range(0, 10))
    int_limit = len(int_list)-1 # 9
    char_list = string.ascii_lowercase
    char_limit = len(char_list)-1 # 25
    pattern = ''
    while len(pattern) < length:
        if int_index <= int_limit:
            new_sequence = char_list[index_up].capitalize() + char_list[index_down] + str(int_list[int_index])
            pattern = pattern + new_sequence
            int_index += 1
        else:
            int_index = 0
            if index_down <= char_limit:
                index_down += 1
            if index_down >= char_limit:
                index_down = 0
                index_up += 1
            if index_up > char_limit:
                index_up = 0
                    
    return pattern
    
def find_offset(length, query):
    return create_pattern(length).find(query)
    
def extend_pattern(pattern, upper, lower, integer):
    return pattern + upper.capitalize() + lower + str(integer)

if __name__ == "__main__":
    main()
