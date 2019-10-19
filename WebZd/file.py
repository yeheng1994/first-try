from pathlib import Path
#读取文件
f = open("H:\\Codeall\\WebZd\\report\\yeheng.txt","r")
fp = f.read()
print(fp)
f.close()
#写入文件
f1 = open("H:\\Codeall\\WebZd\\report\\yeheng.txt","a")  #w 覆盖写入  a 追加写入
f1.write("\n 学校: 重庆大学")
f1.close()

#通过管道打开
with open("H:\\Codeall\\WebZd\\report\\yeheng.txt","r") as fp:
    a = fp.read()
    print(a)


def unify_ext_with_pathlib(path):
    for fpath in Path(path).glob('*.txt'):
        fpath.rename(fpath.with_suffix('.csv'))
'''和旧代码相比，新函数只需要两行代码就完成了工作。而这两行代码主要做了这么几件事：
•首先使用 Path(path) 将字符串路径转换为 Path 对象
•调用 .glob('*.txt') 对路径下所有内容进行模式匹配并以生成器方式返回，结果仍然是 Path 对象，所以我们可以接着做后面的操作
•使用 .with_suffix('.csv') 直接获取使用新后缀名的文件全路径
•调用 .rename(target) 完成重命名'''


def count_nine(fname):
    """计算文件里包含多少个数字 '9'

    """

    count = 0

    with open(fname) as file:
        for line in file:
            count += line.count('9')

    return count


def count_nine_v2(fname):
    """计算文件里包含多少个数字 '9'，每次读取 8kb

    """

    count = 0

    block_size = 1024 * 8

    with open(fname) as fp:

        while True:

            chunk = fp.read(block_size)

            # 当文件没有更多内容时，read 调用将会返回空字符串 ''

            if not chunk:
                break

            count += chunk.count('9')

    return count

