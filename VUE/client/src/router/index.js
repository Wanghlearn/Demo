import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'

const routes = [
 
  {
    path:"/",
    name:'login',
    component:()=>import('../views/LoGin.vue')
  },
  {
    path: '/home',
    name: 'home',
    component: HomeView
  },
  {
    path:"/similar",
    name:'similar',
    component:()=>import('../views/SimilarView.vue')
  },
  {
    path:'/register',
    name:"register",
    component:()=>import('../views/RegisterView.vue')
  }
  
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router
