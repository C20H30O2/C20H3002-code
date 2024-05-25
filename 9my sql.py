from pymysql import connect
conn=connect(  # 建立与mysql数据库的连接
    host="localhost",# 主机名
    port=3306,# 默认3306
    user="root",#账户
    password="123456",#密码
    autocommit=True# 修改为自动确认后就不需要下面在更改数据中提到的的手动确认了
)
print(conn.get_server_info())# 成功打印说明连接成功




cursor=conn.cursor() # 获取到游标对象
conn.select_db("world")# 选择数据库


# cursor.execute("create table test_mysql(id int)")# 执行sql语句   括号里的sql语句结束可以不用写分号
# cursor.execute("select * from country")
# results=cursor.fetchall()# 这个成员方法可以获取到上面的查询结果
# for x in results:# 结果为一个个元组，说明results是一个包含小元组的大元组
#     print(x)


# 更改数据
cursor.execute("insert into student values(1,'jack',18)")
conn.commit() # 没有设置autocommit=True时需要手动通过commit进行确认，才能写入和更改数据
conn.close()# 使用完后关闭连接
