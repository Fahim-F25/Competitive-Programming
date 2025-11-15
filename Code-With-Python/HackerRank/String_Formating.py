def print_formatted(number):
    width = len(format(number,'b'))
    for i in range(1,number+1):
        d = str(i).rjust(width)
        o = format(i,'o').rjust(width)
        x = format(i,'X').rjust(width)
        b = format(i,'b').rjust(width)
        print(f"{d} {o} {x} {b}")
if __name__ == '__main__':
    n = int(input())
    print_formatted(n)