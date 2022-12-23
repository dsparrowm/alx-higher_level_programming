#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    if len(sys.argv) == 1:
        print('{:d} arguments.'.format(0))
    else:
        my_list = list(sys.argv)
        my_list.remove(sys.argv[0])
        if len(my_list) == 1:
            print('{:d} argument:'.format(1))
            print('{:d}: {}'.format(1, my_list[0]))
        else:
            print('{:d} arguments:'.format(len(sys.argv) - 1))
            for i, arg in enumerate(my_list, start=1):
                print('{}: {}'.format(i, arg))
