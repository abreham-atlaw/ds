from typing import *

import uuid

from datetime import datetime

"""
class Request:

	__tablename__ = "core_request"

	id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
	command = Column(String(), nullable=False)
	locked = Column(Boolean(), default=False, nullable=False)
	complete = Column(Boolean(), default=False, nullable=False)
	start_datetime = Column(DateTime(), nullable=False, default=datetime.now)


class Tokens(Model):
	token = Column(UUID(), primary_key=True, default=uuid.uuid4)
"""