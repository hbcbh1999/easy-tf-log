import easy_tf_log

for i in range(10):
    easy_tf_log.log('foo', i)
for j in range(10, 20):
    easy_tf_log.log('bar', j)

easy_tf_log.set_dir('logs2')

for k in range(20, 30):
    easy_tf_log.log('baz', k)
