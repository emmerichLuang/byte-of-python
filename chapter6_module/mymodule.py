

def my_main():

    print('我的第一个module')

    if __name__ == '__main__':
        print('执行自己')
    else:
        print('被调用, __name__:',__name__)


__version__ = '0.1'

