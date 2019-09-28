# 计算机网络实验 lab4

姓名：李沛尧

学号：1712901

## Q1

问题：

1. What is the IP address and TCP port number used by the client computer (source) that is transferring the file to gaia.cs.umass.edu? To answer this question, it’s probably easiest to select an HTTP message and explore the details of the TCP packet used to carry this HTTP message, using the “details of the selected packet header window” (refer to Figure 2 in the “Getting Started with Wireshark” Lab if you’re uncertain about the Wireshark windows.

2. What is the IP address of gaia.cs.umass.edu? On what port number is it sending and receiving TCP segments for this connection?

答案：

1. 192.168.1.102，1161

![Q1-1](./Q1-1.png)

2. 128.119.245.12，80

![Q1-2](./Q1-2.png)

## Q2

问题：

4. What is the sequence number of the TCP SYN segment that is used to initiate the TCP connection between the client computer and gaia.cs.umass.edu? What is it in the segment that identifies the segment as a SYN segment?

5. What is the sequence number of the SYNACK segment sent by gaia.cs.umass.edu to the client computer in reply to the SYN? What is the value of the Acknowledgement field in the SYNACK segment? How did gaia.cs.umass.edu determine that value? What is it in the segment that identifies the segment as a SYNACK segment?

6. What is the sequence number of the TCP segment containing the HTTP POST command? Note that in order to find the POST command, you’ll need to dig into the packet content field at the bottom of the Wireshark window, looking for a segment with a “POST” within its DATA field.

7. Consider the TCP segment containing the HTTP POST as the first segment in the TCP connection. What are the sequence numbers of the first six segments in the TCP connection (including the segment containing the HTTP POST)? At what time was each segment sent? When was the ACK for each segment received? Given the difference between when each TCP segment was sent, and when its acknowledgement was received, what is the RTT value for each of the six segments? What is the EstimatedRTT value (see Section 3.5.3, page 242 in text) after the receipt of each ACK? Assume that the value of the EstimatedRTT is equal to the measured RTT for the first segment, and then is computed using the EstimatedRTT equation on page 242 for all subsequent segments. Note: Wireshark has a nice feature that allows you to plot the RTT for each of the TCP segments sent. Select a TCP segment in the “listing of captured packets” window that is being sent from the client to the gaia.cs.umass.edu server. Then select: Statistics->TCP Stream Graph> Round Trip Time Graph.

8. What is the length of each of the first six TCP segments?

9. What is the minimum amount of available buffer space advertised at the received for the entire trace? Does the lack of receiver buffer space ever throttle the sender?

10. Are there any retransmitted segments in the trace file? What did you check for (in the trace) in order to answer this question?

11. How much data does the receiver typically acknowledge in an ACK? Can you identify cases where the receiver is ACKing every other received segment (see Table 3.2 on page 250 in the text).

12. What is the throughput (bytes transferred per unit time) for the TCP connection? Explain how you calculated this value.

答案：

4. 0，Flag字段

![Q2-4](./Q2-4.png)

5. 0，1，根据Flag中标志位判断，TCP三次握手

![Q2-5](./Q2-5.png)

6. 1

![Q2-6](./Q2-6.png)

7. 
![Q2-71](./Q2-71.png)
![Q2-72](./Q2-72.png)
![Q2-73](./Q2-73.png)
![Q2-74](./Q2-74.png)
![Q2-75](./Q2-75.png)
![Q2-76](./Q2-76.png)
![Q2-77](./Q2-77.png)
![Q2-78](./Q2-78.png)
![Q2-79](./Q2-79.png)
![Q2-710](./Q2-710.png)
![Q2-711](./Q2-711.png)
![Q2-712](./Q2-712.png)
如图所示

![Q2-7](./Q2-7.png)

8. 565,1460,1460,1460,1460,1460

9. 5840，会

![Q2-9](./Q2-9.png)

10. 存在，对于Seq=164041有两次相同的序列号

11. 

12. 观察抓包数据，从带有HTTP POST的TCP链接开始，到带有HTTP RESPONSE结束的TCP链接结束，一共发送了120个长度未1460的数据包，共计用时5.18s，故平均传输速率为(120*1460)/5.18=33822.393822393824(bytes/s)
