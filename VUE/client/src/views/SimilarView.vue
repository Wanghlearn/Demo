<template>
    <div class="container" v-loading="loading">
       
        <div class="back">
    <Background></Background>
  </div>
        <div class="showpart">
            <div>相似度排名如下，相似度排名前五的数据展示如以下折线图</div>   
                <ul>
                    <li v-for="c in content.slice(0,10)" :key="c" v-text="c[1]">
                    </li>
                </ul>
                <ul>
                    <li v-for="c in content.slice(10,20)" :key="c" v-text="c[1]">
                    </li>
                </ul>
        </div>
        <div class="NG">
    <Navigator></Navigator>
  </div>
        <div class="First">
            <FirstChart></FirstChart>
        </div>
        <div class="Second">
            <SecondChart></SecondChart>
        </div>
        <div class="Third">
            <ThirdChart></ThirdChart>
        </div>
        <div class="Forth">
            <ForthChart></ForthChart>
            </div>
        <div class="Fifth">
            <FifthChart></FifthChart>
        </div>
    </div>

    
</template>

<script>
/* eslint-disable */
import axios from "axios";
import FirstChart from "@/components/FirstOne.vue";
import SecondChart from "@/components/SecondOne.vue";
import ThirdChart from "@/components/ThirdOne.vue";
import ForthChart from "@/components/ForthOne.vue";
import FifthChart from "@/components/FifthOne.vue";
import Background from "@/components/BackStarts.vue";
import Navigator from "@/components/NaviGator.vue";
export default {
    name: 'SimilarView',
    components:{
        FirstChart,
        SecondChart,
        ThirdChart,
        ForthChart,
        FifthChart,
        Background,
        Navigator
    },
    data() {
        return{
            content:[],
            loading:false
        }
    },
    mounted() {
        this.loading=true
        this.initialData()
        console.log(this.content)
    },
    methods: {
        initialData:function(){
            axios.get("http://localhost:5000/similar").then(res=>{
                this.content=res.data[0]
                this.loading=false
            })
            .catch(err=>{
                this.content = []
                console.log(err)
            })
        }
    },}
</script>
<style>
.container{
  position:relative;
  left:0px;
  top:0px;
  width:100vw;
  height:100vh;
}
.showpart{
    position:absolute;
    left:4%;
    top:90px;
    width:25%;
    height:40%;
    background-color:'rgba(21,75,140,0.9)';
    font-size:20px;
}
.back{
  position:absolute;
  z-index:-1;
  width:100%;
  height:900px;
  left:0px;
  top:0px;
  margin:0px;
  padding: 0px;
}
.First{
  position:absolute;
  left:36%;
  top:90px;
  width:25%;
  height:40%;
 
}
.Third{
  position:absolute;
  left:4%;
  top:470px;
  width:25%;
  height:40%
}
.Fifth{
  position:absolute;
  left:70%;
  height:40%;
  top:470px;
  width:25%;
}
.Forth{
  position:absolute;
  left:36%;
  height:40%;
  top:470px;
  width:25%;
}
.Second{
  position:absolute;
  left:70%;
  height:40%;
  top:90px;
  width:25%;
  
}
.NG
{
  position:absolute;
  top:10px;
  height:30px;
  width:100%;

}

ul{float:left;list-style:none;width:100px;}

</style>