# The contact class holds contact information

class Contact:
	# The __init__ method initializes the attributes
	def __init__(self, name, phone, email):
		self.__name = name
		self.__phone = phone
		self.__email = email

	# The set_name method sets the name attributes
	def set_name(self, name):
		self.__name = name

	# The set_phone method sets the phone attributes
	def set_phone(self, phone):
		self.__phone = phone

	# The set_email method sets the email attributes
	def set_email(self, email):
		self.__email = email

	# The get_name method returns the name attributes
	def get_name(self):
		return self.__name

	# The get_phone method returns the phone attributes
	def get_phone(self):
		return self.__phone

	# The get_email method returns the email attributes
	def get_email(self):
		return self.__email

	# The __str__method returns the object's state
	def __str__(self):
		return 'Name: ' + self.__name + \
		'\nPhone: ' + self.__phone + \
		'\nEmail: ' + self.__email

