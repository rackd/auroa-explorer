import logging
import constants

levels = [logging.NOTSET, logging.DEBUG, logging.INFO, logging.WARNING,
	logging.ERROR, logging.CRITICAL]

class OutputTypes:
	FILE = 0
	STREAM = 1
	FILE_AND_STREAM = 2

types = [OutputTypes.FILE, OutputTypes.STREAM, OutputTypes.FILE_AND_STREAM]

def init(log_level, output_type):
	if not isinstance(log_level, int):
		raise TypeError("'log_level' must be a numeric value.")
	elif not log_level in levels:
		raise TypeError("'log_level' must be a valid logging level.")
	elif not isinstance(log_level, int):
		raise TypeError("'output_type' must be a numeric value.")
	elif not output_type in types:
		raise TypeError("'output_type' must be a valid logging output type.")

	logger = logging.getLogger()
	formatter = logging.Formatter(constants.LOG_FORMAT)

	match output_type:
		case OutputTypes.FILE | OutputTypes.FILE_AND_STREAM:
			file_handler = logging.FileHandler(constants.LOG_FILE_NAME)
			file_handler.setFormatter(formatter)
			logger.addHandler(file_handler)
		case OutputTypes.STREAM | OutputTypes.FILE_AND_STREAM:
			stream_handler = logging.StreamHandler()
			stream_handler.setFormatter(formatter)
			logger.addHandler(stream_handler)
		
	return logger