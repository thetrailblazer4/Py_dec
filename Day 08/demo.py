import logging

logging.basicConfig(filename='demo.log', level=logging.INFO)


def logger(func):
	def log_func(*args):
		logging.info(f"Running '{func.__name__}' with arguments {args}")
		print(func(*args))

	return log_func


@logger
def add(a, b):
	return a + b

@logger
def sub(a, b):
	return a - b


sub(7,2)
