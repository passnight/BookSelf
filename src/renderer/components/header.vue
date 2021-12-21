<template>
  <div id="wrapper">

    <!-- 顶部 -->
    <div class="header">
    <div ></div>

      <!--顶部图片 logo-->
      <div id="header-content" style="display:flex">
        <img id="logo" src="~@/assets/logo.png">
        <div id="title">Book Shelf</div>
      </div>


    </div>

    

    <main>
      <div class="left-side">
        <span class="title">
 
        </span>
      </div>

      <div class="right-side">
        <div class="doc">

        </div>
        <div class="doc">
        </div>
      </div>
    </main>
  </div>
</template>

<script>
  export default {
    name: 'my-header'
  }
</script>

<style>


  #logo {
    height: 100px;
    width: 100px;
  }


  #title{
    font-size: 40px;  
    color: rgb(243, 236, 236);
    margin: 0 auto;
    position: relative;
    left: -40px;
    top: 30px;
    font-family:'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
  }

  #wrapper{
    text-align: center;
  }



  .header{

    background: url("../assets/headerBackground.jpg") no-repeat;
     width:100%;
     height: 150px;
    background-size:100% 100%;
  }


  #header-content{
    position: relative;
    top: 15px;
    width: 400px;
    margin: 0 auto;
  }

</style>
