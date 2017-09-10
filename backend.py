import sqlite3

class Database:

	def __init__(self, db):
		self.conn=sqlite3.connect(db)
		self.cur=self.conn.cursor()
		self.cur.execute("CREATE TABLE if NOT EXISTS finanza (iden INT, fecha DATE, monto REAL, categoria TEXT, descripción TEXT, necesidad INT, importancia INT)")
		self.conn.commit()

	def insert(self,iden,fecha,monto,categoria,descripcion,necesidad,importancia):
		self.cur.execute("INSERT INTO finanza VALUES (?,?,?,?,?,?,?)",(iden,fecha,monto,categoria,descripcion,necesidad,importancia))
		self.conn.commit()

	def view(self):
		self.cur.execute("SELECT * FROM finanza")
		rows=self.cur.fetchall()
		return rows

	def search(self,iden="",fecha="",monto="",categoria="",descripcion="",necesidad="",importancia=""):
		self.cur.execute("SELECT * FROM finanza WHERE iden=? OR fecha=? OR monto=? OR categoria=? OR descripción=? OR necesidad=? OR importancia=?",(iden,fecha,monto,categoria,descripcion,necesidad,importancia))
		rows=self.cur.fetchall()
		return rows

	def delete(self,iden):
		self.cur.execute("DELETE FROM finanza WHERE iden=?",(iden,))
		self.conn.commit()

	def update(self,iden,fecha,monto,categoria,descripcion,necesidad,importancia):
		self.cur.execute("UPDATE finanza SET fecha=?, monto=?, categoria=?, descripción=?, necesidad=?, importancia=? WHERE iden=?",(fecha,monto,categoria,descripcion,necesidad,importancia,iden))
		self.conn.commit()

	def __del__(self):
		self.conn.close()


#create_table()
#insert(4,"6/28/2017",22.4,"alimento","golosinas",1,4)
#insert(5,"6/29/2017",200,"alimento","verduleria",10,10)
#insert(6,"6/29/2017",100,"limpieza","jabón lavarropas",10,10)
#print(view())
#update(4,"6/27/2017",22.4,"alimento","golosinas",3,5)
#delete(6)

