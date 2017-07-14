### 插入排序算法

#### 思路

- 每次从数组中取出一个数字，与现有数字比较并插入适当的位置，如此重复，**每次均可保持现有的数字按照顺序排列** ，直至数字取完，即排序成功。

- 类似打牌

  1. 第一个条件：保持手上的牌的顺序是正确的。
  2. 每次抓到新的牌均按照顺序插入手上的牌中间。

- 其中有一点比较有意思的是，在每次比较操作发现新元素小于等于已排序的元素时，可以将已排序的元素移到下一位置，然后再将新元素插入该位置，接着再与前面的已排序的元素进行比较，这样做交换操作代价比较大。还有一个做法是，将新元素取出，从左到右依次与已排序的元素比较，如果已排序的元素大于新元素，那么将该元素移动到下一个位置，接着再与前面的已排序的元素比较，直到找到已排序的元素小于等于新元素的位置，这时再将新元素插入进去，就像下面这样：

  ![](Insertion_sort_animation.gif)

  ​

  再来个直观一点的图

  ![插入排序](Insertion-sort-example.gif)

  ​	

  #### 复杂度

  - 时间复杂度

    1. 最好的情况就是已经排好序的数组，这样一次都不用交换
    2. 最坏的情况就是完全逆序的数组，这样每个元素都要挪动，每次都要交换，次数为1+2+3+…+n-1=n(n-1)/2，时间复杂度为$O（n^2$）（即n的平方）
    3. 平均时间复杂度为$O（n^2$），是一种稳定的排序方法

  - 空间复杂度

    插入排序和冒泡排序一样是时间换空间的排序方法，没有使用多余的数据结构，不用分配额外的空间，所以空间复杂度为O（1）

  #### Python实现核心代码

  ```py
  # 插入排序
  def insert_sort(sort_lists):
      length = len(sort_lists)
      for j in range(1, length):
          key = sort_lists[j]
          i = j - 1
          # 向前查找插入位置
          while i >= 0 and sort_lists[i] > key:
              sort_lists[i + 1] = sort_lists[i]
              i = i - 1
          sort_lists[i + 1] = key
  ```

  ​

  ​

  ​

  ​
