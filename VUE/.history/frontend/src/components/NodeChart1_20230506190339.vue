<template>
    <div class="node">
      <div class="title">cc-cc408-hya节点单指标</div> 
    <select v-model="nodechoose" style="width:100px;height:30px;margin-top:5px;margin-bottom:5px;margin-left:10px"
      @change="ChooseNode($event)">
      <option value="">请选择所要展示结点</option>
      <option v-for="item in nodelist" v-bind:key="item.id" v-text="item.name"></option>
    </select>
    <select v-model="nodefeature" style="width:100px;height:30px;margin-top:5px;margin-bottom:5px;margin-left:10px"
      @change="Choose_Node_Feature($event)">
      <option value="">请选择所要展示结点特征</option>
      <option v-for="item in node_feature_list" v-bind:key="item.id" v-text="item.name"></option>
    </select>
     <div class="echart" id="mychart2" :style="myChartStyle"></div>
  </div>
</template>

<script>
import axios from 'axios';
import * as echarts from "echarts";
const d3=require('d3-dsv')
export default {
    data(){
    return{
      nodelist:[{name:"data-node-01(9.9.2.153)",id:1},{name:"data-node-02(9.9.2.154)",id:2},{name:"data-node-03(9.9.2.155)",id:3},{name:"data-node-04(9.9.2.156)",id:4},{name:"data-node-05(9.9.2.157)",id:5},
      {name:"data-node-06(9.9.2.153)",id:6},{name:"data-node-07(9.9.2.154)",id:7},{name:"data-node-08(9.9.2.155)",id:8},{name:"data-node-09(9.9.2.156)",id:9},{name:"data-node-10(9.9.2.157)",id:10},{name:"data-node-11(9.9.2.153)",id:11},
      {name:"data-node-12(9.9.2.154)",id:12},{name:"data-node-13(9.9.2.155)",id:13},{name:"data-node-14(9.9.2.156)",id:14},{name:"data-node-15(9.9.2.157)",id:15},{name:"data-node-16(9.9.2.153)",id:16},{name:"data-node-17(9.9.2.154)",id:17},
      {name:"data-node-18(9.9.2.155)",id:18},{name:"data-node-19(9.9.2.156)",id:19},{name:"data-node-20(9.9.2.157)",id:20},{name:"master-vm-01(9.9.3.150)",id:21},{name:"master-vm-02(9.9.3.151)",id:22},{name:"master-vm-03(9.9.3.152)",id:23}],
      node_feature_list:[{name:"os_load5",id:1},{name:"process_cpu_percent",id:2},{name:"index_time_seconds_total",id:3},{name:"search_query_time_seconds",id:4},
      {name:"transport_rx_size_bytes_total",id:5},{name:"transport_tx_size_bytes_total",id:6}],
      myChart2:{},
      xData2:[],
      yData2:[],
      flag2:0,
      nodechoose:"data-node-01(9.9.2.153)",
      nodefeature:"os_load5",
      initialized:0,
      myChartStyle:{float:"left", width: "100%", height: "85%"}
      }
    },
    created()
    {
      this.Initdata()
    },
    mounted(){
        this.initEcharts2();
    },
    watch:{
        flag2:function()
    {
      this.flag2=0
      this.initEcharts2();
    },
    initialized:function()
    {
      this.initEcharts2();
    }
    },
    methods:{
         initEcharts2()
    {
      const option={
        dataZoom: [{
        type: 'inside',
        show: true,
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
          data:this.xData2
          //type:"time"
        },
        yAxis:{},
        series:[
          {
            data:this.yData2,
            type:"line",
            showSymbol:false
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
      this.myChart2 = echarts.init(document.getElementById("mychart2"));
      this.myChart2.setOption(option);
      window.addEventListener("resize",()=>{
        this.myChart2.resize();
      })
    },
   
    ChooseNode(event)
    {
      this.nodechoose=event.target.value
      if(this.nodefeature!="")
      this.ChangeNodedata()
    },
    Choose_Node_Feature(event)
    {
      this.nodefeature=event.target.value
      //console.log(this.node_feature_name)
      if(this.nodechoose!="")
      this.ChangeNodedata()
    },
    Initdata()
    {
      /*var filename="cc-cc408-hya"+'/'+this.nodefeature+'.csv'
      axios.get(filename)
      .then(res=>{
        var value=d3.csvParse(res.data)
        for(var i=0;i<value.length;i++)
        {
          if(value[i].node_name+"("+value[i].node_ip+")"==this.nodechoose)
          {
            this.xData2.push(Number((value[i].timestamp-value[0].timestamp)/60))
            this.yData2.push(Number(value[i].value))
          }
          
        }
        this.initialized=1
      })*/
      const path='http://localhost:5000/nodeinfo1';
        axios.get(path,{
             params:{
                cluster_name:'cc-cc408-hya',
                node_name:this.nodechoose,
                feature:this.nodefeature
            },
        }).then(res=>{
                this.value=res.data
                for(var i=0;i<this.value.length;i++){
                    this.xData.push(Number(this.value[i].timestamp-this.value[0].timestamp)/60)
                    this.yData.push(Number(this.value[i].value))
                    this.initialized=1
                }
        })
    },
    ChangeNodedata:function()
    {
      var filename="cc-cc408-hya"+'/'+this.nodefeature+'.csv'
      this.xData2=[]
      this.yData2=[]
      axios.get(filename)
      .then(res=>{
        var value=d3.csvParse(res.data)
        for(var i=0;i<value.length;i++)
        {
          if(value[i].node_name+"("+value[i].node_ip+")"==this.nodechoose)
          {
            this.xData2.push(Number((value[i].timestamp-value[0].timestamp)/60))
            this.yData2.push(Number(value[i].value))
          }
          
        }
        this.flag2=1
      })
      console.log(this.xData2)
    }
    }
}
</script>
<style>
.node{
    height:100%
}
.title{
  margin-bottom:10px;
  align-content: center;
  color:rgb(99, 99, 117)
}
</style>