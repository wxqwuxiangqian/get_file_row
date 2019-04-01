import os


class file_rows(object):
    def __init__(self):
        self.row_count = 0

    def get_file_rows(self, file_path):
        count = 0
        # for count, line in enumerate(open(file_path, 'r', encoding='utf-8')):
        for count, line in enumerate(open(file_path, 'rb')):
            pass
        count += 1
        return count

    def get_file(self, path):
        global row_count
        list_dir = os.listdir(path)
        for file in list_dir:
            inner_path = path + '/' + file
            if os.path.isdir(inner_path):
                # print("%s is dir" % inner_path)
                self.get_file(inner_path)
            else:
                cf_rows = self.get_file_rows(inner_path)
                self.row_count += cf_rows
                # print("%s is file,rows:%s" % (inner_path, cf_rows))

    def get_rows(self, path):
        self.row_count = 0
        try:
            self.get_file(path)
        except Exception as e:
            print('统计出错:%s' % e.__str__())
        return self.row_count


if __name__ == '__main__':
    fr = file_rows()
    print(fr.get_rows('机械臂代码'))
