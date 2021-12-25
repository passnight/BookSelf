<template>
        <!-- 导航栏 -->
    <div class="topnav">
    <ul>
      <li><router-link to="/"><a href="#home" >主页</a></router-link></li>
      <li><router-link to="/search"><a href="#news">搜索</a></router-link></li>
      
      <li><router-link to="/bookList"><a href="#about">书库</a></router-link></li>
      <li><router-link to="/shoppingCart"><a href="#contact">购物车</a></router-link></li>
      <li><router-link to="/creatCar"><a href="#contact">添加购物车</a></router-link></li>

    </ul>
  </div> 
</template>

<script>
export default {
  name: 'nav-page',
  methods: {
  }

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