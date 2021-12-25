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
      path: '/search',
      name: 'search-page',
      component: require('@/components/SearchPage').default
    },
    {
      path: '/login',
      name: 'login-page',
      component: require('@/components/LoginPage').default
    },
    {
      path: '/register',
      name: 'register-page',
      component: require('@/components/RegisterPage').default
    },
    {
      path: '/bookList',
      name: 'bookList-page',
      component: require('@/components/BookListPage').default
    },
    {
      path: '/bookDetail',
      name: 'bookDetail-page',
      component: require('@/components/BookDetailPage').default
    },
    {
      path: '/shoppingCart',
      name: 'shoppingCart-page',
      component: require('@/components/ShoppingCartPage').default
    },
    {
      path: '/checkout',
      name: 'checkout-page',
      component: require('@/components/CheckoutPage').default
    },
    {
      path: '/creatCar',
      name: 'creatCar-page',
      component: require('@/components/CreatCarPage').default
    }
  ]
})
