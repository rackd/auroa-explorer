import json
import logging

class _Parser:
	def __init__(self, data):
		self.ObservationTime = data["Observation Time"]
		self.ForecastTime = data["Forecast Time"]
		self.DataFormat = data["Data Format"]
		self.Coordinates = data["coordinates"]
		self.Type = data["type"]

class StringParser(_Parser):
	def __init__(self, json_str):
		try:
			data = json.loads(json_str)
			logging.info("Successfully loaded JSON data from string")
		except (ValueError, TypeError):
			logging.info("Failed to load JSON data from file")
			raise

		super().__init__(data)

class FileParser(_Parser):
	def __init__(self, fp):
		try:
			data = json.load(fp)
			logging.info("Successfully loaded JSON data from string")
		except (ValueError, TypeError):
			logging.info("Failed to load JSON data from file")
			raise

		super().__init__(data)