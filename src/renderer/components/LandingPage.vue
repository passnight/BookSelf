<template>
  <div>
    <img class="mainBackground" src="~@/assets/main.png">
    <div class="frame">
      <h3>选择功能</h3>
      <form>
        <div v-if="isLogin">
          <h1>已登录</h1>
        </div>

        <div v-else>
          <router-link to="/login"><button>登录</button></router-link>
          <router-link to="/register"><button>注册</button></router-link>
        </div>
      </form>
    </div>
  </div>
</template>

<script>
export default {
  name: 'landing-page',
  data() {
    return {
      isLogin:this.$store.state.isLogin
    }
  }
}
</script>

<style>

.mainBackground{
    position: relative;
    width: 100%;

}

.frame {
    position:absolute;
    right:30px;
    top:250px;
    color:#63071c;
    font-weight: bold;
    font-family:'Trebuchet MS', 'Lucida Sans Unicode', 'Lucida Grande', 'Lucida Sans', Arial, sans-serif;
    padding: 13px;
    width: 60%;
    height: 100px;
    background-color: rgba(240, 255, 255, 0.3);
 
    border-radius: 20px;
    text-align: center;
}

.frame form{
  padding: 10px;
}


.frame form button{
  background-color: bisque;
  font-weight: bold;
  width: 100px;
  height: 30px;
}
</style>
