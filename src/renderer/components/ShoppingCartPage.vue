<template>
  <div class="shoppingCar">
    <div v-if="isCarEmpty">
        <h1>购物车内没有物品</h1>
    </div>

    <div v-else>
      <body>
        <div id="app">
          <div class="shoppingBar">
            <h2>购物清单</h2>
              <table>
                <tr>
                  <th>
                    <input type="checkbox"  v-model="isCheckedAll" @change="checkedAll($event)">
        全选
        </th>
        <th>商品名称</th>
        <th>数量</th>
        <th>单价（元）</th>
        <th>金额（元）</th>
        </tr>

        <tr v-for="(item,index) in car" v-bind:key="index" class="commodity">
        <th>
        <input v-model="isCheck[index]" type="checkbox" class="input">
        </th>
        <th class="content">
        <img src="../assets/book_picture.jpg" width="100px" height="100px">
        <p>{{item.title}}</p>
        </th>
        <th>
        <button type="button" @click="decrease(index)">-</button>
        <span>{{item.quantities}}</span>
        <button type="button" @click="add(index)">+</button>
        </th>
        <th>{{item.price}}</th>
        <th class="money">{{item.price * item.quantities}}</th>
        <th>
        <span id="delete" @click="deleteThis(index)" class="glyphicon glyphicon-remove"></span>
        </th>
        </tr>
        </table>
        <div class="shoppingBar-footer">
        <div class="manage">
        <span class="del" @click="deleteSelected">删除所选商品</span>
        <span class="delAll" @click="deleteAll">清空</span>
        <span class="return" @click="shopContinue">继续购物</span>
        <span v-if="!isSave" class="return" @click="save">保存更改</span>
        </div>
        <button id="go" type="button" @click="buy">去结算</button>
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
  </div>
</template>

<script>
import axios from 'axios'
export default {
  inject:['reload'],
  name: 'shoppingCart-page',
  data() {
    return{
      car: this.$store.state.car,
      isCarEmpty: this.$store.state.isCarEmpty,
      isCheck: [],
      isCheckedAll: false,
      isSave: true
    }
  },
  computed:{
    quantitiesAll: function() {
      var sum=0;
      if(this.car.length < 1)
        return
      
      if(this.isCheckedAll) {
        for(var i in this.isCheck) {
          sum+=this.car[i].quantities;
        }
        return sum;
      }

      for(var i in this.isCheck) {
        if(this.isCheck[i]) {
          sum+=this.car[i].quantities;
        }
      }
      return sum;
    },
    totalPrice: function() {
      var sum1=0;
      if(this.car.length < 1)
        return

      if(this.isCheckedAll) {
        for(var i in this.isCheck) {
          sum1+=this.car[i].quantities*this.car[i].price;
        }
        return sum1;
      }
      for(var i in this.isCheck) {
        if(this.isCheck[i]) {
          sum1+=this.car[i].quantities*this.car[i].price;
        }
      }
      return sum1;
    },
  },
  watch: {
    'isCheck': function() {
      for(var i in this.isCheck) {
        if(this.isCheck[i] == false) {
          this.isCheckedAll=false;
          return
        }
      }
      this.isCheckedAll=true;
    }
  },
  methods: {
    shopContinue(){
      this.$router.push('/bookList')
    },
    decrease: function(index) {
      if(this.car[index].quantities==1) {
        alert("修改数量不能小于0");
        return;
      } else {
        this.car[index].quantities--;
        if(this.isSave)
        this.isSave=false;
      } 
    },
    add: function(index) {
      if(this.car[index].quantities==20) {
        alert("购买的商品数量不能超过20件！");
        return; 
      } else {
        this.car[index].quantities++;
        if(this.isSave)
        this.isSave=false;
      }
    },
    checkInit() {
      for(var i in this.car)
        this.isCheck.push(false)
    },
    checkedAll: function(e) {
      var isCheckedAll=e.target.checked;
      if(isCheckedAll) {
        for(var i in this.isCheck) {
          this.isCheck[i]=true;
        }
      } else {
        for(var i in this.isCheck) {

          this.isCheck[i]=false;
        }
      }
    },
    deleteThis: function(index) {
      var falg=confirm("您确定要删除此商品吗？");
      if(falg) {
        this.car.splice(index,1);
      } else {
        return false;
      }
    },
    deleteSelected: function() {
      var isFinish=true
      for(var i=this.car.length-1;i>=0;i--) {
        if(this.isCheck[i]) {
          axios
          .get("/shopping_basket/delete_item",{
            params:{
              item_id: this.car[i].item_id
            }
          })
          .then((res) => {
            console.log(res.data);
            if (res.data.code == 200) {
            } else {
              isFinish=false
            }
          });
        }
      }
      if(isFinish){
        alert("删除成功")
        this.car.splice(i,1);
      }
      else
        alert("删除失败")
    },
    deleteAll: function() {
      alert("清空！");
    },
    buy(){

      this.$router.push('/checkout')
    },
    save() {
      var userId=this.$store.state.user.userId
      var isFinish=true
      for(var i in this.car) {
        axios
        .get("/shopping_basket/update_item",{
          params:{
            user_id: userId,
            book_isbn: this.car[i].book_isbn,
            number: this.car[i].quantities
          }
        })
        .then((res) => {
			    console.log(res.data);
          if (res.data.code == 200) {
          } else {
            isFinish=false
          }
        });}
      if(isFinish)
        alert("保存成功")
      else
        alert("保存失败")
    }
  },
  mounted:function () {   //自动触发写入的函数
    this.checkInit();
  }
}
</script>

