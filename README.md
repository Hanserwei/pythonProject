# Python学习记录

## 为什么我选择学python

2024年我毕业了，考研失败了，进入了一家我本以为很好的公司，但是进去之后发现和我想象的公司并不相同，这个公司是个国企，所以国企的老毛病也都有，公司的办事效率极其的低下。公司目前使用的后台数据库还是SQLserver2008,导致现在很多使用window10以及windows11的电脑在使用这个数据库的时候遇到了很多的困难。至于后台前端系统，感觉开发的时候还是在windowsXP的时代，界面UI十分简陋不说，操作也是十分的反人类，而我由于本科生的关系。无缘于研发，所以即使我想把这个后台系统推翻重做也不可能，虽然研发现在也不打算更新这各系统了，他们选择和研究院合作开发了一套在Ubuntu上的后台系统，初体验之后发现还是依然的难用。可能是由于国企都喜欢一味地去追求高学历，忽视了科班的重要性，就我观点来说，学历是次要的，关键是能力，能否给公司带来足够的效益是最关键的。但是国企貌似不是这一套逻辑，他们认为的是研究生>本科生>大专生。我认为这种看法是相当错误的。询问和我同期进入研发的同事得知，他们现在要学的语言是Java,HTML 5,JavaScript,Vue等等，然而他们在大学以及研究所阶段从未接触到。现在是从零开始学。那么问题来了，研究生可以从零开始学，本科生，大专生为什么不可以？我无法改变公司，但我能改变自己，我要花最短时间掌握一门方便易用的语言，无疑就只有Python了。我希望在学了这门语言之后能加快我的工作效率，这也是我学习这门语言的初衷！

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


- 数据容器的分类

  数据容器可以按照以下视角进行简单的分类:

  - 是否支持下标索引
    - 支持:列表,元组,字符串--序列类型
    - 不支持:集合,字典--非序列类型
  - 是否支持重复元素
    - 支持:列表,元组,字符串--序列类型
    - 不支持:集合,字典--非序列类型
  - 是否支持修改内部元素
    - 支持:列表,集合,字典
    - 不支持:元组,字符串

- 数据容器特点对比

|          | 列表                                | 元组                              | 字符串             | 集合                   | 字典                                     |
| -------- | ----------------------------------- | --------------------------------- | ------------------ | ---------------------- | ---------------------------------------- |
| 元素数量 | 支持多个                            | 支持多个                          | 支持多个           | 支持多个               | 支持多个                                 |
| 元素类型 | 任意                                | 任意                              | 仅字符             | 任意                   | key:除字典外任意类型<br />Value:任意类型 |
| 下标索引 | 支持                                | 支持                              | 支持               | 不支持                 | 不支持                                   |
| 重复元素 | 支持                                | 支持                              | 支持               | 不支持                 | 不支持                                   |
| 可修改性 | 支持                                | 不支持                            | 不支持             | 支持                   | 支持                                     |
| 数据有序 | 是                                  | 是                                | 是                 | 否                     | 否                                       |
| 使用场景 | 可修改,可重复记录一批数据的记录场景 | 不可修改,可重复的一批数据记录场景 | 一串字符的记录场景 | 不可重复的数据记录场景 | 以Key检索Value的数据记录场景             |

- 对于有序的数据容器的切片操作（针对列表，字符串，元组）

  语法:序列[起始下标:结束下标:步长]
  起始下标表示从何处开始,可以留空,留空表示从头开始
  结束下标表示到何处结束(不包含),可以留空,留空表示截取到尾
  步长表示取元素的间隔,步长为1表示一个一个取元素,步长为2表示每跳过一个元素取元素,步长为N,表示每此跳过N-1个元素取元素
  步长为负数的时候,表示反向取(注意,起始下标和结束下标也要反向标记),所有负号其实只是表示方向
  对序列切片的操作不会影响序列的本身,只是得到一各新的字符串

  ```python
  # 对list进行切片
  my_list = [0,1,2,3,4,5,6,7,8]
  result1 = my_list[1:4]
  print(result1) # [1,2,3,4]
  
  # 对tuple进行切片
  my_tuple = (0,1,2,3,4,5,6,7,8)
  result2 = my_tuple[:]
  print(result2) # 012345678
  
  # 对str进行切片
  my_str = "012345678"
  result3 = my_str[::2]
  print(result3) # 0246
  
  # 对序列进行切片,从头开始到最后结束,步长为-1
  result4 = my_str[::-1]
  print(result4) # 876543210
  
  # 对列表进行切片从3开始到1结束,步长为-1
  result5 = my_list[3:1:-1]
  print(result5) # 31
  
  # 对元组进行切片,从头开始,到尾结束,步长为-2
  result6 = my_tuple[::-2]
  print(result6) # 86420
  ```

  若没有指定切片结束的位置，那么就是到该容器的末尾且末尾可以取到。

