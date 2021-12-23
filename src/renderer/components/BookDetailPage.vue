<template>
  <div class="book-wrapper">
    <div class="book-information">
      <img src="../assets/book_picture.jpg">

      <div class="book-detail">
        <div>书名：
          <div  class="book-title" >
          </div>
        </div>
        <div>作者：
          <div class="book-author">
          </div>
        </div>
        <div>价格：
          <div class="book-price">
            ¥46
          </div>
        </div>
      </div>

    </div>

    <div class="function">
      <button  type="button" class="detail-button" style="vertical-align:middle" @click="addShoppingCar">
        <span>添加到购物车 </span>
      </button>
    </div>

  </div>
</template>

<script>
export default {
  name: 'bookDetail-page',
  data () {
    return {
      book_title: ''
    }
  },
  methods: {
    addShoppingCar () {
      alert("加入购物车成功")
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
  padding: 15px;
}

.book-price{
  color: red;
  display: inline-block;
}

.function{
  margin-left: 50px;
  margin-top: 50px;
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