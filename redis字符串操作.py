import redis

pool =redis.ConnectionPool(host = '127.0.0.1',port = '6379')
r = redis.Redis(connection_pool=pool)

# ====================================
# redis 中的字符串操作
# 01 set  (仅在value为字符串时使用)
# ex : 过期时间(s)
# px : 过期时间(ms)
# nx : name不存在时才有效 (True/False)
# xx : neme存在时才有效 (True/False)
# r.set(name="info",value="alex",ex=10)

# 02 setnx 等同于 set(nx=True)

# 03 setex 等同于 set(ms = ?)

# 04 mset 批量设置  输入为键值对或字典
# r.mset({"name":"alex","age":10})

# 05 get 取值操作
# print( r.get("name"))

# 06 mget 批量取值
# print(r.mget(["name","age"]))

# getset 设置新值并获取原来的值
# print(r.getset("name",'yang'))

# getrange 按照value字符串索引取值  []
# print(r.getrange('name',0,2))

# setrange 按照value字符串索引修改
# r.setrange('name',1,'uan')  # yang -> yuan 
# print(r.get('name'))

# strlen 返回value字符串长度
# print(r.strlen("name"))

# incr 自增操作  默认自加1
# r.incr('age',1)

# incrbyfloat() 自加浮点数

# decr 自减操作

# append(key,value) value 的值追加
# r.append('name',' he')


