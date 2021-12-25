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
        axios
        .get("/shopping_basket/get",{
          params:{
            user_id: user.userId
          }
        })
        .then((res) => {
			    console.log(res.data);
          if (res.data.code == 200) {
            store.state.car=res.data.data.check_out_list;
            store.state.checkoutListId=res.data.data.check_out_list_id;
            store.state.credit_card=res.data.data.credit_card;
            store.state.isCarEmpty=false
            next()
          } else {
            alert("支付方式未完善或购物车为空");
          }
        });
      }
  } else if ( to.path === '/creatCar') {
    if(store.state.user.userId === -1) {
      alert('请先登录')
      next('/login')
    } else {
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
  } else if ( to.path === '/bookList') {
    if(store.state.isSearch == false)
    {
      store.state.isBookList = true;
      axios
        .get("/book/search",{
          params:{
            isbn: '',
            title: '',
            author: ''
          }
        })
        .then((res) => {
			    console.log(res.data);
          if (res.data.code == 200) {
            store.state.bookList=res.data.data.bookList;
            next();
          } else {
            alert("出错了");
            next("/");
          }
        });
    } else {
      next();
    }
  } else {
    next()
  }
})