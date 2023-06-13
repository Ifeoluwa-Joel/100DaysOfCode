import time

epoch = time.gmtime(0)
print(epoch)
print(time.asctime(epoch))

clock = time.time()
print(clock)

my_time = time.localtime()
print(my_time)
print(time.asctime(my_time))
