<template>
  <div class="login-body">
    <div class="loginBox">
		<h2>login</h2>
		<form action="">
			<div class="item">
				<input type="text" required v-model="loginForm.login_username">
				<label for="">userName</label>
			</div>
			<div class="item">
				<input type="password" required v-model="loginForm.login_password">
				<label for="">password</label>
			</div>
			<button type="button" class="login-btn" @click="login">submit
				<span></span>
				<span></span>
				<span></span>
				<span></span>
			</button>
            <div class="msg">
                Don't have account?
                <router-link to="/register"><a>sign up</a></router-link>
            </div>
            <div class="msg">
                Forget your password?
                <router-link to="/findPassword"><a>find password</a></router-link>
            </div>
		</form>
	</div>
</div>
</template>

<script>
export default {
  name: 'login-page',
  data () {
    return {
      loginForm: {
        login_username: '',
        login_password: ''
      },
      userToken: ''
    }
  },
  methods: {
    login () {
      var passwordreg = /^[a-zA-Z0-9]{8,32}$/
      if (this.loginForm.login_username === '') {
        alert('账号不能为空')
      } else if (this.loginForm.login_password === '') {
        alert('密码不能为空')
      } else if (!passwordreg.test(this.loginForm.login_password)) {
        alert('密码由8-32位数字和字母组成')
      } else {
		alert('登陆成功')
        // this.axios({
        //   method: 'post',
        //   url: '/user/login',
        //   data: _this.loginForm
        // }).then(res => {
        //   console.log(res.data);
        //   _this.userToken = 'Bearer ' + res.data.data.login-body.token;
        //   // 将用户token保存到vuex中
        //   _this.changeLogin({ Authorization: _this.userToken });
        //   _this.$router.push('/home');
        //   alert('登陆成功');
        // }).catch(error => {
        //   alert('账号或密码错误');
        //   console.log(error);
        // });
      }
    }
  }
}
</script>

<style>
.a {
	text-decoration: none;
}
.loginBox input,
.loginBox button {
	background: transparent;
	border: 0;
	outline: none;
}

.login-body {
    height: 100%;
	background: linear-gradient(#141e30, #243b55);
	display: flex;
	justify-content: center;
	align-items: center;
	font-size: 16px;
	color: #03e9f4;
}

.loginBox {
	width: 400px;
	height: 364px;
	background-color: #0c1622;
	margin: 190px auto;
	border-radius: 10px;
	box-shadow: 0 15px 25px 0 rgba(0, 0, 0, .6);
	padding: 40px;
	box-sizing: border-box;
}

h2 {
	text-align: center;
	color: aliceblue;
	margin-bottom: 30px;
	font-family: 'Courier New', Courier, monospace;
}
		
.item {
	height: 45px;
	border-bottom: 1px solid #fff;
	margin-bottom: 40px;
	position: relative;
}

.item input {
	width: 100%;
	height: 100%;
	color: #fff;
	padding-top: 20px;
	box-sizing: border-box;
}

.item input:focus+label,
.item input:valid+label {
	top: 0px;
	font-size: 2px;
}

.item label {
	position: absolute;
	left: 0;
	top: 12px;
	transition: all 0.5s linear;
}

.login-btn {
	padding: 10px 20px;
	margin-top: 10px;
	color: #03e9f4;
	position: relative;
	overflow: hidden;
	text-transform: uppercase;
	letter-spacing: 2px;
	left: 35%;
}

.login-btn:hover {
	border-radius: 5px;
	color: #fff;
	background: #03e9f4;
	box-shadow: 0 0 5px 0 #03e9f4,
		0 0 25px 0 #03e9f4,
		0 0 50px 0 #03e9f4,
		0 0 100px 0 #03e9f4;
	transition: all 1s linear;
}

.login-btn>span {
	position: absolute;
}

.login-btn>span:nth-child(1) {
	width: 100%;
	height: 2px;
	background: -webkit-linear-gradient(left, transparent, #03e9f4);
	left: -100%;
	top: 0px;
	animation: line1 1s linear infinite;
}

@keyframes line1 {
	50%,
	100% {
		left: 100%;
	}
}

.login-btn>span:nth-child(2) {
	width: 2px;
	height: 100%;
	background: -webkit-linear-gradient(top, transparent, #03e9f4);
	right: 0px;
	top: -100%;
	animation: line2 1s 0.25s linear infinite;
}

@keyframes line2 {
	50%,
	100% {
		top: 100%;
	}
}

.login-btn>span:nth-child(3) {
	width: 100%;
	height: 2px;
	background: -webkit-linear-gradient(left, #03e9f4, transparent);
	left: 100%;
	bottom: 0px;
	animation: line3 1s 0.75s linear infinite;
}

@keyframes line3 {
	50%,
	100% {
		left: -100%;
	}
}

.login-btn>span:nth-child(4) {
	width: 2px;
	height: 100%;
	background: -webkit-linear-gradient(top, transparent, #03e9f4);
	left: 0px;
	top: 100%;
	animation: line4 1s 1s linear infinite;
}

@keyframes line4 {
	50%,
	100% {
		top: -100%;
	}
}

.msg{
   margin-top: 10px;
}
</style>