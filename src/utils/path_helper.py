import os
from os import path

absolute_path = path.dirname(path.realpath(__file__))


def project_path(*sub_folders):
	"""Returns the path of the project."""
	return path.join(absolute_path, "..", "..", *sub_folders)


def combine_path(original_path, *args):
	"""
	Concatenates the given path with additional path components.
	"""
	return path.join(original_path, *args)


if __name__ == '__main__':
	print(os.listdir(project_path()))