- 对于字符串的进阶操作

  - 将字符串内的某个元素替换成指定的元素

    ```python
    # replace方法
    # 将字符串内的元素1替换成元素2,得到一个新字符串
    new_name = name.replace("h","H")
    print(new_name)
    ```

  - 将字符串切割为多个字符串并存入一个列表之中

    ```python
    # split方法
    # 按照指定的分隔字符串,将字符串分割为多个字符串,并存入列表对象中
    # 注意:字符串本身不变只是得到一个新的列表
    my_str = "hello my school"
    my_str_list = my_str.split(' ')
    print(my_str_list)
    ```

  - 去除掉字符串内的指定的字符

    ```python
    # strip方法
    # 去除字符串前后空格()使用.strip()
    # 去除指定的元素
    # 对于第二个情况,会去除每个元素比如.strip('123'),那么1 2 3都会去除
    # 注意:该方法还可以去除掉换行符\n
    my_str = "   hello world   "
    new_my_str = my_str.strip()
    print(new_my_str)
    my_str = "123hello world321"
    new_my_str_2 = my_str.strip('123')
    print(new_my_str_2)
    ```

- `.clear()`、`.count()` 和 `.remove()` 方法可以与以下 Python 数据容器一起使用：

  1. **列表 (List)**：
     - `.clear()`：从列表中移除所有元素。
     - `.count()`：返回列表中指定元素的出现次数。
     - `.remove()`：从列表中移除指定元素的第一次出现。

  2. **集合 (Set)**：
     - `.clear()`：从集合中移除所有元素。
     - `.count()`：集合不适用此方法。
     - `.remove()`：从集合中移除指定元素。如果未找到该元素，则引发 `KeyError`。

  3. **字典 (Dictionary)**：
     - `.clear()`：从字典中移除所有项。
     - `.count()`：字典不适用此方法。
     - `.remove()`：字典不适用此方法。

  以下是演示如何在列表和集合中使用这些方法的示例：

  ```python
  # 列表示例
  my_list = [1, 2, 3, 4, 1, 2, 3]
  my_list.remove(2)  # 移除第一个出现的2
  print(my_list)  # 输出: [1, 3, 4, 1, 2, 3]
  print(my_list.count(1))  # 输出: 2
  my_list.clear()  # 清空列表
  print(my_list)  # 输出: []
  
  # 集合示例
  my_set = {1, 2, 3, 4}
  my_set.remove(2)  # 从集合中移除2
  print(my_set)  # 输出: {1, 3, 4}
  my_set.clear()  # 清空集合
  print(my_set)  # 输出: set()
  ```

  注意，`.count()` 和 `.remove()` 方法不适用于字典。

- `.pop()` 方法在 Python 中主要用于列表和字典，它的作用如下：

  1. **列表 (List)**：
     - `.pop([index])`：移除并返回列表中指定位置（`index`）的元素。如果未提供 `index`，默认移除并返回最后一个元素。如果 `index` 超出范围，会引发 `IndexError`。

  2. **字典 (Dictionary)**：
     - `.pop(key)`：移除并返回字典中指定键（`key`）对应的值。如果该键不存在，会引发 `KeyError`。

  以下是使用 `.pop()` 方法的示例：

  ```python
  # 列表示例
  my_list = [1, 2, 3, 4]
  last_element = my_list.pop()  # 移除并返回最后一个元素
  print(last_element)  # 输出: 4
  print(my_list)  # 输出: [1, 2, 3]
  
  element_at_index = my_list.pop(1)  # 移除并返回索引为1的元素
  print(element_at_index)  # 输出: 2
  print(my_list)  # 输出: [1, 3]
  
  # 字典示例
  my_dict = {'a': 1, 'b': 2, 'c': 3}
  value = my_dict.pop('b')  # 移除并返回键为'b'的值
  print(value)  # 输出: 2
  print(my_dict)  # 输出: {'a': 1, 'c': 3}
  ```

  总结：`.pop()` 方法可以用来从列表或字典中移除特定元素，并返回该元素的值。

