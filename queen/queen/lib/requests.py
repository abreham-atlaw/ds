from typing import *
from abc import ABC, abstractmethod

import requests


class Request(ABC):

	class Method:
		GET = 'get'
		POST = 'post'

	def __init__(self, url, params=None, data=None, method=None, headers=None):
		self.__url = url
		self.__params = params
		self.__method = method
		self.__data = data
		self.__headers = headers
		self.__r = None
		if method is None:
			self.__method = Request.Method.GET

	def __get(self):
		return requests.get(self.__url, params=self.__params, headers=self.__headers)

	def __post(self):
		return requests.post(self.__url, json=self.__data, headers=self.__headers)

	def __execute(self):
		if self.__method == Request.Method.GET:
			return self.__get()
		return self.__post()

	def call(self):
		self.__r = self.__execute()

	def get_value(self, json=True):
		if json:
			return self.__r.json()
		return self.__r.text


