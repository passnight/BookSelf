<template>
  <div id="app">
    <my-head></my-head>
    <my-nav></my-nav>
    <router-view></router-view>
  </div>
</template>

<script>
import myHead from './components/Header'
import myNav from './components/Nav'
export default {
  name: 'app',
  components: {myHead, myNav},
  provide () {
    return {
      reload: this.reload
    }
  },
  data () {
    return {
      isRouterAlive: true
    }
  },
  methods: {
    reload () {
      this.isRouterAlive = false
      this.$nextTick(function () {
        this.isRouterAlive = true
      })
    }
  }
}
</script>
  
<style>
</style>
