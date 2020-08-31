import redis

pool =redis.ConnectionPool(host = '127.0.0.1',port = '6379')
r = redis.Redis(connection_pool=pool)

# ====================================
# redis 中的list操作

# lpush 创建新的链表 从右向左
# r.lpush('score',56,79,78,47,54) 

# rpush 创建新的链表 从左向右
# r.lpush('score',56,79,78,47,54) 

# lpushx  仅当name存在是则将值添加到链表左侧
# r.lpushx('score',555)
# r.rpushx 同样

# llen 返回name对应链表元素的数量
# print(r.llen('score'))

# linsert 在name对应的链表插入value
# where 向前向后 before after
# refvalue 标杆值
# r.linsert('score',where = 'after',refvalue=47,value= 48)

# lset 重新赋值
# index 链表index
# r.lset('score',0,5)

# lrem 删除链表中的值
# count = 0 删除对应的所有重复元素
# count = n  从左向右删除前n个对应元素
# count = -n  从右向左删除前n个对应元素
#r.lrem('score',count=0,value = 78)

# lpop 删除并返回最左边的元素
# r.lpop('score')
# rpop

# ltrim 删除对应name的不再范围内的元素
# r.ltrim('score',2,5)

# lindex 按照索引取链表中的value
# print(r.lindex('score',0))

# lrange 查看name对应的链表
# print(r.lrange('score',0,-1))

