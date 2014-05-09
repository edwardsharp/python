import argparse

parser = argparse.ArgumentParser(prog='PROG')
parser.add_argument('--host', default='host1', help='pass along a host label to update')

args = vars(parser.parse_args())
print(args['host'])