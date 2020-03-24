import configparser

def config_parser(config_file_path):
    """
    Initializes the configuration

    Args:
        config_file_path:str: Path to .ini configuration file
    """

    # asserting configuration file has the correct extension
    path = config_file_path.split('.')
    assert(path[len(path)-1] == 'ini')

    config = configparser.ConfigParser()
    config.read(config_file_path)
    return config