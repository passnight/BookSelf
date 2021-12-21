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
  name: 'bookShelf',
  components: {myHead, myNav}
}
</script>
  
<style>
</style>
