import yaml

with open("app/resources/config.yml", '+r') as config:
    cfg = yaml.load(config, Loader=yaml.FullLoader)

db_config = cfg['database']
auth_config = cfg['auth']
prj_config = cfg['project']