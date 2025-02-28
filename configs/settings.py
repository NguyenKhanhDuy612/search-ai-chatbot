import os

import tomli

from utils.path_helper import project_path

# Load TOML config as fallback
config_path = project_path('development.toml')
with open(config_path, "rb") as f:
    toml_config = tomli.load(f)

# API Keys
google_api_key = os.getenv("GOOGLE_API_KEY", toml_config["API_KEYS"]["GOOGLE_API_KEY"])

# LangSmith settings
langsmith_tracing = os.getenv("LANGCHAIN_TRACING_V2", str(toml_config["LANGSMITH"]["LANGCHAIN_TRACING_V2"])).lower() == "true"
langsmith_endpoint = os.getenv("LANGCHAIN_ENDPOINT", toml_config["LANGSMITH"]["LANGCHAIN_ENDPOINT"])
langsmith_api_key = os.getenv("LANGCHAIN_API_KEY", toml_config["LANGSMITH"]["LANGCHAIN_API_KEY"])
langsmith_project = os.getenv("LANGCHAIN_PROJECT", toml_config["LANGSMITH"]["LANGCHAIN_PROJECT"])

# Model settings
temperature = float(os.getenv("TEMPERATURE", str(toml_config["MODEL_SETTINGS"]["TEMPERATURE"])))
max_tokens = int(os.getenv("MAX_TOKENS", str(toml_config["MODEL_SETTINGS"]["MAX_TOKENS"])))
model_name = os.getenv("MODEL_NAME", toml_config["MODEL_SETTINGS"]["MODEL_NAME"])
gemini_model = os.getenv("GEMINI_MODEL", toml_config["MODEL_SETTINGS"]["GEMINI_MODEL"])

# Vector store settings
chroma_persist_directory = os.getenv("CHROMA_PERSIST_DIRECTORY", toml_config["VECTOR_STORE"]["CHROMA_PERSIST_DIRECTORY"])
collection_name = os.getenv("COLLECTION_NAME", toml_config["VECTOR_STORE"]["COLLECTION_NAME"])
