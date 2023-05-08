<template>
    <div class="cluster">
        <div class="title">集群层面</div> 
<select v-model="clusterchoose" style="width:100px;height:30px;margin-top:5px;margin-bottom:5px;margin-left:10px"
            @change="ChooseCluster($event)">
  <option value="">请选择所要展示集群</option>
  <option v-for="item in clusterlist" v-bind:key="item.id" v-text="item.name"></option>
</select>
       
<select v-model="featurechoose" style="width:100px;height:30px;margin-top:5px;margin-bottom:5px;margin-left:10px"
          @change="ChooseFeature($event)">
          <option value="">请选择所要展示特征</option>
  <option v-for="item in featurelist" v-text="item.name" v-bind:key="item.id"></option>
  </select>
       
  <div class="echart" id="mychart" :style="myChartStyle"></div>
  </div>
</template>
<script>
import axios from 'axios';
import * as echarts from "echarts";
//const d3=require('d3-dsv')
export default {
   data(){
    return{
      clusterlist:[{name:"cc-cc408-hya",id:1},{name:"cc-cc553",id:2}],
      featurelist:[{name:"status",id:1},{name:"active_shards",id:2},{name:"health_node",id:3}],
      myChart:{},
      xData:[],
      yData:[],
      myChartStyle:{float: "left", width: "100%", height: "85%"},
      flag:0,
      clusterchoose:"cc-cc408-hya",
      featurechoose:"status",
      initialized:0
    }
    },
    created()
    {
       this.Initdata()
    },
    mounted()
    {
       
        this.initEcharts()
    },
    watch:{
    flag:function()
    {
      this.flag=0
      this.initEcharts();
    },
    initialized:function()
    {
      this.initEcharts()
    }
    },
    methods:{
        initEcharts()
    {
      
      const option={
        dataZoom: [{
        type: 'inside',
        height: 20,
        left: '10%',
        right: '10%',
        bottom: '2%',
        start:90,
        end: 100,
        filterMode:"filter",
        xAxisIndex: [0],
        textStyle: {
          color: "#71A3CD",
          fontSize: 11
        }
        },
        {
          type:"inside",
          orient:"vertical"
        }],
        xAxis:{
          data:this.xData
          
          //type:"time"
        },
        yAxis:{},
        series:[
          {
            data:this.yData,
            type:"line",
            showSymbol:false,
            itemStyle: {
                borderRadius: 30,
              },

          }
        ],
         color: ["rgba(21,75,200,0.9)"],
        
        tooltip: {
          trigger: "axis",
          backgroundColor:'rgba(21,75,140,0.9)',
            extraCssText:'box-shadow: 0  6px 10px rgba(0,8,23,.65)',
          padding:[5,20],
          axisPointer: {
              type: "cross",
              lineStyle: {
                  width: '40',
                  color: {
                      type: 'linear',
                      x: 0,
                      y: 0,
                      x2: 0,
                      y2: 1,
                      colorStops: [{
                          offset: 0, color: 'rgba(91,179,252,0.5)' // 0% 处的颜色
                      }, {
                          offset: 1, color: 'rgba(91,179,252,1)' // 100% 处的颜色
                      }],
                      global: false // 缺省为 false
                  }
              }
          },

      },
      grid: {
        //坐标系设置
        containLabel: true,
        left: 0,
        right: 10,
        bottom: 0,
        top: 34,
        show:true,
        backgroundColor: new echarts.graphic.LinearGradient(0, 0, 0, 1, [
            {
                offset: 0,
                color: "rgba(1,48,87,0.2)" // 0% 处的颜色
            },
            {
                offset: 1,
                color: "rgba(1,48,87,0.8)" // 100% 处的颜色
            }
        ]), //背景渐变色
        borderColor: "rgba(0,0,0,0)"
    }
}
      
      this.myChart = echarts.init(document.getElementById("mychart"));
      this.myChart.setOption(option);
      window.addEventListener("resize",()=>{
        this.myChart.resize();
      })
    },
     ChooseCluster(event)
    {
        this.clusterchoose=event.target.value
        if(this.featurename!="")
        {
          this.Changedata()
        }
    },
    ChooseFeature(event)
    {
      this.featurechoose=event.target.value
      this.Changedata()
    },
    Initdata()
    {
      //console.log(1111)
      /*var filename=this.clusterchoose+'/'+this.featurechoose+'.csv'
      axios.get(filename)
        .then(res=>{
          var value=d3.csvParse(res.data)
          for(var i=0;i<value.length;i++)
          {
            this.xData.push(Number((value[i].timestamp-value[0].timestamp)/60))
            this.yData.push(Number(value[i].value))
            this.initialized=1
          }
        })*/
        const path='http://localhost:5000/test';
        axios.get(path)
            .then((res)=>{
                this.value=res.data
                for(var i=0;i<this.value.length;i++){
                    this.xData.push(Number(this.value[i].timestamp-this.value[0].timestamp)/60)
                    this.yData.push(Number(this.value[i].value))
                    this.initialized=1
                }
        })
        ///console.log(11111)
    },
    Changedata:function()
    {
      /*var filename=this.clusterchoose+'/'+this.featurechoose+'.csv'
      this.xData=[]
      this.yData=[]
      axios.get(filename)
        .then(res=>{
          var value=d3.csvParse(res.data)
              
          for(var i=0;i<value.length;i++)
          {
            this.xData.push(Number((value[i].timestamp-value[0].timestamp)/60))
            this.yData.push(Number(value[i].value))
            this.flag=1
          }
        })*/
        this.xData=[]
        this.yData=[]
        const path='http://localhost:5000/test';
        this.axios({
            methods:'get',
            params:{
                cluster_name:this.clusterchoose,
                
            }
        })
            .then(res=>{
                this.value=res.data
                for(var i=0;i<this.value.length;i++){
                    this.xData.push(Number(this.value[i].timestamp-this.value[0].timestamp)/60)
                    this.yData.push(Number(this.value[i].value))
                    this.flag=1
                }
            })
    }
    }     
    }
   

</script>
<style>
.cluster{
    height:100%;
}
.title{
  margin-bottom:10px;
  align-content: center;
  color:rgb(99, 99, 117)
}
select{
  background-color: rgba(1,1,1,0);
  color: rgb(57, 122, 179);
  border-color: rgba(21,75,140,0.5);
  border-radius: 50px;
}
</style>