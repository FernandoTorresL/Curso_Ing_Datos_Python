import yaml

__config = None

def config():

    global __config

    if not __config:
        with open('config.yaml', mode='r') as f:
            config = yaml.safe_load(f)

    return config
