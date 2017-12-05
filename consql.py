# import pymysql
#
# class db:
#     def con(self):
#         self.con = pymysql.connect("127.0.0.1", "root", "Aa000000", "mylchweb")
#         self.cursor = self.con.cursor()
#
#     def close(self):
#         self.con.close()
#         del self.cursor
#         del self.con
#
#     def ls(self, sql):
#         self.con()
#         self.cursor.execute(sql)
#         self.res = self.cursor.fetchall()
#         self.close()
#         return (self.res)
#
#     def up(self, sql):
#         print(sql)
#         try:
#             self.con()
#             self.cursor.execute(sql)
#             self.con.commit()
#             self.close()
#         except:
#             self.con.rollback()
#             self.close()
#
#
#
#
#         # 打开数据库连接
#         # vdb = pymysql.connect("127.0.0.1", "root", "Aa000000", "mylchweb")
#
#         # 使用 cursor() 方法创建一个游标对象 cursor
#         # cursor = db.cursor()
#
#         # 使用 execute()  方法执行 SQL 查询
#         # cursor.execute("SELECT * from USER ")
#
#         # 使用 fetchone() 方法获取单条数据.
#         # data = cursor.fetchone()
#         # print("Database version : %s " % data)
#
#         # results = cursor.fetchall()
#         # print(results);
#
#         # SQL 插入语句
#         # sql = """INSERT INTO EMPLOYEE(FIRST_NAME,
#         #          LAST_NAME, AGE, SEX, INCOME)
#         #          VALUES ('Mac', 'Mohan', 20, 'M', 2000)"""
#         # try:
#         #    # 执行sql语句
#         #    cursor.execute(sql)
#         #    # 提交到数据库执行
#         #    db.commit()
#         # except:
#         #    # 如果发生错误则回滚
#         #    db.rollback()
#
#
#
#
#
#         # 关闭数据库连接
#         # db.close()
