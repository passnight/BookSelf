import Vue from 'vue'
import axios from 'axios'
import store from './store'

import App from './App'
import router from './router'

if (!process.env.IS_WEB) Vue.use(require('vue-electron'))
Vue.http = Vue.prototype.$http = axios
Vue.config.productionTip = false

axios.defaults.baseURL = 'http://localhost:8848'

/* eslint-disable no-new */
new Vue({
  components: { App },
  router,
  store,
  template: '<App/>'
}).$mount('#app')

router.beforeEach((to, from, next) => {
  if( to.path === '/shoppingCart') {
      var user = store.getters.user
      if (user.userId === -1) {
        alert('请先登录')
        next('/login')
      } else {
        alert(user.userId)
        next()
      }
  } else if ( to.path === '/bookDetail') {
    var detailId= store.getters.bookDetail
    if (detailId === -1){
      alert(发生错误)
      next('/bookList')
    } else {
      next()
    }
  } else {
    next()
  }
})