import mysql.connector


class PersonDa:
	def connect(self):
		self.connection = mysql.connector.connect(
			host='localhost',
			user='root',
			password='barbod.87.08',
			database='gks'
		)
		self.cursor = self.connection.cursor()


	def disconnect(self, commit=False):
		if commit:
			self.connection.commit()
		self.cursor.close()
		self.connection.close()


	def save(self, person):
		self.connect()
		self.cursor.execute(
			"INSERT INTO user_tbl (id,name,family,phone) VALUES (""%s,%s,%s,%s,%s,%s)",
			[person.id, person.name, person.family, person.username, person.password, person.phone])
		self.disconnect(True)
