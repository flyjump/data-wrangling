from import_config import api_login
import sys


def main(env):
    config = api_login(env)
    print(config)


if __name__ == '__main__':
    if len(sys.argv) > 1:
        env = sys.argv[1]
    else:
        env = 'TEST'
    main(env)
