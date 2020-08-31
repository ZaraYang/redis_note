import redis

pool =redis.ConnectionPool(host = '127.0.0.1',port = '6379')
r = redis.Redis(connection_pool=pool)

# ====================================
# redis 中的其他操作


# keys 返回redis中的键 name
# * 或 ?
print(r.keys(pattern='*'))

# exists 检查某个name是否存在
# print(r.exists('z'))

# expire 为某个name设置超时时间
# r.expire('z',100)

# rename 重命名某个name
# r.rename('z','z_set')

# delete 删除某个name
# r.delete('name')

# rendomkey 随即获取name
# print(r.randomkey())

# type 返回name类型
# print(r.type('z_set'))

# scan_iter 对name生成generator
# for i in r.scan_iter():
#     print(i)


