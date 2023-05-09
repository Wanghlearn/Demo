<template>
<div id="background">
    <!-- 星空背景-->
    <div class="stars">
        <div class="star" v-for="(item,index) in starsCount" :key="index" ref="star"></div>
    </div>
</div>
</template>

<script>
export default {
  data(){
    return{
      //定义星星的数量与间距
      starsCount:1000,
      distance:800,
    };
  },
    //实现星星的运动
    mounted() {
    //绑定组件
    let starArr=this.$refs.star
    //调用数组中每个元素
    starArr.forEach(item=>{
      var distance = this.distance+(Math.random()*300)
      //设置旋转的基点
      item.style.transformOrigin=`0 0 ${distance}px`
      item.style.transform=`translate3d(0,0,-${distance}px)
      rotateY(${(Math.random()*360)}deg) rotateX(${(Math.random()*(-80))}deg)`
    })
  }
}
</script>

<style scoped>
#background{
  width: 100%;
  min-width: 1200px;
  height: 100%;
  /*径向渐变*/
  background: radial-gradient(ellipse at bottom, #01011f 30%, #060233 100%);
  /*溢出隐藏*/
  overflow: hidden;
  position: relative;
}
/*星空部分css*/
.stars{
    transform: perspective(800px);
    transform-style: preserve-3d;
    position: absolute;
    left: 50%;
    /*动画属性，控制速度；infinite 动画播放无限次；linear从头到尾速度相同*/
    animation: rotate 70s infinite linear;
    /*调整位置 让星星处于屏幕中间*/
    bottom: -300px;
  }
/*定义star属性*/
.star{
  width: 2px;
  height: 2px;
  background: #ffffff;
  position: absolute;
  top: 0;
  left: 0;
}
/*无限旋转 rorate为动画名称*/
@keyframes rotate {
  /*0%为动画的开始时间*/
  0%{
    /*css样式,perspective为视距，rotate*为移动距离*/
    transform: perspective(600px) rotateZ(20deg) rotateX(-40deg) rotateY(0);
  }
  /*100%为动画的结束时间*/
  100%{
    transform: perspective(600px) rotateZ(20deg) rotateX(-40deg) rotateY(-360deg);
  }
}
</style>
