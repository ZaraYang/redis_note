import redis
# python操纵redis缓存数据库

# redis实例
# 127.0.0.1为本机ip，6379为默认端口
# ===================================
# 基本连接方式
# r = redis.Redis(host='127.0.0.1',port=6379)
# ===================================
# 基于连接池连接  避免对同一个客户端的重复连接，提高效率
pool =redis.ConnectionPool(host = '127.0.0.1',port = '6379')
r = redis.Redis(connection_pool=pool)

# 设置和读取redis中的值
# r.set(name = 'age',value=99)
# print(r.get('age'))





