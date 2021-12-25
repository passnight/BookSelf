<template>
  <div class="checkoutCar">

         <body>
        <div id="app">
          <div class="checkoutBar">
            <h2>支付清单</h2>
              <table>
                <tr>
        <th>商品名称</th>
        <th>数量</th>
        <th>单价（元）</th>
        <th>金额（元）</th>
        </tr>

        <tr v-for="(item,index) in car" v-bind:key="index" class="commodity">

        <th class="content">
        <img src="../assets/book_picture.jpg" width="100px" height="100px">
        <p>{{item.title}}</p>
        </th>
        <th>
        <span>{{item.quantities}}</span>
        </th>
        <th>{{item.price}}</th>
        <th class="money">{{item.price * item.quantities}}</th>

        </tr>
        </table>
        <div class="checkoutBar-footer">
        <div class="manage">

        <router-link to="/shoppingCart"><span class="return">返回</span></router-link>

        </div>
        <button id="go" type="button" @click="pay">支付</button>
        <div class="buy">
        <span>{{quantitiesAll}}</span>
        件商品总计:
        <span>￥{{totalPrice}}</span>
        </div>
        </div>
        </div>
        </div>


        </body>

  </div>
</template>

<script>
import axios from 'axios'
export default {
  name: 'checkout-page',
  data() {
    return{
      car: this.$store.state.car,
      quantitiesAll: 0,
      totalPrice: 0
    }
  },
  methods: {
      Init() {
        for(var index in this.car) {
            this.quantitiesAll+=this.car[index].quantities
            this.totalPrice+=this.car[index].quantities*this.car[index].price
        }
      },
      pay() {
        axios
        .get("/shopping_basket/pay",{
          params:{
            user_id: this.$store.state.user.userId
          }
        })
        .then((res) => {
			    console.log(res.data);
          if (res.data.code == 200) {
            alert("支付成功");
            this.$router.push("/")
          } else {
            
          }
        });
      }
  },
  mounted:function () {   //自动触发写入的函数
    this.Init();
  }
}
</script>

<style>
.buy{
    font-weight: bold;
}

.buy span{
    color:red;
    font-size: 20px;
}

.checkoutCar body{
  margin:0;
  padding:0;
  height:auto;
  text-decoration:none;
  list-style:none;
  font-size:12px;
  background-color:#f5f5f5
}


hr{
  width:100%;height:2px;background-color:#ff6700
}

.checkoutBar{
  width:1130px;
  border:2px solid #f5f5f5;
  margin:40px auto;
  position:relative;
  background-color:#fff;font-size:16px
}

.checkoutBar h2{
  height:60px;line-height:60px;
  color:#000;text-indent:40px
}

.checkoutBar table{
  width:100%;
  margin-bottom:60px
}

.checkoutBar table .money{
  color:red
}

.checkoutBar table .commodity{
  border:3px solid #f5f5f5;
  height:150px
}

.checkoutBar>table tr th input{
  width:25px;
  height:25px;
  margin-left:30px
}

.checkoutBar table tr:first-of-type{
  height:80px;color:#424242;
  font-size:14px;
  border-top:1px solid #f5f5f5;
  border-bottom:1px solid #f5f5f5
}

.checkoutBar table tr th img{
  width:120px;
  height:100px;
  float:left
}

.checkoutBar table tr th p{
  float:right;width:100px;
  font-size:18px;
  color:#424242
}

.checkoutBar table tr .content{
  width:220px;
  padding:0 100px
}

.checkoutBar table tr #delete{
  cursor:pointer;
  font-size:20px
}

.checkoutBar table tr #delete:hover{
  color:red
}

.checkoutBar .checkoutBar-footer{
  border:1px solid #f5f5f5;
  width:1130px;
  height:60px;
  position:absolute;
  margin-top:10px;
  color:#757575;
  font-size:14px;
  background-color:#fff
}

.checkoutBar .checkoutBar-footer .manage{
  float:left;
  height:40px
}

.checkoutBar .checkoutBar-footer .manage .delAll,.return{
  cursor:pointer;
  background:#f5f5f5;
  color:#757575;line-height:60px;margin:0 30px
}

.checkoutBar .checkoutBar-footer .manage .delAll,.return:hover{
  color:#ff6700;
  transition:all .5s ease-in-out
}

.checkoutBar .checkoutBar-footer .manage .del,.return{
  cursor:pointer;
  background:#f5f5f5;
  color:#757575;line-height:60px;margin:0 30px
}

.checkoutBar .checkoutBar-footer .manage .del,.return:hover{
  color:#ff6700;
  transition:all .5s ease-in-out
}

.checkoutBar .checkoutBar-footer .buy{
  float:right;
  height:40px;
  line-height:60px
}
  
.checkoutBar .checkoutBar-footer #go{
  float:right;
  height:60px;
  width:110px;
  font-weight:400;
  font-size:18px;
  outline:none;
  background-color:red;
  border:none;
  border-radius:2px;
  margin-left:10px;
  cursor:pointer;
  color:#fff
}
</style>