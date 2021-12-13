<template>
  <div>
  <div class="mainBackground"></div>
  </div>
</template>

<script>
export default {
  name: 'landing-page',
  methods: {
    open (link) {
      this.$electron.shell.openExternal(link)
    }
  }
}
</script>

<style>

.mainBackground{
  position:fixed;

    background: url("../assets/main.png") no-repeat;
    width:100%;
		height:100%;
    min-width: 1000px;
    background-repeat: no-repeat;
    background-size: cover;
    -webkit-background-size: cover;
    -o-background-size: cover;
    background-position: center 0;
  }

</style>
