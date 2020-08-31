import redis

pool =redis.ConnectionPool(host = '127.0.0.1',port = '6379')
r = redis.Redis(connection_pool=pool)

# ====================================
# redis 中的hash操作

# hset 设置hash值
# r.hset("infos","name","alex")

# hmset 批量设置hash
# r.hmset("infos",{'age':99,'gender':'male'})

# hget 查找某hash的特定key对应的值
# print(r.hget("infos","name"))

# hgetall 查找某hash的所有key对应的值
# print(r.hgetall("infos"))

# hmget 取特定键中多个key对应的hash
# print(r.hmget("infos",['name','gender']))

# hlens 返回特定name对应的hash有几个键值对
# print(r.hlen('infos'))

# hkeys 返回特定name对应的hash的所有键
# print(r.hkeys('infos'))

# hvals 返回特定name对应的hash的所有值
# print(r.hvals("infos"))

# hexists 检查特定的name的hash中特定的键是否存在
# print(r.hexists('infos','name'))

# hdel 删除 name 或者键值对  返回0或1
# print(r.hdel("infos",'sex'))

# hincrby() 对hash中的value作自增操作
# r.hincrby("infos",'age',1)

# hincrbyfloat 对hash中的value作浮点数自增操作
# r.hincrbyfloat("infos",'age',0.1)

# hscan_iter  将hash做成生成器 generator
# match 对key进行匹配
# for i in r.hscan_iter('infos',match='a*'):
#     print(i)







