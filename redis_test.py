import redis

r = redis.StrictRedis(host='localhost', port=6379, db=0)
r.set('foo', 'bar')

pool = redis.ConnectionPool(host='localhost', port=6379, db=0)
r = redis.Redis(connection_pool=pool)

r = redis.Redis(unix_socket_path='/tmp/redis.sock')

pool = redis.ConnectionPool(connection_class=YourConnectionClass,your_arg='...', ...)
print r.get('foo')
