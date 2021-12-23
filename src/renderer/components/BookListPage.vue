<template>
  <div>
    <div v-if="isHave">

    <!-- 搜索到结果 && 书库 -->
    <div id="booklist">
      <div v-for="item in booklist" v-bind:key="item.id"> 
        {{item.title}} <router-link to="/bookDetail"><button @click="toDetail(item.id)" type="button">详情</button></router-link>
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
      booklist: this.$store.state.bookList
    }
  },
  methods: {
    toDetail(id) {
      this.$store.commit("setBookDetail",id)
    }
  }
}
</script>

<style>

</style>