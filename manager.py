import os
import toml

with open('config.toml') as conf_file:
    config = toml.loads(conf_file.read())

if not os.path.isdir(config['logging']['dir']):
    os.makedirs(config['logging']['dir'])


from Package import module as module
from AnotherPackage import module as another_module

if __name__ == '__main__':
    module.do_something()
    another_module.do_something()