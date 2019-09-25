# 计算机网络实验 lab2

姓名：李沛尧

学号：1712901

## Q3

问题：
4. Locate the DNS query and response messages. Are then sent over UDP or TCP?
5. What is the destination port for the DNS query message? What is the source port of DNS response message?
6. To what IP address is the DNS query message sent? Use ipconfig to determine the IP address of your local DNS server. Are these two IP addresses the same?
7. Examine the DNS query message. What “Type” of DNS query is it? Does the query message contain any “answers”?
8. Examine the DNS response message. How many “answers” are provided? What do each of these answers contain?
9. Consider the subsequent TCP SYN packet sent by your host. Does the destination IP address of the SYN packet correspond to any of the IP addresses provided in the DNS response message?
10. This web page contains images. Before retrieving each image, does your host issue new DNS queries?

答案：

4. UDP
![Q3-4](./Q3-4.png)

5. 53
![Q3-51](./Q3-51.png)
![Q3-52](./Q3-52.png)

6. 202.113.16.41，是同一个IP

![Q4-61](./Q4-61.png)
![Q4-62](./Q4-62.png)

7. A和AAAA，包含了域名和查询类型

![Q4-71](./Q4-71.png)
![Q4-72](./Q4-72.png)

8. A返回了3个，AAAA返回了2个
![Q4-81](./Q4-81.png)
![Q4-82](./Q4-82.png)

9. 包含的有，向查询到的ipv6地址发起了TCP请求
![Q4-91](./Q4-91.png)

10. 没有发起DNS查询请求，查询目标域名的DNS请求只有一次
![Q4-10](./Q4-10.png)

## Q4

问题：
11. What is the destination port for the DNS query message? What is the source port of DNS response message?
12. To what IP address is the DNS query message sent? Is this the IP address of your default local DNS server?
13. Examine the DNS query message. What “Type” of DNS query is it? Does the query message contain any “answers”?
14. Examine the DNS response message. How many “answers” are provided? What do each of these answers contain?
15. Provide a screenshot.


答案：

11. 53，53

12. 202.113.16.41，是

13. A和AAAA，不包含

![Q5-13](./Q5-13.png)

14. 3个和四个

![Q5-141](./Q5-141.png)
![Q5-142](./Q5-142.png)

15. 

![Q5-151](./Q5-151.png)
![Q5-152](./Q5-152.png)
![Q5-153](./Q5-153.png)
![Q5-154](./Q5-154.png)

## Q6

问题：

16. To what IP address is the DNS query message sent? Is this the IP address of your default local DNS server?
17. Examine the DNS query message. What “Type” of DNS query is it? Does the query message contain any “answers”?
18. Examine the DNS response message. What MIT nameservers does the response message provide? Does this response message also provide the IP addresses of the MIT namesers?
19. Provide a screenshot.

答案：

16. 202.113.16.41，和本地DNS服务器一致

17. NS，不包含

![Q6-17](./Q6-17.png)

18. 返回信息如图，不包含MIT名称服务IP地址

![Q6-18](./Q6-18.png)

19. 

![Q6-191](./Q6-191.png)
![Q6-192](./Q6-192.png)

## Q7

问题：

20. To what IP address is the DNS query message sent? Is this the IP address of your default local DNS server? If not, what does the IP address correspond to?
21. Examine the DNS query message. What “Type” of DNS query is it? Does the query message contain any “answers”?
22. Examine the DNS response message. How many “answers” are provided? What does each of these answers contain?
23. Provide a screenshot.


答案：

20. 18.72.0.3 MIT的DNS服务器

21. A，不包含

![Q7-201](./Q7-201.png)
![Q7-202](./Q7-202.png)

22. 0个，两个

![Q7-211](./Q7-211.png)
![Q7-212](./Q7-212.png)

23. 

![Q7-221](./Q7-221.png)
![Q7-222](./Q7-222.png)
![Q7-223](./Q7-223.png)
![Q7-224](./Q7-224.png)
