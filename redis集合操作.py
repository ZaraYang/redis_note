import redis

pool =redis.ConnectionPool(host = '127.0.0.1',port = '6379')
r = redis.Redis(connection_pool=pool)

# ====================================
# redis 中的集合操作

# sadd 在name对应的集合添加元素
# r.sadd('score_set01',1,2,3,4,5,6,6,7,8)
# r.sadd('score_set02',6,7,8,9,10,11,12,13)

# scard 获取name对应的集合元素的数量
# print(r.scard("score_set01"))

# sdiff 在某个name对应的集合中却不在其他集合中的元素 叉集
# print(r.sdiff('score_set01','score_set02'))

# sinter 获取name对应集合的交集
# print(r.sinter("score_set01","score_set02"))

# sunion 获取name对应集合的并集
# print(r.sunion("score_set01","score_set02"))

# sismember 检查value是否是name对应的集合的成员
# print(r.sismember('score_set01',100))

# spop 随即删除并返回一个value
# print(r.spop('score_set01'))

# srandmember 从name对应的集合随即获取m个元素
# print(r.srandmember('score_set01',3))

# srem 删除结合中的某些value
# print(r.srem('score_set02',10))

# sscan_iter 返回生成器
# for i in r.sscan_iter('score_set02'):
#     print(i)

# smembers 查看对应name集合的成员
# print(r.smembers('score_set01') )
# print(r.smembers('score_set02') )


