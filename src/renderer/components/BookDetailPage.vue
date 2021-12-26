<template>
  <div class="book-wrapper">
    <div class="book-information">
      <img src="../assets/book_picture.jpg">

      <div class="book-detail">
        <div>书名：
          <div  class="book-title" >
            {{book_title}}
          </div>
        </div>
        <div>作者：
          <div class="book-author">
            {{book_author}}
          </div>
        </div>
        <div>质量：
          <div class="book-quality">
            {{book_quality}}
          </div>
        </div>
        <div>isbn：
          <div class="book-isbn">
            {{book_isbn}}
          </div>
        </div>
        <div>价格：
          <div class="book-price">
            ¥{{book_price}}
          </div>
        </div>
      </div>

    </div>

    <div class="buttonBox">

    <div class="back">
      <button  type="button" class="back-button" style="vertical-align:middle" @click="back">
        <span>返回 </span>
      </button>
    </div>

    <div class="function">
      <button  type="button" class="detail-button" style="vertical-align:middle" @click="addShoppingCar">
        <span>添加到购物车 </span>
      </button>
    </div>

    </div>

  </div>
</template>

<script>
import axios from 'axios'
export default {
  name: 'bookDetail-page',
  data () {
    return {
      book_title: this.$store.state.bookList[this.$store.state.bookDetailId].title,
      book_author: this.$store.state.bookList[this.$store.state.bookDetailId].author,
      book_quality: this.$store.state.bookList[this.$store.state.bookDetailId].quality,
      book_price: this.$store.state.bookList[this.$store.state.bookDetailId].price,
      book_isbn: this.$store.state.bookList[this.$store.state.bookDetailId].isbn

    }
  },
  methods: {
    back() {
      this.$router.push('/bookList')
    },
    addShoppingCar () {
      if(this.$store.state.user.userId === -1)
        alert("请先登录")
      else {
        axios
        .get("/shopping_basket/add_item", {
          params: {
            user_id: this.$store.state.user.userId,
            book_isbn: this.book_isbn
          },
        })
        .then((res) => {
			    console.log(res.data);
          if (res.data.code == 200) {
            alert("添加购物车成功")    
          } else {
            if(res.data.data.msg === "购物车不存在，请先创建购物车")
              alert("请先完善支付方式")
            else if(res.data.data.msg === "书已存在购物车中")
              alert('此书已在购物车中')
          }
        });}
      
    }
  }
}
</script>

<style>

.book-wrapper{
  height:600px;

}

.book-information {
  height: 50%;
    display: flex;
    justify-content: flex-start;
}

.book-information img{
  height: 100%;
}

.book-detail div{
  font-size: 20px;
  font-weight: bold;
  padding: 10px;
}

.book-price{
  color: red;
  display: inline-block;
}
.book-title{
  display: inline-block;
}
.book-author{
  display: inline-block;
}
.book-isbn{
  display: inline-block;
}
.book-quality{
  display: inline-block;
}

.buttonBox{
  display: flex;
  justify-content: flex-start;
}

.function{
  margin-left: 110px;
  margin-top: 50px;
  display: flex;
}

.back{
  margin-left: 50px;
  margin-top: 50px;
}

.back-button {
  display: inline-block;
  border-radius: 4px;
  background-color: #7a6d69;
  border: none;
  color: #FFFFFF;
  text-align: center;
  font-size: 28px;
  padding: 20px;
  width: 300px;
  transition: all 0.5s;
  cursor: pointer;
  margin: 5px;
}

.back-button span {
  cursor: pointer;
  display: inline-block;
  position: relative;
  transition: 0.5s;
}

.back-button span:after {
  content: '«';
  position: absolute;
  opacity: 0;
  top: 0;
  left: -20px;
  transition: 0.5s;
}

.back-button:hover span {
  padding-left: 25px;
}

.back-button:hover span:after {
  opacity: 1;
  left: 0;
}

.detail-button {
  display: inline-block;
  border-radius: 4px;
  background-color: #f4511e;
  border: none;
  color: #FFFFFF;
  text-align: center;
  font-size: 28px;
  padding: 20px;
  width: 300px;
  transition: all 0.5s;
  cursor: pointer;
  margin: 5px;
}

.detail-button span {
  cursor: pointer;
  display: inline-block;
  position: relative;
  transition: 0.5s;
}

.detail-button span:after {
  content: '»';
  position: absolute;
  opacity: 0;
  top: 0;
  right: -20px;
  transition: 0.5s;
}

.detail-button:hover span {
  padding-right: 25px;
}

.detail-button:hover span:after {
  opacity: 1;
  right: 0;
}

</style>