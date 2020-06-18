python接口自动化
接口测试理论
    接口概念：
        接口又称API（应用程序编程接口），是一些预先设计好的函数，目的是提供应用程序与开发人员基于某软件或硬件得以 访问一组例程的能力，而又无需访问源码，或理解内部工作机制的细节。

    接口类型：
        HTTP接口
        Web Service接口

    测试点：
        业务功能测试（场景测试）：
            正常场景
            异常场景
        边界测试：
            输入输出边界：
            业务规则边界：
        组合测试：
        异常测试：
        性能测试：
            响应时间
            吞吐量
            并发数
        安全测试：
            敏感信息加密
            SQL注入
    HTTP响应码：
        100  请求成功，请继续发送请求
        101  服务器正在切换协议

        200  请求成功
        201  已创建，请求成功，并且在服务器端已创建新的资源
        202  已接收，请求正确接收，但是还没有处理
        203  非权威信息，返回实体的头部信息不是源服务器中的有效集
        204  已接受，但是返回信息中没有内容，页面需要重置
        205  已接受，返回信息中没有内容，页面不需要重置

        300  请求的资源有多个选项
        301  永久重定向
        302  临时重定向，再次请求必须使用原url
        303  查看其他位置
        304  未改变，可以使用缓存
        305  必须使用代理

        400  客户端错误，url语法错误
        401  未授权的请求
        403  禁止，服务器拒绝服务
        404  请求的资源不存在，暂时不存在，没有详细信息
        405  请求方法被禁止
        406  请求中的mime类型与资源的mime类型不符
        407  必须通过代理服务器认证
        408  请求超时
        409  冲突
        410  已删除，请求的资源被删除了

        500  服务器内部错误
        501  未实现，服务器未实现请求中的方法
        502  网关错误
        503  服务器目前不能使用，多半是超载、停机维护
        504  网关超时
        505  请求协议错误
    
    OSI七层模型：
        应用层：文件传输，电子邮件，文件服务，虚拟终端
        表示层：数据格式化，代码转换，数据加密
        会话层：解除与建立与别的接点的联系（会话）
        传输层：提供端对端的接口（TCP/IP)
        网络层：为数据包选择路由
        链路层：传输有地址的帧及错误检测功能
        物理层：以二进制数据形式在物理媒体上传输数据


偏函数：
    functools.partial()会帮我们创建一个偏函数
    作用：把函数的某个参数固定住（也就是设置默认值），返回一个新的函数，调用这个新函数会更简单

匿名函数：
    f = lambda x:x*x
    关键字lambda表示匿名函数，冒号前的x表示函数参数，冒号后面是一个表达式，匿名函数只能有一个表达式

装饰器：
    作用：可以在不修改函数的情况下增加函数的功能

返回函数：


高阶函数：
    map(func, Iterable)：map将传入的函数依次作用于序列的每个元素，并把结果作为新的Iterator返回

    reduce(func, Iterable):reduce把一个函数作用于序列，reduce把函数结果继续和序列下一个元素做累积计算
        reduce(f, [1, 2, 3, 4])= f(f(f(1, 2), 3), 4)

    filter(func, Iterable)：filter将函数作用于序列的每个元素，filter将函数返回为true的序列值留下

    sorted()：该函数可以对list进行排序，也可以接受一个key来进行自定义排序，key指定的函数可以作用于list的每个元素

    用例设计：
        1、找到针对点，比如模块的功能、操作点、UI、安全、性能、兼容、交叉时间
        2、通过针对点，设计相应的用例，比如：
            通过功能，设计出：正常场景、异常场景、业务逻辑方面的用例
            通过操作点，设计出：输入输出边界、组合测试、业务规则边界方面的用例
            通过UI，设计出UI测试用例
            通过安全，设计出安全测试用例
            通过性能，设计出安全测试用例
            ...

python接口自动化测试框架
    组成：python+unittest+git+Jenkins+MySQL+Jira
    
Fiddler使用：

    1、抓HTTPS包设置
        进入Tools-->Options-->HTTPS
        勾选：Capture HTTPS CONNECTs（捕获HTTPS流量）
            Decrypt HTTPS traffic（解密HTTPS流量）
            Ionore server certificate（忽略服务器证书错误）
        点击：Actions按钮
        选择：Trust Root Certificate（信任跟证书）
        一直点确定

    2、抓Chrome浏览器包
        进入Chrome浏览器，在设置中修改代理，设置为127.0.0.1  8888
        在fiddler-->tools-->options-->https-->actions中点击Export Root Certificate to Desktop（导出根证书到桌面）
        将导出的证书添加到Chrome的“受信任的跟证书颁发机构”栏

    3、抓移动端的包
        在fiddler-->tools-->options-->Connections中点击Allow remote computers to connect（允许远程计算机连接），重启fiddler
        将手机接入和电脑同一个局域网，并设置手机代理为电脑IPV4地址
        在手机浏览器中输入：HTTP://IPv4地址，点击fiddler root certificate下载安装fiddler证书到手机，重启fiddler
        
    4、设置Filters（过滤）
        进入Filters界面
        勾选：Use Filters
        Hosts栏：（通过主机来设置过滤条件）
            选择Hosts栏中第二个下拉菜单中的Show only the following hosts(只显示下面的主机)
            在下面的输入框中输入将要显示的主机
        Client Process栏（通过客户端进程来设置过滤条件）
            Show only traffic from(仅显示来自后面选择框中的流量)
            Show only Internet Explorer traffic(仅显示来自IE浏览器的流量)
            Hide traffic from Service Host(隐藏来自服务主机的通信)
        Request Headers:(通过请求头来设置过滤条件)
        Breakpoints:(通过断点来设置过滤条件)
        Response Status Code:(通过响应码来设置过滤条件)
        Response Type and Size:(通过响应类型和响应大小来设置过滤条件)
        Response Headers:(通过响应头来设置过滤条件)

    5、设置断点
        为什么要设置断点：
            为了修改请求或者响应的数据，以达到调试接口的作用。
            通过浏览器发送请求，fiddler截获请求（断点），fiddler修改请求数据，fiddler发送修改后的请求，服务器收到请求并作出响应
            fiddler截获响应并修改响应，fiddler发送给浏览器。因为是浏览器发出的请求，可以最大限度的模拟真实用户情况
        
        步骤：
            1、在命令行中输入bpu，清除所有的断点
            2、在命令行中输入bpu xxx(在发起请求时中断所有包含xxx字符串的会话)
            3、通过客户端发送需要调试的请求
            4、在fiddler中选中请求，修改请求
            5、点击Break on Response(中断响应)
            6、点击Run to Completion(运行到完成)