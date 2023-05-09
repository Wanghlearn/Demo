<template>

    <div class="echart" id="mychart9" :style="myChartStyle"></div>
</template>
<script>
import axios from "axios";
import * as echarts from "echarts";
export default {
    data()
    {
        return{
            xData:[],
            yData:[],
            compared_yData:[],
            flag:0,
            myChartStyle:{float: "left", width: "100%", height: "85%"},
            myChart:{}
        }
    },
    created()
    {
        this.initData()
    },
     mounted(){
        this.initEcharts()
    },
    watch:{
        flag:function()
        {
            this.flag=0
            this.initEcharts()
        }
    },
    methods:{
        initData()
        {
            axios.get("http://localhost:5000/similar").then(res=>{
                var value=res.data[1][3]
                var comparedvalue=res.data[1][5]
                for(var i=0;i<value.length;i++)
                {
                    this.xData.push(value[i][0])
                    this.yData.push(value[i][1])
                    this.compared_yData.push(comparedvalue[i][1])
                    this.flag=1
                }
                
            })
            .catch(err=>{
                console.log(err)
            })
        },
        initEcharts()
    {
      
      const option={
        dataZoom: [{
        type: 'inside',
        height: 20,
        left: '10%',
        right: '10%',
        bottom: '2%',
        start:0,
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
        legend:{
            data:["第18组数据","异常数据"],
            textStyle:{
                color:"rgba(255,255,255,0.5)"
            }
        },
        xAxis:{
          data:this.xData
          
          //type:"time"
        },
        yAxis:{},
        series:[
          {
            name:"第18组数据",
            data:this.yData,
            type:"line",
            showSymbol:false,
            itemStyle: {
                borderRadius: 30,
              },

          },
          {
            name:"异常数据",
            data:this.compared_yData,
            type:"line",
            showSymbol:false,
            color:"rgba(255,0,0,0.5)"
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
      
      this.myChart = echarts.init(document.getElementById("mychart9"));
      this.myChart.setOption(option);
      window.addEventListener("resize",()=>{
        this.myChart.resize();
      })
    }
    }
}
</script>
<style>

</style>