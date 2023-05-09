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


## 使用说明：   
目前主要有三个页面(这两天想加个注册功能):登陆页面，信息展示页面和相似度对比分析页面；   
页面最上方的导航栏可以切换页面。   
登陆页面：目前只有一个账号可以登录，用户名：wanghan，密码：123456   
信息展示页面：集群层面一个折线图，节点层面单指标两个折线图，多指标两个折线图，分别对应两个集群，下拉框可以选择不同集群不同节点以及不同指标。   
信息展示页面还有一个刷新按钮，需要点击按钮的最上方，进行数据刷新。   
相似度对比分析页面：展示了相似度对比分析的结果以及相似度排名前五的五组数据的折线图，每个折线图中有两条折线，红色的折线表示0.csv的异常数据。   



