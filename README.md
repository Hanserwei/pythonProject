# Python学习记录

## 为什么我选择学python

2024年我毕业了，考研失败了，进入了一家我本以为很好的公司，但是进去之后发现和我想象的公司并不相同，这个公司是个国企，所以国企的老毛病也都有，公司的办事效率极其的低下。公司目前使用的后台数据库还是SQLserver2008,导致现在很多使用window10以及windows11的电脑在使用这个数据库的时候遇到了很多的困难。至于后台前端系统，感觉开发的时候还是在windowsXP的时代，节目UI十分简陋不说，操作也是十分的反人类，而我由于本科生的关系。无缘于研发，所以即使我想把这个后台系统推翻重做也不可能，虽然研发现在也不打算更新这各系统了，他们选择和研究院合作开发了一套在Ubuntu上的后台系统，初体验之后发现还是依然的难用。可能是由于国企都喜欢一味地去追求高学历，忽视了科班的重要性，就我观点来说，学历是次要的，关键是能力，能否给公司带来足够的效益是最关键的。但是国企貌似不是这一套逻辑，他们认为的是研究生>本科生>大专生。我认为这种看法是相当错误的。询问和我同期进入研发的同事得知，他们现在要学的语言是Java,HTML 5,JavaScript,Vue等等，然而他们在大学以及研究所阶段从未接触到。现在是从零开始学。那么问题来了，研究生可以从零开始学，本科生，大专生为什么不可以？我无法改变公司，但我能改变自己，我要花最短时间掌握一门方便易用的语言，无疑就只有Python了。我希望在学了这门语言之后能加快我的工作效率，这也是我学习这门语言的初衷！

## IDE和环境配置

- Python有很多的IDE工具可选，我本人常用的是Jet Brain公司的[PyCharm](https://www.jetbrains.com/pycharm/download/?section=linux)以及由Microsoft公司推出的开源软件[VScode](https://code.visualstudio.com/Download)。
- 环境配置使用的是[Anaconda](https://www.anaconda.com/download/success)软件进行配置。
- 系统是[ArchLinux](https://archlinux.org/)操作系统。

## 目录解释

- 课程代码文件夹包含学习期间产出的所有代码以及笔记，每个文件的名字序号按学习的先后顺序进行排列
- 课程代码里面的练习代码主要包括了在学习途中的一些配套练习题，但是大部分都没把题目写上去。

## 致谢

- 感谢[哔哩哔哩视频平台](https://www.bilibili.com/)，这个平台是我学习代码用得最多的平台。
- 感谢[黑马程序员](https://space.bilibili.com/37974444?spm_id_from=333.337.0.0)的老师，我的前端，Java以及目前在学的Python都是观看的[哔哩哔哩视频平台](https://www.bilibili.com/ )上[黑马程序员](https://space.bilibili.com/37974444?spm_id_from=333.337.0.0)的免费视频。（个人经济实力有限无法报名[黑马程序员](https://space.bilibili.com/37974444?spm_id_from=333.337.0.0)的付费课程。）

## 相关网址

## 关键笔记

- 对于列表list的处理

  1. 列表索引查询,使用的是index方法

     ```python
     my_list = ['itcast','itheima','python']
     index = my_list.index("itheima")
     print(index)
     index2 = my_list.index("abc")
     print(index2)
     ```

  2. 列表元素的插入,使用的是insert方法

     ```python
     my_list = ['itcast','itheima','python']
     my_list.insert(1,'best')
     print(my_list)
     ```

  3. 列表追加元素,使用的是append方法

     ```python
     my_list = ['itcast','itheima','python']
     my_list.append('SWJTU')
     print(my_list)
     ```

  4. 列表追加一批元素(元素可以来自于其他数据容器),使用的是extend方法

     ```python
     my_list = ['itcast','itheima','python']
     my_list2 = [1,2,3]
     my_list.extend(my_list2)
     print(my_list)
     ```

  5. 列表中元素删除,使用的是pop方法或del *list*直接删除列表的元素,pop方法准确来说应该是取出元素

     ```python
     my_list = ['itcast','itheima','python']
     del my_list[2]
     print(my_list)
     
     # 值得注意的是.pop是将对应下标的元素取出,而不是直接删除,所以可以用量取到取出的值
     my_list2 = ['itcast','itheima','python']
     word = my_list2.pop(2)
     print(my_list2)
     print(word,type(word))
     ```

  6. 指定列表中的一个元素删除,使用remove方法

     ```python
     # 传入的元素后从前到后在列表里进行搜索,删除遇到的第一个匹配元素
     my_list = [1,2,3,4,5,1,2,3]
     my_list.remove(1)
     print(my_list)
     ```

  7. 清空列表,使用的是clear方法

     ```python
     my_list = [1,2,3,4,5,1,2,3]
     my_list.clear()
     print(my_list)
     ```

  8. 统计列表中某一个元素的数量,使用的是count方法

     ```python
     my_list = [1,1,1,2,3,4,1,2,3,4,5,6,'1','1']
     print(my_list.count(1))
     print(my_list.count('1'))
     ```

  9. 统计列表所有元素的数目,使用的是函数len

     ```python
     my_list = [1,1,1,2,3,4,1,2,3,4,5,6,'1','1']
     count = len(my_list)
     print(count)
     ```

     
