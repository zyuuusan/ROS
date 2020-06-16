# SLAM step by step



## :memo: Pre-requirement

### Read: 

[ROS tutorials(Beginner Level) 幫助了解ROS](http://wiki.ros.org/ROS/Tutorials)
[ROS by example v1 (Ch7, Ch8 navigation相關)](http://file.ncnynl.com/ros/ros_by_example_v1_indigo.pdf)
[ROS navigation tutorial (6.1)](http://wiki.ros.org/navigation)

對於navigation功能的建立，觀念來自這兩篇：
[ROS 教程之 navigation ： 用 move_base 控制自己的机器人(1)](https://blog.csdn.net/heyijia0327/article/details/41823809?fbclid=IwAR0zJhQoz3n-py2AkoesNt8NWYN2U0odei-Wds4Kt8qho56QV6ngI-ksFZs)
[ROS 教程之 navigation ： 用 move_base 控制自己的机器人(2)](https://blog.csdn.net/heyijia0327/article/details/41831529)

## Navigation Stack & communication layer
**after building your own workspace, for the navigation stack**

### You can start with these packages：

- [x] **move_base**
- [ ] **amcl**
> 我們沒特別安裝這個package，但是他好像是通訊層的功能，可以研究一下
- [x] **customized package(beginner_tutorial)**
> 用來存放自訂的訊息(輪速之類的)以及發布odometry到ROS系統上的節點


****
**Install package by git**
```
$ cd catkin_ws/src
$ git clone --branch branch_name github_link_on_ros.org
    // mind the version
$ cd ..
$ catkin_make
```

## beginner_tutorials

## 待解決的 Error

發生在map server，底盤的速度訊息經過odometry_publisher轉換發佈到ROS系統中，但map server(也就是gmapping package)運行時無法接到正確的odom input，無法用機器人真實的odometry訊息建圖。
**解決方法:** 
[Notes for Gmapping](https://hackmd.io/@shaohungchan/BkNvytnT-?type=view)
他有說到關於frame的問題，[ROS by example](http://file.ncnynl.com/ros/ros_by_example_v1_indigo.pdf)書中也有提到odometry message & odometry frame
在 odometry_publisher.py中使用了rospy模組下的publisher跟tf.broadcaster，可以檢查一下frame id

## 其他參考資料
> 遇到error就丟google找找看，kinetic的資料不少

[ROS系列文整理 (ROS Tutorials)](https://pojenlai.wordpress.com/2012/12/14/ros%E6%95%99%E5%AD%B8%E7%B3%BB%E5%88%97%E6%96%87%E6%95%B4%E7%90%86/)

[ROS探索总结（十四）—— move_base（路径规划）](https://www.guyuehome.com/270)

[ROS 教程之navigation: 用程序设定导航目标点](https://blog.csdn.net/heyijia0327/article/details/43565227)