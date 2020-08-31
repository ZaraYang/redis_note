import redis

pool =redis.ConnectionPool(host = '127.0.0.1',port = '6379')
r = redis.Redis(connection_pool=pool)

# ====================================
# redis 中的有序集合操作

# zadd 生成name对应的有序集合
# r.zadd('z',{"n1":1,"n2":2,"n3":5,"n4":3})

# zcard 返回name对应的有续集合的元素数量
# print(r.zcard('z'))

# zcount name对应的有序集合中分数在[min,max]之间的个数
# print(r.zcount('z',0,3))

# zincrby name对应的集合中value的分数增加
# r.zincrby('z',value= 'n2', amount= 3)

# zrange name对应的有序集合的索引查询
# print(r.zrange('z',1,3))

# zscore 返回某个对应的name集合的value的分数
# print(r.zscore('z','n1'))

# zrank 获取某个值在name对应的集合中的排行
# 不存在返回None
# print(r.zrank('z','n5'))

# zrem 按照value删除集合成员
# r.zrem('z','n1')

# zremrangebyrank 根据排行/分数范围删除
# r.zremrangebyrank('z',0,2)
# r.zremrangebyscore('z',0,5)

# zinterstore 取两个有序集合的交集，如遇到相同数值不同分数，则按照aggregate处理
# aggregate ： MIN MAX SUM
# dest 新集合的name
# keys 作交集的结合
# r.zinterstore('z3',('z1','z2'))

# zunionstore 并集同上

# 查看name对应的有序集合
# 0 为光标
print(r.zscan('z'))



