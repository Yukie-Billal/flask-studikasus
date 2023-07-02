import os

def get_env(name:str) -> str :
	return str(os.environ.get(name))