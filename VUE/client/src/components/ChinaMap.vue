<template>
  <!-- 具备一个宽高的dom -->
  <div ref="main" style="height: 600px ;width: 100%;margin: 0;padding: 0;overflow: hidden" @dblclick="revertMap"></div>
</template>

<script>
// 导入echarts
import * as echarts from 'echarts';
// 中国地图
import chianJson from '@/map/china.json'
// 导入echarts主题
require('@/theme/dark')
// axios
import axios from 'axios'
// 各省份对应的矢量数据地址
import {getProvinceMapInfo} from '@/utils/map-utils'
export default {
  name: "china-map",
  data() {
    return {
      chart: ''
    }
  },
  mounted() {
    this.$nextTick(() => {
      this.initChart()
      window.addEventListener('resize', this.screenAdapter)
      this.screenAdapter()
    })

  },
  methods: {
    initChart() {
      // init第一个参数 ref定义的的，第二个参数主题
      this.chart = echarts.init(this.$refs.main, 'chalk')
      echarts.registerMap("chain", chianJson)
      this.chart.setOption({
        geo: {
          type: 'map', // 类型
          map: 'chain',
          top: '5%', // 距离顶部
          bottom: '5%', // 距离底部
          itemStyle: { // 地图区域的样式。
            areaColor: '#2E72BF', // 地图整体区域的颜色
            borderColor: '#333', //地图边界线的颜色
          },
        },
        // 自定义提示框的内容
        tooltip: {
          trigger: 'item',
          // 自定义提示框的内容
          formatter(params) {
            return (
              "<div>" +
              params.data.name +
              " <br> " +
              params.seriesName +
              "</div>"
            );
          }
        },
        // 散点图
        series: [
          {
            type: 'effectScatter',  //特效散点图
            rippleEffect: { // 涟漪效果
              scale: 5,
              brushType: 'stroke'
            },
            coordinateSystem: 'geo', // 使用坐标
            name: "一线城市",
            data: [
              {name: "北京", value: [116.46, 39.92]},
              {name: "上海", value: [121.48, 31.22]},
              {name: "广州", value: [113.23, 23.16]},
              {name: "深圳", value: [114.07, 22.62]},
            ]
          },
          {
            type: 'effectScatter',  //特效散点图
            rippleEffect: { // 涟漪效果
              scale: 5,
              brushType: 'stroke'
            },
            coordinateSystem: 'geo', // 使用坐标
            name: "二线城市",
            data: [
              {name: "南京", value: [118.78, 32.04]},
              {name: "杭州", value: [120.19, 30.26]},
              {name: "成都", value: [104.06, 30.67]},
              {name: "武汉", value: [114.31, 30.52]},
            ]
          },
          {
            type: 'effectScatter',  //特效散点图
            rippleEffect: { // 涟漪效果
              scale: 5,
              brushType: 'stroke'
            },
            coordinateSystem: 'geo', // 使用坐标
            name: "三线城市",
            data: [
              {name: "拉萨", value: [91.11, 29.97]},
              {name: "乌鲁木齐", value: [87.68, 43.77]},
              {name: "西宁", value: [101.74, 36.56]},
              {name: "兰州", value: [103.73, 36.03]},
            ]
          },
        ],
        
      })
      this.chart.on('click', async arg =>{
        const provinceInfo = getProvinceMapInfo(arg.name)
        console.log("provinceInfo",provinceInfo)
        // 如果存在key执行下面内容
        if(provinceInfo.key !== undefined){
          // 获取static下面的json数据
          const res = await axios.get("http://localhost:9528" + provinceInfo.path)
          echarts.registerMap(provinceInfo.key, res.data)
          const changeOption={
            geo:{
              map: provinceInfo.key
            }
          }
          this.chart.setOption(changeOption)
        }
      })

    },
    // 当浏览器的大小发生变化的时候，会调用此方法来完成适配
    screenAdapter() {
      // 获取自适应大小
      const titleFontSize = this.$refs.main.offsetWidth / 100 * 3.6
      console.log("titleFontSize", titleFontSize)
      // 自适应配置
      const adapterOption = {
        title: {
          textStyle: {
            fontSize: titleFontSize // 自适应字体大小
          }
        },
        legend: { // 图例组件
          itemWidth: titleFontSize / 2,
          itemHeight: titleFontSize / 2,
          itemGap: titleFontSize / 2,
          textStyle: {
            fontSize: titleFontSize / 2 // 自适应字体大小
          }
        },
      }
      this.chart.setOption(adapterOption)
      // 自适应
      this.chart.resize()
    },
    // 回退
    revertMap(){
      const revertOption={
        geo:{
          map: 'chain'
        }
      }
      this.chart.setOption(revertOption)
    },
  },
}
</script>

<style lang="scss" scoped>
.dashboard-container{
  height: 100%;
  width: 100%;
}
</style>

