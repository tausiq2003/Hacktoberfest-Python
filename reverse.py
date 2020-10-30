import sys
if len(sys.argv) > 1:
    for char in sys.argv[1][::-1]:
        sys.stdout.write(char)
    sys.stdout.write('\n')
