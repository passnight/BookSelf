<template>
  <div id="app">
    <my-head></my-head>
    <router-view></router-view>
  </div>
</template>

<script>
import myHead from './components/header.vue'
export default {
  name: 'book seller',
  components: { myHead }
}
</script>

<style>
  /* CSS */
</style>
