"# NJU-Courses-Snatcher-Server" 
## 预处理

1.所有需要设置的变量都在文件开头，使用qq邮箱smtp服务发送验证码及通知，所以需要开通qq邮箱smtp
2.url获取方式是打开chrome F12控制台 NetWork，随便选择一节能选的课, 在 NetWork 里面 拦截请求url，然后根据需要从 element 里面提取想要的课程的课程ID，拼凑成新的Url //懒得写各个课程的url...请自取

## 运行
1.先运行cookies，这时候收件邮箱里会出现验证码图片【很有可能在回收箱里】，然后输入验证码，至此获取cookies

2.运行

> nohup python3 -u course.py > course.log 2>&1 &

程序就不断在后台执行了