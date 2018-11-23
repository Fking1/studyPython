import pymysql.cursors

connect = pymysql.connect(host='localhost',user='root',password='123456',db='spring',charset='utf8')
# 获取会话指针
cursor = connect.cursor()
sql = ''
cursor.execute(sql);

connect.commit()
connect.close()