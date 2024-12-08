from configparser import ConfigParser
#from lib.logger_opt import *

config_file = './config.ini'
config = ConfigParser()
config.read(config_file)

version = ''

param_img_w = None 
param_img_h = None 

def get_version():
    return version

def check_config_section():
    if not config.has_section('common'):
        config.add_section('common')

    if not config.has_section('param'):
        config.add_section('param')

    config.write(open(config_file, 'w'))

def get_config():
    global version, param_img_w, param_img_h
    try:
        version = config.get('common', 'version')
    except Exception as e:
        logger.warning(e)
        version = ''

    try:
        param_img_w = config.get('param', 'img_w')
    except Exception as e:
        logger.warning(e)
        param_img_w = ''

    try:
        param_img_h = config.get('param', 'img_h')
    except Exception as e:
        logger.warning(e)
        param_img_h = ''

def reload_config():
    check_config_section()
    get_config()

if __name__ == '__main__':
    reload_config()
