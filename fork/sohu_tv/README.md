问题1: 爬取tv.sohu.com的页面, 提取视频相关信息，不可用爬虫框架完成

需求:

* 做到最大可能的页面覆盖率
* 选择重要的信息进行存储
* 选择合适的数据存储方式，便于后续使用
* 可通过参数限制要抓取视频信息的数目
* 要用多线程方式完成抓取
* 反防抓取策略
* *分布式支持
* *崩溃后进度恢复

星号部分为加分项, 可只给出设计思路 ...




### 爬虫原理（采用广度优先算法）

维护三个队列：

* queue         存放待提取url
* tv_queue      存放需要提取视频信息的url
* count_queue   用于计数

1、 从一个入口(首页）地址开始，将地址加入队列，并存储到已抓取的url数据库集合中；

2、 取出存储在队列中的一条地址，解析该页面，从该页面中抽取出其包含的URL集合，过滤无效url,将得到的url与已经抓取的url集合进行对比，
    如果url集合中尚不存在，加入集合，并加入抓取队列，对于得到的链接如果符合视频页规则，则加入视频信息提取队列，进行视频信息提取；

3、 重复第二步，直到爬虫达到设置的抓取数量。



### 视频信息抓取规则

只抓取单独的视频页，不抓取分类和剧集等页面信息

对于视频页主要有两种类型：

官方发布的视频：http://tv.sohu.com/20140304/n395970803.shtml
日期 + 编号

用户上传的视频：http://my.tv.sohu.com/us/200430155/63582287.shtml
用户id + 编号


body部分不同频道结构不够统一，对于一般的视频信息采集，页面head部分的信息已经足够丰富（目前也只采集head部分)。
如果需要更详尽的信息大概主要可从下面这些片段提取信息。

    <div class="infoBox cfix  id=info">
    <div class="info info-con">
    <div class="area cfix" id="content">



### 数据采用MongoD存储

主要有两个集合：
url   存储已经收集到的地址：主要用于比对和去重，防止重复抓取

* url: 原始链接地址
* id: 原始链接地址的hash值，用于快速比对


tv    用于存储获取的视频信息

数据存储在MongoDB，为提高性能对于已经抓取的url可以考虑用redis存储和进行去重比对。广度优先可能会采集很多重复的url，
在数据库中已知url变多时，从中进行查询和对比可能会很慢，可以将类似首页和主要濒道的url等最容易出现重复的部分单独存储在一个列表中，
在去重对比时先对比这个小的列表，如果重复则不再需要查询数据库。


### 可通过参数限制要抓取视频信息的数目
参数可以通过 video_num 设置


### 反防抓取策略：
通过设置设置User-Agent等实现简单的反防抓取，如果需要可以添加代理设置，维护一个ip地址池，频繁更换ip欺骗服务器。
必要时调整抓取频率。


### 分布式支持

利用redis Lists 作为队列，使待处理url中心化存储，所有url采集爬虫将获得的url push 到lists，再从lists取出新的任务。
带提取视频的队列同理实现。

既用redis lists 替代Queue，实现多机器信息共享

将原先存储在MongoDB中的已处理url采用 redis sets 替代。


### 崩溃后的恢复？

所有已经遍历得到的地址队列同步存储在数据库中，在一个地址被成功处理后可以做一条标记，在崩溃后将未标记部分重新加入队列，从上次结束的位置继续搜索。
对于待提取视频的也做同样处理。

或者直接用redis 替代 Queue ？


### 爬虫测试

在4小时内抓取独立url地址超过10万，视频信息条目超过8万。数据参见data目录内。



### 视频总数估算

site:tv.sohu.com

Baidu: 83,100,000
Google：17,300,000

30,000,000 ?