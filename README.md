# Demo
## 语言：       
vue 3.x+element-plus  
python 3.x  
## 部署环境：    
### 后端：  
pip install flask  
pip install Flask-Cors  
pip install flask_sqlalchemy
pip install scipy
pip install scikit-learn
### 前端：   
npm install axios   
npm install echarts   
npm install element-plus 

## 运行方式：
进入后端目录 python app.py
进入前端目录 yarn run dev

## 使用说明：   
目前主要有四个页面:登陆页面，注册页面，信息展示页面和相似度对比分析页面；   
页面最上方的导航栏可以切换页面。   
登陆页面：可以登录数据库中已存在的用户信息，信息出错会有相应提示。
注册页面：注册属于自己的账号，用户名不可重复，会有提示。
信息展示页面：集群层面一个折线图，节点层面单指标两个折线图，多指标两个折线图，分别对应两个集群，下拉框可以选择不同集群不同节点以及不同指标。 
滚动鼠标滚轮，折线图可以进行放大和缩小，折线超出视野范围可以用鼠标拉一下。
信息展示页面还有一个刷新按钮，需要点击按钮的最上方，进行数据刷新。   
相似度对比分析页面：展示了相似度对比分析的结果以及相似度排名前五的五组数据的折线图，每个折线图中有两条折线，红色的折线表示0.csv的异常数据。   

## 接口说明
### clusterinfo
#### 接口功能
> 查询集群信息
#### URL
> http://localhost:5000/clusterinfo
#### HTTP请求方式
> GET
#### 请求参数
|参数|必选|类型|说明|
|----- |-------|-----|-----|
|cluster_name|ture|string|请求的集群名|
|feature    |true    |string   |请求的特征名|
#### 返回字段
|返回字段|字段类型|说明|
|-----|------|-----------------------------   |
|values  |json   |[时间戳，特征值]的二元数组列表   |
#### 接口示例
> 地址：[http://localhost:5000/clusterinfo？cluster_name='cc-cc408-hya'&feature='active_shards']
``` javascript
{
    {"timestamp": 1681291847,
    "value": 5114},
     {"timestamp": 1681291907,
    "value": 5114},
    ...
}
```
### clusterinfo1
#### 接口功能
> 查询集群节点信息
#### URL
> http://localhost:5000/clusterinfo1
#### HTTP请求方式
> GET
#### 请求参数
|参数|必选|类型|说明|
|-----  |-------|-----|-----                               |
|cluster_name    |ture    |string|请求的集群名                          |
|node_name    |true    |string   |请求的节点名|
|feature    |true    |string   |请求的特征名|
#### 返回字段
|返回字段|字段类型|说明                              |
|----   |------|-----------------------------   |
|values  |json   |[时间戳，特征值]的二元数组列表   |
#### 接口示例
> 地址：[http://localhost:5000/clusterinfo1？cluster_name='cc-cc408-hya'&node_name=data-node-04&feature='process_cpu_percent']
``` javascript
{
    {"timestamp": 1681291847,
    "value": 2},
     {"timestamp": 1681291907,
    "value": 1},
    ...
}
```
### clusterinfo2
#### 接口功能
> 查询集群节点磁盘信息
#### URL
> http://localhost:5000/clusterinfo2
#### HTTP请求方式
> GET
#### 请求参数
|参数|必选|类型|说明|
|-----  |-------|-----|-----                               |
|cluster_name    |ture    |string|请求的集群名                          |
|node_name    |true    |string   |请求的节点名|
|mount_name    |true    |string   |请求的磁盘名|
#### 返回字段
|返回字段|字段类型|说明 
|-----   |------|-----------------------------   |
|values  |json   |[时间戳，特征值]的二元数组列表   | 
#### 接口示例
> 地址：
[http://localhost:5000/clusterinfo1？cluster_name='cc-cc408-hya'&node_name='data-node-04'&mount_name='/srv/data01 (/dev/sdb)']
``` javascript
{
    {"timestamp": 1681291847,
    "value": 1830000000000},
     {"timestamp": 1681291907,
    "value": 1830000000000},
    ...
}
```



