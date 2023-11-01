'''requests
1. requests是什么? 
 - requests是Python中的一个第三方库, 用于发送HTTP请求, 并处理HTTP响应.
 - 它具备以下功能: 
    1. 发送HTTP请求
    2. 处理HTTP响应
    3. 处理Cookie
    4. 自动跟随重定向
    5. 设置请求头和参数
    6. 处理代理
    7. 文件的上传和下载
    8. 客户端身份验证
    9. SSL验证
 - 它的适用场景广泛, 常用于Web爬虫, API访问, Web应用程序测试, 数据采集等.

2. requests.get()会返回哪些数据?
requests.get(url)向指定url发送HTTP GET请求后, 会返回一个包含HTTP响应的对象 - response.
它包含的返回数据如下: 
 - response.text: 提取响应中的文本内容, 通常是HTML/XML/JSON等(可用来提取网页内容).
 - response.content: 提取响应中的二进制内容, 通常用于下载文件或处理非文本数据.
 - response.url: 获取实际请求的url, 这在处理重定向时十分又用.
 - response.headers: 它是包含HTTP响应头信息的字典, 可以使用它获取响应的元数据.
 - response.status_code: HTTP响应的状态码, 200表示成功, 404表示未找到, 等等.
 - response.encoding: 获取响应的字符编码, 可通过它来正确解码响应的文本内容.
 - response.cookies: 获取响应中的cookies信息.
 - response.json(): 若响应内容是JSON格式的数据, 可使用此方法将其解析为Python对象.
 - response.raise_for_status(): 若响应状态码表示错误(如4XX), 此方法会引发异常, 方便错误处理.
'''