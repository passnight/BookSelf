<template>
  <div>
  <div class="mainBackground"></div>
  </div>
</template>

<script>
export default {
  name: 'landing-page'
}
</script>

<style>

.mainBackground{
  position:fixed;

    background: url("../assets/main.png") no-repeat;
    width:100%;
		height:100%;
    background-repeat: no-repeat;
    background-size: cover;
    -webkit-background-size: cover;
    -o-background-size: cover;
    background-position: center 0;
  }

</style>
