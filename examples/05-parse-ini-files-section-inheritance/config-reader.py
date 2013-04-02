
from pyconfigini import parse_ini

config = parse_ini('config.ini', 'production')

print config.value
print config.section1.value


config = parse_ini('config.ini', 'development')

print config.value
print config.section1.value
