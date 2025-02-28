import os

import envtoml

from src.utils.path_helper import project_path


# Load TOML config as fallback
def set_env_vars(config_dict):
	for key, value in config_dict.items():
		if isinstance(value, dict):
			set_env_vars(value)
		else:
			os.environ[key] = str(value)


config_path = project_path('development.toml')
toml_config = envtoml.load(open(config_path))
set_env_vars(toml_config)

# API Keys
google_api_key = toml_config["API_KEYS"]["GOOGLE_API_KEY"]

# LangSmith settings
langsmith_vars = toml_config["LANGSMITH"]
langsmith_tracing = langsmith_vars["LANGCHAIN_TRACING_V2"]
langsmith_endpoint = langsmith_vars["LANGCHAIN_ENDPOINT"]
langsmith_api_key = langsmith_vars["LANGCHAIN_API_KEY"]
langsmith_project = langsmith_vars["LANGCHAIN_PROJECT"]

# Model settings
model_setting_vars = toml_config["MODEL_SETTINGS"]
temperature = model_setting_vars["TEMPERATURE"]
max_tokens = model_setting_vars["MAX_TOKENS"]
model_name = model_setting_vars["MODEL_NAME"]
gemini_model = model_setting_vars["GEMINI_MODEL"]

# Vector store settings
vector_store_vars = toml_config["VECTOR_STORE"]
chroma_persist_directory = vector_store_vars["CHROMA_PERSIST_DIRECTORY"]
collection_name = vector_store_vars["COLLECTION_NAME"]

# Flask settings
app_port = toml_config["FLASK"]["APP_PORT"]
flask_debug = toml_config["FLASK"].get("FLASK_DEBUG", False)
