import logging

from src.configs.flask_config import DefaultConfig
from src.configs.init_app import create_app
from src.configs.log_setup import setup_logging
from src.configs.settings import app_port

log_level = logging.INFO
config = DefaultConfig
setup_logging(level=log_level)
app = create_app(config_class=config)

if __name__ == "__main__":
	app.logger.debug('STARTING APP')
	app.run(host='0.0.0.0', port=app_port)