- 数据容器的通用操作

  - 遍历

    五类数据容器都支持for循环遍历操作,除字典和集合不支持while循环操作外(无法进行下标索引),其余数据容器也支持while循环操作

  - len(容器):统计容器的元素个数

    ```python
    my_list = [1,2,3]
    my_tuple = (1,2,3,4,5)
    my_str = 'itheima'
    my_set = {1,2,3,4,5}
    my_dict = {'key1':1,'key2':2,'key3':3,'key4':4,'key5':5}
    print(len(my_list)) # 结果3
    print(len(my_tuple)) # 结果5
    print(len(my_str)) # 结果7
    print(len(my_set)) #结果5
    print(len(my_dict)) #结果5
    ```

  - max(容器):统计容器的最大元素

    ```python
    my_list = [1,2,3]
    my_tuple = (1,2,3,4,5)
    my_str = 'itheima'
    my_set = {1,2,3,4,5}
    my_dict = {'key1':1,'key2':2,'key3':3,'key4':4,'key5':5}
    print(max(my_list)) # 结果3
    print(max(my_tuple)) # 结果5
    print(max(my_str)) # 结果t
    print(len(my_set)) #结果5
    print(len(my_dict)) #结果key5
    ```

  - min(元素):统计容器的最小元素

    ```python
    my_list = [1,2,3]
    my_tuple = (1,2,3,4,5)
    my_str = 'itheima'
    my_set = {1,2,3,4,5}
    my_dict = {'key1':1,'key2':2,'key3':3,'key4':4,'key5':5}
    print(min(my_list)) # 结果3
    print(min(my_tuple)) # 结果5
    print(min(my_str)) # 结果7
    print(len(my_set)) #结果1
    print(len(my_dict)) #结果key1
    ```

  - 数据容器的类型转换

    - 容器转列表

      ```python
      # 数据容器的类型转换
      my_list = [1,2,3]
      my_tuple = (1,2,3,4,5)
      my_str = 'atheism'
      my_set = {1,2,3,4,5}
      my_dict = {'key1':1,'key2':2,'key3':3,'key4':4,'key5':5}
      # 类型转换:容器转列表
      print(f"列表转列表的结果是{list(my_list)}")
      print(f"元组转列表的结果是{list(my_tuple)}")
      print(f"字符串转列表的结果是{list(my_str)}")
      print(f"集合转列表的结果是{list(my_set)}")
      print(f"字典转列表的结果是{list(my_dict)}")
      ```

    - 容器转元组

      ```python
      # 数据容器的类型转换
      my_list = [1,2,3]
      my_tuple = (1,2,3,4,5)
      my_str = 'atheism'
      my_set = {1,2,3,4,5}
      my_dict = {'key1':1,'key2':2,'key3':3,'key4':4,'key5':5}
      # 类型转换:容器转元组
      print(f"列表转元组的结果是{tuple(my_list)}")
      print(f"元组转元组的结果是{tuple(my_tuple)}")
      print(f"字符串转元组的结果是{tuple(my_str)}")
      print(f"集合转元组的结果是{tuple(my_set)}")
      print(f"字典转元组的结果是{tuple(my_dict)}")
      ```

    - 容器转字符串

      ```python
      # 数据容器的类型转换
      my_list = [1,2,3]
      my_tuple = (1,2,3,4,5)
      my_str = 'atheism'
      my_set = {1,2,3,4,5}
      my_dict = {'key1':1,'key2':2,'key3':3,'key4':4,'key5':5}
      # 类型转换:容器转字符串
      print(f"列表转字符串的结果是{str(my_list)}")
      print(f"元组转字符串的结果是{str(my_tuple)}")
      print(f"字符串转字符串的结果是{str(my_str)}")
      print(f"集合转字符串的结果是{str(my_set)}")
      print(f"字典转字符串的结果是{str(my_dict)}")
      ```

    - 容器转集合

      ```python
      # 数据容器的类型转换
      my_list = [1,2,3]
      my_tuple = (1,2,3,4,5)
      my_str = 'atheism'
      my_set = {1,2,3,4,5}
      my_dict = {'key1':1,'key2':2,'key3':3,'key4':4,'key5':5}
      # 类型转换:容器转集合
      print(f"列表转集合的结果是{set(my_list)}")
      print(f"元组转集合的结果是{set(my_tuple)}")
      print(f"字符串转集合的结果是{set(my_str)}")
      print(f"集合转集合的结果是{set(my_set)}")
      print(f"字典转集合的结果是{set(my_dict)}")
      ```

  - 容器的通用排序功能

    使用sort(容器，[reverse = True])进行排序，若不加reverse则默认为正序，若加了reverse=True则为倒序列排序。

    ```python
    my_list = [3,4,1,6,8,0]
    my_tuple = (0,6,3,8,9)
    my_str = 'atheism'
    my_set = {5,7,2,1,4,6}
    my_dict = {'key1':6,'key2':4,'key3':2,'key4':1,'key5':0}
    print(f"列表对象排序的结果是{sorted(my_list)}")
    print(f"元组对象排序的结果是{sorted(my_tuple)}")
    print(f"字符串对象排序的结果是{sorted(my_str)}")
    print(f"集合对象排序的结果是{sorted(my_set)}")
    print(f"字典对象排序的结果是{sorted(my_dict)}")
    # 排序的结果都会变成列表对象,即对容器进行排序并存入一个列表,字典排序也同样会丢失Value
    print(f"列表对象排序的结果是{sorted(my_list,reverse=True)}")
    print(f"元组对象排序的结果是{sorted(my_tuple,reverse=True)}")
    print(f"字符串对象排序的结果是{sorted(my_str,reverse=True)}")
    print(f"集合对象排序的结果是{sorted(my_set,reverse=True)}")
    print(f"字典对象排序的结果是{sorted(my_dict,reverse=True)}")
    ```
    

