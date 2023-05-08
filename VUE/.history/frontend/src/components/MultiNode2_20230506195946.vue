<template>
   <div class="MultiNode1"> 
    <div class="title">cc-cc553-interestPrice节点多指标</div>   
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
  <div class="echart" id="mychart5" :style="myChartStyle"></div>
  </div>
</template>
<script>
import axios from 'axios';
import * as echarts from "echarts";
//const d3=require('d3-dsv')
export default {
   data(){
    return{
      nodelist:[{name:"data-node-01(9.9.6.147)",id:1},{name:"data-node-02(9.9.6.148)",id:2},{name:"data-node-03(9.9.6.149)",id:3},{name:"data-node-04(9.9.6.147)",id:4},{name:"data-node-05(9.9.6.148)",id:5},
      {name:"data-node-06(9.9.6.149)",id:6},{name:"data-node-07(9.9.6.147)",id:7},{name:"data-node-08(9.9.6.148)",id:8},{name:"data-node-09(9.9.6.149)",id:9},{name:"data-node-10(9.9.6.147)",id:10},{name:"data-node-11(9.9.6.148)",id:11},
      {name:"data-node-12(9.9.6.149)",id:12},{name:"master-vm-01(9.9.5.159)",id:21},{name:"master-vm-02(9.9.5.160)",id:22},{name:"master-vm-03(9.9.5.161)",id:23}],
      node_mount_list:[{name:"data-node-01(9.9.6.147)",mount:"/srv/data01 (/dev/sdb)",id:1},{name:"data-node-01(9.9.6.147)",mount:"/srv/data02 (/dev/sdc)",id:1},{name:"data-node-01(9.9.6.147)",mount:"/srv/data03 (/dev/sdd)",id:1},
      {name:"data-node-02(9.9.6.148)",mount:"/srv/data01 (/dev/sdb)",id:2},{name:"data-node-02(9.9.6.148)",mount:"/srv/data02 (/dev/sdc)",id:2},{name:"data-node-02(9.9.6.148)",mount:"/srv/data03 (/dev/sdd)",id:2},
      {name:"data-node-03(9.9.6.149)",mount:"/srv/data01 (/dev/sdb)",id:3},{name:"data-node-03(9.9.6.149)",mount:"/srv/data02 (/dev/sdc)",id:3},{name:"data-node-03(9.9.6.149)",mount:"/srv/data03 (/dev/sdd)",id:3},
      {name:"data-node-04(9.9.6.147)",mount:"/srv/data04 (/dev/sde)",id:4},{name:"data-node-04(9.9.6.147)",mount:"/srv/data05 (/dev/sdf)",id:4},{name:"data-node-04(9.9.6.147)",mount:"/srv/data06 (/dev/sdg)",id:4},
      {name:"data-node-05(9.9.6.148)",mount:"/srv/data04 (/dev/sde)",id:5},{name:"data-node-05(9.9.6.148)",mount:"/srv/data05 (/dev/sdf)",id:5},{name:"data-node-05(9.9.6.148)",mount:"/srv/data06 (/dev/sdg)",id:5},
      {name:"data-node-06(9.9.6.149)",mount:"/srv/data04 (/dev/sde)",id:6},{name:"data-node-06(9.9.6.149)",mount:"/srv/data05 (/dev/sdf)",id:6},{name:"data-node-06(9.9.6.149)",mount:"/srv/data06 (/dev/sdg)",id:6},
      {name:"data-node-07(9.9.6.147)",mount:"/srv/data07 (/dev/sdh)",id:7},{name:"data-node-07(9.9.6.147)",mount:"/srv/data08 (/dev/sdi)",id:7},{name:"data-node-07(9.9.6.147)",mount:"/srv/data09 (/dev/sdj)",id:7},
      {name:"data-node-08(9.9.6.148)",mount:"/srv/data07 (/dev/sdh)",id:8},{name:"data-node-08(9.9.6.148)",mount:"/srv/data08 (/dev/sdi)",id:8},{name:"data-node-08(9.9.6.148)",mount:"/srv/data09 (/dev/sdj)",id:8},
      {name:"data-node-09(9.9.6.149)",mount:"/srv/data07 (/dev/sdh)",id:9},{name:"data-node-09(9.9.6.149)",mount:"/srv/data08 (/dev/sdi)",id:9},{name:"data-node-09(9.9.6.149)",mount:"/srv/data09 (/dev/sdj)",id:9},
      {name:"data-node-10(9.9.6.147)",mount:"/srv/data10 (/dev/sdk)",id:10},{name:"data-node-10(9.9.6.147)",mount:"/srv/data11 (/dev/sdl)",id:10},{name:"data-node-10(9.9.6.147)",mount:"/srv/data12 (/dev/sdm)",id:10},
      {name:"data-node-11(9.9.6.148)",mount:"/srv/data10 (/dev/sdk)",id:11},{name:"data-node-11(9.9.6.148)",mount:"/srv/data11 (/dev/sdl)",id:11},{name:"data-node-11(9.9.6.148)",mount:"/srv/data12 (/dev/sdm)",id:11},
      {name:"data-node-12(9.9.6.149)",mount:"/srv/data10 (/dev/sdk)",id:12},{name:"data-node-12(9.9.6.149)",mount:"/srv/data11 (/dev/sdl)",id:12},{name:"data-node-12(9.9.6.149)",mount:"/srv/data12 (/dev/sdm)",id:12},
      {name:"master-vm-01(9.9.5.159)",mount:"/ (/dev/mapper/vg_root-lv_root)",id:21},
      {name:"master-vm-02(9.9.5.160)",mount:"/ (/dev/mapper/vg_root-lv_root)",id:22},
      {name:"master-vm-03(9.9.5.161)",mount:"/ (/dev/mapper/vg_root-lv_root)",id:23}],
      myChart:{},
      xData:[],
      yData:[],
      myChartStyle:{float: "left", width: "100%", height: "85%"},
      flag3:0,
      nodechoose:"data-node-01(9.9.6.147)",
      mountchoose:"/srv/data01 (/dev/sdb)",
      initialized:0
    }
    },
   created()
   {
    this.Initdata();
   },
    mounted()
    {
        this.initEcharts();
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
            showSymbol:false,
            "itemStyle": {
            "normal": {
                "barBorderRadius": 0
            },
          }
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
      this.myChart = echarts.init(document.getElementById("mychart5"));
      this.myChart.setOption(option);
      window.addEventListener("resize",()=>{
        this.myChart.resize();
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
    Initdata()
    {
      /*var filename="cc-cc553/multi.csv"
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
          })   */
        const path='http://localhost:5000/nodeinfo2';
        axios.get(path,{
             params:{
                cluster_name:'cc-cc553-interestPrice',
                node_name:this.nodechoose.split('(')[0],
                mount_name:this.mountchoose,
            },
        }).then(res=>{
                this.value=res.data
                for(var i=0;i<this.value.length;i++){
                    this.xData.push(Number(this.value[i].timestamp-this.value[0].timestamp)/60)
                    this.yData.push(Number(this.value[i].value/Math.pow(10,12)))
                }
                this.initialized=1
        })
          
        
        
    },
    Changedata:function()
    {
      /*var filename="cc-cc553/multi.csv"
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
        })*/
        this.xData2=[]
        this.yData2=[]
        const path='http://localhost:5000/nodeinfo2';
        axios.get(path,{
             params:{
                cluster_name:'cc-cc553-interestPrice',
                node_name:this.nodechoose.split('(')[0],
                mount_name:this.mountchoose,
            },
        }).then(res=>{
                this.value=res.data
                for(var i=0;i<this.value.length;i++){
                    this.xData.push(Number(this.value[i].timestamp-this.value[0].timestamp)/60)
                    this.yData.push(Number(this.value[i].value/Math.pow(10,12)))
                    this.flag3=1
                }
        })
    }
    }     
    }
   

</script>
<style>
.MultiNode2{
    height:100%;
}
.title{
  margin-bottom:10px;
  align-content: center;
  color:rgb(99, 99, 117)
}
</style>