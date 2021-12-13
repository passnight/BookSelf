import Vue from 'vue'
import Router from 'vue-router'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/main',
      name: 'main-page',
      component: require('@/components/LandingPage').default
    },
    {
      path: '*',
      redirect: '/main'
    },
    {
      path: '/test',
      name: 'test-page',
      component: require('@/components/Test').default
    }
  ]
})
