<template>
<div class="gross">
  <el-button class="flushbutton" type="button" @click="flush"><span>刷新</span></el-button>
  <div class="back">
    <Background></Background>
  </div>
  <div class="NG">
    <Navigator></Navigator>
  </div>
  <div class="Cluster">
    <ClusterChart ref="clusterchart"></ClusterChart>
  </div>
  <div class="NodeChart1">
    <NodeChart1 ref="nodechart1"></NodeChart1>
  </div>
  <div class="NodeChart2">
    <NodeChart2 ref="nodechart2"></NodeChart2>
  </div>
  <div class="Multinode1">
    <MultiNode1 ref="multinode1"></MultiNode1>
  </div>
  <div class="Multinode2">
    <MultiNode2 ref="multinode2"></MultiNode2>
  </div>
  <div class="ChinaMap">
    <ChMap></ChMap>
  </div>
</div>
</template>

<script>

import Background from "@/components/BackStarts.vue";
import ClusterChart from "@/components/ClusterChart.vue";
import NodeChart1 from "@/components/NodeChart1.vue";
import NodeChart2 from "@/components/NodeChart2.vue";
import MultiNode1 from "@/components/MultiNode1.vue";
import MultiNode2 from "@/components/MultiNode2.vue";
import Navigator from "@/components/NaviGator.vue";
import ChMap from "@/components/ChinaMap.vue";
//import Flushbutton from "@/components/FlushButton.vue";
export default {
  components:{
    Background,
    ClusterChart,
    NodeChart1,
    NodeChart2,
    MultiNode1,
    MultiNode2,
    Navigator,
    ChMap,
   // Flushbutton
  },
  methods:{
   flush()
   {
    console.log(1111)
    this.$refs.clusterchart.Changedata()
    this.$refs.nodechart1.ChangeNodedata()
    this.$refs.nodechart2.ChangeNodedata()
    this.$refs.multinode1.Changedata()
    this.$refs.multinode2.Changedata()
   }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
.gross{
  position:relative;
  left:0px;
  top:0px;
  width:100vw;
  height:100vh;
}
.back{
  position:absolute;
  z-index:-1;
  width:100%;
  height:900px;
  left:0px;
  top:0px;
}
.NodeChart1{
  position:absolute;
  left:4%;
  top:90px;
  width:25%;
  height:40%;
 
}
.Multinode1{
  position:absolute;
  left:4%;
  top:470px;
  width:25%;
  height:40%
}
.NodeChart2{
  position:absolute;
  left:70%;
  height:40%;
  top:470px;
  width:25%;
}
.Cluster{
  position:absolute;
  left:36%;
  height:40%;
  top:470px;
  width:25%;
}
.Multinode2{
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
.ChinaMap
{
  z-index:-1;
  position:absolute;
  left:25%;
  height:60%;
  top:40px;
  width:50%;
 
}
.flushbutton{
  position:absolute;
  background-color: rgb(57, 122, 179,0.5);
  color:aliceblue;
  height:50px;
  line-height:50px;
  padding:10px;
  width:50px;
  border-radius: 50px;
  left:90%;
  text-align:center;
  box-shadow: rgb(57, 122, 179);
}
</style>
