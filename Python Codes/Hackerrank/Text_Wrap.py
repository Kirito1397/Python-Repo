import textwrap

def wrap(string, max_width):
    wrapper = textwrap.TextWrapper(width = max_width)
    final_strings = wrapper.wrap(text=string)
    return "\n".join(final_strings[:])

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)