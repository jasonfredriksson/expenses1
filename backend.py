import sqlite3

def create_table():
	conn=sqlite3.connect("finanzas.db")
	cur=conn.cursor()
	cur.execute("CREATE TABLE if NOT EXISTS finanza (iden INT, fecha DATE, monto REAL, categoria TEXT, descripción TEXT, necesidad INT, importancia INT)")
	conn.commit()
	conn.close()

def insert(iden,fecha,monto,categoria,descripcion,necesidad,importancia):
	conn=sqlite3.connect("finanzas.db")
	cur=conn.cursor()
	cur.execute("INSERT INTO finanza VALUES (?,?,?,?,?,?,?)",(iden,fecha,monto,categoria,descripcion,necesidad,importancia))
	conn.commit()
	conn.close()

def view():
	conn=sqlite3.connect("finanzas.db")
	cur=conn.cursor()
	cur.execute("SELECT * FROM finanza")
	rows=cur.fetchall()
	conn.close()
	return rows

def search(iden="",fecha="",monto="",categoria="",descripcion="",necesidad="",importancia=""):
	conn=sqlite3.connect("finanzas.db")
	cur=conn.cursor()
	cur.execute("SELECT * FROM finanza WHERE iden=? OR fecha=? OR monto=? OR categoria=? OR descripción=? OR necesidad=? OR importancia=?",(iden,fecha,monto,categoria,descripcion,necesidad,importancia))
	rows=cur.fetchall()
	conn.close()
	return rows

def delete(iden):
	conn=sqlite3.connect("finanzas.db")
	cur=conn.cursor()
	cur.execute("DELETE FROM finanza WHERE iden=?",(iden,))
	conn.commit()
	conn.close()

def update(iden,fecha,monto,categoria,descripcion,necesidad,importancia):
	conn=sqlite3.connect("finanzas.db")
	cur=conn.cursor()
	cur.execute("UPDATE finanza SET fecha=?, monto=?, categoria=?, descripción=?, necesidad=?, importancia=? WHERE iden=?",(fecha,monto,categoria,descripcion,necesidad,importancia,iden))
	conn.commit()
	conn.close()	
