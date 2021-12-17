<template>
        <!-- 导航栏 -->
    <div class="topnav">
    <ul>
      <li><router-link to="/"><a href="#home" >主页</a></router-link></li>
      <li><router-link to="/test"><a href="#news">搜索</a></router-link></li>
      <li><router-link to=""><a href="#contact">222</a></router-link></li>
      <li><router-link to=""><a href="#about">333</a></router-link></li>
    </ul>
  </div> 
</template>

<script>
export default {

}
</script>

<style>
  * {
    box-sizing: border-box;
    margin: 0px;
    padding: 0px;
  }

  .topnav {
    margin: 0px 0px;
    background-color: #777777;
    overflow: hidden;  /*清除浮动，否则会父级坍塌*/
  }

  .topnav ul {
    list-style-type: none;
  }

  .topnav ul li a {
    float: left;
    padding: 10px;
    text-decoration: none;
    color: white;
  }

  .topnav ul li a:hover {
    background-color: black;
  }

  .topnav ul li a.active {
    background-color: #4CAF50;
  }
</style>