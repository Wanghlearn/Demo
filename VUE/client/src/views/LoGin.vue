<template>
<div id="background">
    <span class="tit">远程监控系统</span>
    <div class="container">
        <form method="post">
          <h1>Login</h1>
          <div class="form">
              <div class="item">
                <!-- v-model把输入的值传输给name变量 -->
                <label>用户名：</label><input type="text" v-model.trim="name"
                                          placeholder="请输入用户名">
                <br/>
              </div>
              <div class="item">
                <label>密码：</label><input type="password" v-model.trim="password"
                                         placeholder="请输入密码">
                <br/>
              </div>
          </div>
        </form>
        <!-- 点击按钮触发handlelogin方法 -->
        <button type="submit" @click.prevent="handlelogin">登录</button>
        <button type="submit" @click.prevent="register">注册</button>
        <span>{{error}}</span>
    </div>
</div>
</template>

<script>
import axios from "axios"
export default {
  data(){
    return{
      name:"",
      password:"",
      error:""
    };
  },
    //实现星星的运动
    mounted() {
  },
  methods:{
    handlelogin:function()
    {
       const path="http://localhost:5000/login"
      axios.get(path,{
        params:{
            name:this.name,
            password:this.password
        }
      }).then(res=>{
        if(res.data=="1")
        {
          this.$router.replace('/home');//成功匹配则跳转至主页面
        }
        else{
          this.error=res.data
        }
      })  
       },
       register:function()
       {
        this.$router.replace('/register');
       }
      
 
  }
};
</script>

<style scoped>
#background{
  width: 100%;
  min-width: 1200px;
  height: 100vh;
  /*径向渐变*/
  background: radial-gradient(ellipse at bottom, #383c3d 10%, #090a0f 100%);
  /*溢出隐藏*/
  overflow: hidden;
  position: relative;
  padding:0px;
  margin:0px;
}
.container{
  width: 480px;
  height: 300px;
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%,-50%);
  background: rgba(0, 0, 0, 0.5);
  text-align: center;
  border-radius: 20px;
  margin-top: 10px;
}
.container h1{
  margin-top: 5%;
  color: aliceblue;
  margin-left: 20px;
}
.container button{
  margin-top: 5%;
}
.item {
  color: white;
  margin-left: 15%;
  margin-top: 35px;
  font-size: 20px;
  text-align: left;
}
.item label{
  float:left;
  width: 5em;
  margin-right: 1em;
  text-align: right;
}
.form{
  margin-top: 5%;
}
/*登录输入框css*/
input{
  margin-left: -5px;
  padding: 4px;
  border: solid 2px #006bc2;
  border-radius: 10px;
  outline: 0;
  width: 200px;
  height: 23px;
}
/*登录按钮*/
button{
  position: relative;
  height: 33px;
  width: 100px;
  background: rgba(35, 19, 252, 0.5);
  border-radius: 10px;
  margin-top: 18px;
  color: white;
  margin-left: 40px;
  margin-right: 10px;
}
.tit{
    position:absolute;
    top:100px;
    left:40%;
    font-size: 50px;
    color: aliceblue;
}

</style>
