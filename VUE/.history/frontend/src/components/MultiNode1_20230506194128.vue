<template>
  <div class="MultiNode1">  
    <div class="title">cc-cc408-hya节点多指标</div>   
<select v-model="nodechoose" style="width:100px;height:30px;margin-top:5px;margin-bottom:5px;margin-left:10px"
            @change="ChooseNode($event)">
  <option value="">请选择所要展示节点</option>
  <option v-for="item in nodelist" v-bind:key="item.id" v-text="item.name"></option>
</select>
<select v-model="mountchoose" style="width:100px;height:30px;margin-top:5px;margin-bottom:5px;margin-left:10px"
          @change="ChooseMount($event)">
          <option value="">请选择所要展示磁盘</option>
  <option v-for="item in node_mount_list" v-bind:key="item.id" v-show="nodechoose==item.name">{{item.mount}}</option>
  </select> 
  <div class="echart" id="mychart4" :style="myChartStyle"></div>
  </div>
</template>
<script>
/* eslint-disable */ 
import axios from 'axios';
import * as echarts from "echarts";
//const d3=require('d3-dsv')
export default {
   data(){
    return{
       nodelist:[{name:"data-node-01(9.9.2.153)",id:1},{name:"data-node-02(9.9.2.154)",id:2},{name:"data-node-03(9.9.2.155)",id:3},{name:"data-node-04(9.9.2.156)",id:4},{name:"data-node-05(9.9.2.157)",id:5},
      {name:"data-node-06(9.9.2.153)",id:6},{name:"data-node-07(9.9.2.154)",id:7},{name:"data-node-08(9.9.2.155)",id:8},{name:"data-node-09(9.9.2.156)",id:9},{name:"data-node-10(9.9.2.157)",id:10},{name:"data-node-11(9.9.2.153)",id:11},
      {name:"data-node-12(9.9.2.154)",id:12},{name:"data-node-13(9.9.2.155)",id:13},{name:"data-node-14(9.9.2.156)",id:14},{name:"data-node-15(9.9.2.157)",id:15},{name:"data-node-16(9.9.2.153)",id:16},{name:"data-node-17(9.9.2.154)",id:17},
      {name:"data-node-18(9.9.2.155)",id:18},{name:"data-node-19(9.9.2.156)",id:19},{name:"data-node-20(9.9.2.157)",id:20},{name:"master-vm-01(9.9.3.150)",id:21},{name:"master-vm-02(9.9.3.151)",id:22},{name:"master-vm-03(9.9.3.152)",id:23}],
      node_mount_list:[{name:"data-node-01(9.9.2.153)",mount:"/srv/data01 (/dev/sdb)",id:1},{name:"data-node-01(9.9.2.153)",mount:"/srv/data02 (/dev/sdc)",id:2},{name:"data-node-01(9.9.2.153)",mount:"/srv/data03 (/dev/sdd)",id:3},
      {name:"data-node-02(9.9.2.154)",mount:"/srv/data01 (/dev/sdb)",id:4},{name:"data-node-02(9.9.2.154)",mount:"/srv/data02 (/dev/sdc)",id:5},{name:"data-node-02(9.9.2.154)",mount:"/srv/data03 (/dev/sdd)",id:6},
      {name:"data-node-03(9.9.2.155)",mount:"/srv/data01 (/dev/sdb)",id:7},{name:"data-node-03(9.9.2.155)",mount:"/srv/data02 (/dev/sdc)",id:8},{name:"data-node-03(9.9.2.155)",mount:"/srv/data03 (/dev/sdd)",id:9},
      {name:"data-node-04(9.9.2.156)",mount:"/srv/data01 (/dev/sdb)",id:10},{name:"data-node-04(9.9.2.156)",mount:"/srv/data02 (/dev/sdc)",id:11},{name:"data-node-04(9.9.2.156)",mount:"/srv/data03 (/dev/sdd)",id:12},
      {name:"data-node-05(9.9.2.157)",mount:"/srv/data01 (/dev/sdb)",id:13},{name:"data-node-05(9.9.2.157)",mount:"/srv/data02 (/dev/sdc)",id:14},{name:"data-node-05(9.9.2.157)",mount:"/srv/data03 (/dev/sdd)",id:15},
      {name:"data-node-06(9.9.2.153)",mount:"/srv/data04 (/dev/sde)",id:16},{name:"data-node-06(9.9.2.153)",mount:"/srv/data05 (/dev/sdf)",id:17},{name:"data-node-06(9.9.2.153)",mount:"/srv/data06 (/dev/sdg)",id:18},
      {name:"data-node-07(9.9.2.154)",mount:"/srv/data04 (/dev/sde)",id:19},{name:"data-node-07(9.9.2.154)",mount:"/srv/data05 (/dev/sdf)",id:20},{name:"data-node-07(9.9.2.154)",mount:"/srv/data06 (/dev/sdg)",id:21},
      {name:"data-node-08(9.9.2.155)",mount:"/srv/data04 (/dev/sde)",id:22},{name:"data-node-08(9.9.2.155)",mount:"/srv/data05 (/dev/sdf)",id:23},{name:"data-node-08(9.9.2.155)",mount:"/srv/data06 (/dev/sdg)",id:24},
      {name:"data-node-09(9.9.2.156)",mount:"/srv/data04 (/dev/sde)",id:25},{name:"data-node-09(9.9.2.156)",mount:"/srv/data05 (/dev/sdf)",id:26},{name:"data-node-09(9.9.2.156)",mount:"/srv/data06 (/dev/sdg)",id:27},
      {name:"data-node-10(9.9.2.157)",mount:"/srv/data04 (/dev/sde)",id:28},{name:"data-node-10(9.9.2.157)",mount:"/srv/data05 (/dev/sdf)",id:29},{name:"data-node-10(9.9.2.157)",mount:"/srv/data06 (/dev/sdg)",id:30},
      {name:"data-node-11(9.9.2.153)",mount:"/srv/data07 (/dev/sdh)",id:31},{name:"data-node-11(9.9.2.153)",mount:"/srv/data08 (/dev/sdi)",id:32},{name:"data-node-11(9.9.2.153)",mount:"/srv/data09 (/dev/sdj)",id:33},
      {name:"data-node-12(9.9.2.154)",mount:"/srv/data07 (/dev/sdh)",id:34},{name:"data-node-12(9.9.2.154)",mount:"/srv/data08 (/dev/sdi)",id:35},{name:"data-node-12(9.9.2.154)",mount:"/srv/data09 (/dev/sdj)",id:36},
      {name:"data-node-13(9.9.2.155)",mount:"/srv/data07 (/dev/sdh)",id:37},{name:"data-node-13(9.9.2.155)",mount:"/srv/data08 (/dev/sdi)",id:38},{name:"data-node-13(9.9.2.155)",mount:"/srv/data09 (/dev/sdj)",id:39},
      {name:"data-node-14(9.9.2.156)",mount:"/srv/data07 (/dev/sdh)",id:40},{name:"data-node-14(9.9.2.156)",mount:"/srv/data08 (/dev/sdi)",id:41},{name:"data-node-14(9.9.2.156)",mount:"/srv/data09 (/dev/sdj)",id:42},
      {name:"data-node-15(9.9.2.157)",mount:"/srv/data07 (/dev/sdh)",id:43},{name:"data-node-15(9.9.2.157)",mount:"/srv/data08 (/dev/sdi)",id:44},{name:"data-node-15(9.9.2.157)",mount:"/srv/data09 (/dev/sdj)",id:45},
      {name:"data-node-16(9.9.2.153)",mount:"/srv/data10 (/dev/sdk)",id:46},{name:"data-node-16(9.9.2.153)",mount:"/srv/data11 (/dev/sdl)",id:47},{name:"data-node-16(9.9.2.153)",mount:"/srv/data12 (/dev/sdm)",id:48},
      {name:"data-node-17(9.9.2.154)",mount:"/srv/data10 (/dev/sdk)",id:49},{name:"data-node-17(9.9.2.154)",mount:"/srv/data11 (/dev/sdl)",id:50},{name:"data-node-17(9.9.2.154)",mount:"/srv/data12 (/dev/sdm)",id:51},
     
      {name:"data-node-18(9.9.2.155)",mount:"/srv/data10 (/dev/sdk)",id:52},{name:"data-node-18(9.9.2.155)",mount:"/srv/data11 (/dev/sdl)",id:53},{name:"data-node-18(9.9.2.155)",mount:"/srv/data12 (/dev/sdm)",id:54},
       {name:"data-node-19(9.9.2.156)",mount:"/srv/data10 (/dev/sdk)",id:55},{name:"data-node-19(9.9.2.156)",mount:"/srv/data11 (/dev/sdl)",id:56},{name:"data-node-19(9.9.2.156)",mount:"/srv/data12 (/dev/sdm)",id:57},
      {name:"data-node-20(9.9.2.157)",mount:"/srv/data10 (/dev/sdk)",id:58},{name:"data-node-20(9.9.2.157)",mount:"/srv/data11 (/dev/sdl)",id:59},{name:"data-node-20(9.9.2.157)",mount:"/srv/data12 (/dev/sdm)",id:60},
      {name:"master-vm-01(9.9.3.150)",mount:"/ (/dev/mapper/vg_root-lv_root)",id:61},{name:"master-vm-02(9.9.3.151)",mount:"/ (/dev/mapper/vg_root-lv_root)",id:62},{name:"master-vm-03(9.9.3.152)",mount:"/ (/dev/mapper/vg_root-lv_root)",id:63}],
      myChart:{},
      xData:[],
      yData:[],
      myChartStyle:{float: "left", width: "100%", height: "85%"},
      flag3:0,
      nodename:"",
      nodechoose:"data-node-01(9.9.2.153)",
      mountchoose:"/srv/data01 (/dev/sdb)",
      initialized:0
    }
    },
    created()
    {
      this.Initdata()
    } ,
    mounted()
    {     
        this.initEcharts()
    },
    watch:{
    flag3:function()
    {
      this.flag3=0
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
        yAxis:{
          min:1
        },
        series:[
          {
            data:this.yData,
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
      this.myChart = echarts.init(document.getElementById("mychart4"));
      this.myChart.setOption(option);
      window.addEventListener("resize",()=>{
        this.myChart.resize();
      })
    },
    Initdata()
    {
     
      /*var filename="cc-cc408-hya/multi.csv"
      axios.get(filename)
        .then(res=>{
          var value=d3.csvParse(res.data)
          for(var i=0;i<value.length;i++)
          {
            if(value[i].node_name+"("+value[i].node_ip+")"==this.nodechoose&&value[i].mount==this.mountchoose)
           {
              this.xData.push(Number((value[i].timestamp-value[0].timestamp)/60))
              this.yData.push(Number(value[i].value/Math.pow(10,12)))
           } 
          }
          this.initialized=1
          })*/
        const path='http://localhost:5000/nodeinfo1';
        axios.get(path,{
             params:{
                cluster_name:'cc-cc553-interestPrice',
                node_name:this.nodechoose.split('(')[0],
                feature:this.nodefeature
            },
        }).then(res=>{
                this.value=res.data
                for(var i=0;i<this.value.length;i++){
                    this.xData2.push(Number(this.value[i].timestamp-this.value[0].timestamp)/60)
                    this.yData2.push(Number(this.value[i].value))
                }
                this.initialized=1
        })
          
        
    },
     ChooseNode(event)
    {
        this.nodechoose=event.target.value
        for(var i=0;i<this.node_mount_list.length;i++)
        {
          if(this.node_mount_list[i].name==this.nodechoose)
          {
            this.mountchoose=this.node_mount_list[i].mount;
            break
          }
        }
        if(this.mountchoose!="")
        {
          this.Changedata()
        }
    },
    ChooseMount(event)
    {
      this.mountchoose=event.target.value
      this.Changedata()
    },
    Changedata:function()
    {
      console.log(2222222)
      var filename="cc-cc408-hya/multi.csv"
      this.xData=[]
      this.yData=[]
      axios.get(filename)
        .then(res=>{
          var value=d3.csvParse(res.data)    
          for(var i=0;i<value.length;i++)
          {
            if(value[i].node_name+"("+value[i].node_ip+")"==this.nodechoose&&value[i].mount==this.mountchoose)
           {
              this.xData.push(Number((value[i].timestamp-value[0].timestamp)/60))
              this.yData.push(Number(value[i].value/Math.pow(10,12)))
           }   
          }
           this.flag3=1
        })
    }
    }     
    }
   

</script>
<style>
.MultiNode1{
    height:100%;
  
}
.title{
  margin-bottom:10px;
  align-content: center;
  color:rgb(99, 99, 117)
}
</style>