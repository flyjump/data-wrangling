from configparser import ConfigParser
import sys

def get_config(env):
    config = ConfigParser()
    if env == 'PROD':
        config.read(['config/production.cfg'])
    elif env == 'TEST':
        config.read(['config/test.cfg'])
    else:
        config.read(['config/development.cfg'])
    return config


def api_login(env_):
    config = get_config(env_)
    my_client = get_client(config.get('api_login', 'user'),
                           config.get('api_login', 'pass'))
    return my_client


def get_client(user, auth_key):
    return {'user': user,
            'auth_key': auth_key}


if __name__ == '__main__':
    if len(sys.argv) > 1:
        env = sys.argv[1]
    else:
        env = 'TEST'
    print(api_login(env))
