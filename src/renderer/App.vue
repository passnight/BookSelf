<template>
  <div id="app">
    <my-head></my-head>
    <my-nav></my-nav>
    <router-view></router-view>
  </div>
</template>

<script>
import myHead from './components/header.vue'
import myNav from './components/nav.vue'
export default {
  name: 'book seller',
  components: { myHead, myNav }
}
</script>

<style>
  /* CSS */
</style>
