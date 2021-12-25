<template>
  <div>
    <div v-if="isHave">
      <div v-if="isSearch">
        <h1>搜索结果如下：</h1>
      </div>
      <div v-else>
        <h1>书库如下：</h1>
      </div>

      <!-- 搜索到结果 && 书库 -->
      <div id="booklist">
        <div v-for="(item,index) in booklist" v-bind:key="index"> 
          {{item.title}} <router-link to="/bookDetail"><button @click="toDetail(index)" type="button">详情</button></router-link>
        </div>
      </div>

    
    </div>

    <!-- 搜索不到结果 -->
    <div v-else>
    <h1>找不到搜索的结果</h1>
    </div>
  </div>
</template>

<script>
export default {
  name: 'bookList-page',
  data() {
    return {
      isHave: this.$store.state.isBookList,
      booklist: this.$store.state.bookList,
      isSearch: this.$store.state.isSearch
    }
  },
  methods: {
    toDetail(id) {
      this.$store.commit("setBookDetail",id)
    }
  },
  destroyed: function () {
    //离开页面时搜索重置
    this.$store.commit('setSearchState',false)
  }
}
</script>

<style>
#booklist div{
  font-size: 20px;
  padding: 8px;
}
#booklist div button{
  margin-left: 10px;
}
</style>