<style>
.shoppingCar body{
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

.shoppingBar{
  width:1130px;
  border:2px solid #f5f5f5;
  margin:40px auto;
  position:relative;
  background-color:#fff;font-size:16px
}

.shoppingBar h2{
  height:60px;line-height:60px;
  color:#000;text-indent:40px
}

.shoppingBar table{
  width:100%;
  margin-bottom:60px
}

.shoppingBar table .money{
  color:red
}

.shoppingBar table .commodity{
  border:3px solid #f5f5f5;
  height:150px
}

.shoppingBar>table tr th input{
  width:25px;
  height:25px;
  margin-left:30px
}

.shoppingBar table tr:first-of-type{
  height:80px;color:#424242;
  font-size:14px;
  border-top:1px solid #f5f5f5;
  border-bottom:1px solid #f5f5f5
}

.shoppingBar table tr th img{
  width:120px;
  height:100px;
  float:left
}

.shoppingBar table tr th p{
  float:right;width:100px;
  font-size:18px;
  color:#424242
}

.shoppingBar table tr .content{
  width:220px;
  padding:0 100px
}

.shoppingBar table tr #delete{
  cursor:pointer;
  font-size:20px
}

.shoppingBar table tr #delete:hover{
  color:red
}

.shoppingBar .shoppingBar-footer{
  border:1px solid #f5f5f5;
  width:1130px;
  height:60px;
  position:absolute;
  margin-top:10px;
  color:#757575;
  font-size:14px;
  background-color:#fff
}

.shoppingBar .shoppingBar-footer .manage{
  float:left;
  height:40px
}

.shoppingBar .shoppingBar-footer .manage .delAll,.return{
  cursor:pointer;
  background:#f5f5f5;
  color:#757575;line-height:60px;margin:0 30px
}

.shoppingBar .shoppingBar-footer .manage .delAll,.return:hover{
  color:#ff6700;
  transition:all .5s ease-in-out
}

.shoppingBar .shoppingBar-footer .manage .del,.return{
  cursor:pointer;
  background:#f5f5f5;
  color:#757575;line-height:60px;margin:0 30px
}

.shoppingBar .shoppingBar-footer .manage .del,.return:hover{
  color:#ff6700;
  transition:all .5s ease-in-out
}

.shoppingBar .shoppingBar-footer .buy{
  float:right;
  height:40px;
  line-height:60px
}
  
.shoppingBar .shoppingBar-footer #go{
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