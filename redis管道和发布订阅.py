import redis

pool =redis.ConnectionPool(host = '127.0.0.1',port = '6379')
r = redis.Redis(connection_pool=pool)

# ====================================
# redis 中的管道
# 事务：要么同时成功，或者同时失败
# 不允许执行一半

# pipe = r.pipeline(transaction=True)
# pipe.set('name','alex')
# pipe.set('role','sb')
# pipe.execute()

# ===================================
# redis发布订阅

# 订阅者
# pub = r.pubsub()
# pub.subscribe("fm104.5")
# pub.parse_response()

# while 1:
#     msg = pub.parse_response()
#     print(msg)

# 发布者

# r.publish('fm104.5','hello world')
# 信息将被复制，订阅者人手一份


