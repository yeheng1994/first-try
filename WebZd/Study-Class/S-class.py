
class dog(object):
#   def __init__(self,a):
#       self.age = a
#      print("read 今年:", a)
    def zhuazi(self):
        print("使用嘴巴")
    def chigutou(self):
        self.zhuazi()
        print("吃骨头")
    def chishi(self):
        print("吃屎")


if __name__ == "__main__":
    read =dog() #实例化
    read.chigutou()
