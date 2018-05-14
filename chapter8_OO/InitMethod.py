#构造方法__init__


class MyDate:

    def __init__(self, yyyy, mm, dd):
        self.yyyy = yyyy;
        self.mm = mm;
        self.dd = dd;
        print('execute init~')

    def print_date(self):
        #print(self.yyyy,'-',self.mm, '-', self.dd)
        print('instance print:{}-{}-{}'.format(self.yyyy, self.mm, self.dd))


d = MyDate('2018', '01','11');
d.print_date()


