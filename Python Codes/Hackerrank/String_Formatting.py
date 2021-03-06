def print_formatted(number):
    for n in range(number):
        # oct_len = len(str(oct(number)).replace('0',''))
        bin_len = len(str(bin(number)).replace('0b',''))
        HEX = hex(n+1)[2:]
        OCT = oct(n+1)[2:]
        BIN = bin(n+1)[2:]
        print (str(n+1).rjust(bin_len) ,  OCT.rjust(bin_len).upper() , HEX.rjust(bin_len).upper() , BIN.rjust(bin_len))     

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)

# ALTERNATE:
# ===============

# STDIN = int(input())
# w = len(str(bin(STDIN)).replace('0b',''))

# for i in range(1, STDIN+1):
#     b = bin(int(i)).replace('0b','').rjust(w, ' ')
#     o = oct(int(i)).replace('0','', 1).rjust(w, ' ')
#     h = hex(int(i)).replace('0x','').upper().rjust(w, ' ')
#     j = str(i).rjust(w, ' ')
#     print (j, o, h, b)

# TESTCASE:
# ==============

    #  1      1      1      1
    #  2      2      2     10
    #  3      3      3     11
    #  4      4      4    100
    #  5      5      5    101
    #  6      6      6    110
    #  7      7      7    111
    #  8     10      8   1000
    #  9     11      9   1001
    # 10     12      A   1010
    # 11     13      B   1011
    # 12     14      C   1100
    # 13     15      D   1101
    # 14     16      E   1110
    # 15     17      F   1111
    # 16     20     10  10000
    # 17     21     11  10001
    # 18     22     12  10010
    # 19     23     13  10011
    # 20     24     14  10100
    # 21     25     15  10101
    # 22     26     16  10110
    # 23     27     17  10111
    # 24     30     18  11000
    # 25     31     19  11001
    # 26     32     1A  11010
    # 27     33     1B  11011
    # 28     34     1C  11100
    # 29     35     1D  11101
    # 30     36     1E  11110
    # 31     37     1F  11111
    # 32     40     20 100000
    # 33     41     21 100001
    # 34     42     22 100010
    # 35     43     23 100011
    # 36     44     24 100100
    # 37     45     25 100101
    # 38     46     26 100110
    # 39     47     27 100111
    # 40     50     28 101000
    # 41     51     29 101001
    # 42     52     2A 101010
    # 43     53     2B 101011
    # 44     54     2C 101100
    # 45     55     2D 101101
    # 46     56     2E 101110
    # 47     57     2F 101111
    # 48     60     30 110000
    # 49     61     31 110001
    # 50     62     32 110010
    # 51     63     33 110011
    # 52     64     34 110100
    # 53     65     35 110101
    # 54     66     36 110110
    # 55     67     37 110111
    # 56     70     38 111000
    # 57     71     39 111001
    # 58     72     3A 111010
    # 59     73     3B 111011
    # 60     74     3C 111100
    # 61     75     3D 111101
    # 62     76     3E 111110
    # 63     77     3F 111111