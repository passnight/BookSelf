<template>
  <div class="search-body">
    <div class="searchBox">
		  <h2>search</h2>
		    <form action="">
		  <div class="search-item">
            <label for="">bookISBN</label>

            <input  v-model="searchForm.isbn">
          </div>
          <div class="search-item">
            <label>bookTitle</label>
            <input v-model="searchForm.booktitle">	
          </div>
          <div class="search-item">
            <label for="">bookAuthor</label>

            <input  v-model="searchForm.author">
          </div>
         
          <button type="button" class="search-btn" @click="search">submit
            <span></span>
            <span></span>
            <span></span>
            <span></span>
          </button>
		</form>
	</div>
</div>
</template>

<script>
import axios from "axios";
export default {
  name: 'search-page',
  data () {
    return {
      searchForm: {
		isbn: '',
        booktitle: '',
        author: ''
	  }
    }
  },
  methods: {
    search () {
      axios
        .get("/book/search",{
          params:{
            isbn: this.searchForm.isbn,
            title: this.searchForm.booktitle,
            author: this.searchForm.author
          }
        })
        .then((res) => {
			    console.log(res.data);
          if (res.data.code == 200) {
            this.$store.commit('updateBookList',res.data.data.bookList)
			this.$store.commit('setSearchState',true)
            this.$router.push('/bookList')
          } else {
            alert("出错了");
			this.$router.push('/search')
          }
        });
    }
  }
}
</script>

<style>
.a {
	text-decoration: none;
}

.searchBox input,
.searchBox button {
	background: transparent;
	border: 0;
	outline: none;
}

.search-body {
    height: 100%;
	background: linear-gradient(#141e30, #243b55);
	display: flex;
	justify-content: center;
	align-items: center;
	font-size: 16px;
	color: #03e9f4;
}

.searchBox {
	width: 400px;
	height: 426px;
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
		
.search-item {
	height: 45px;
	border-bottom: 1px solid #fff;
	margin-bottom: 40px;
	position: relative;
  display: flex;
}

.search-item input {
	width: 100%;
	height: 100%;
	color: #fff;
	padding-top: 20px;
	box-sizing: border-box;
}

.search-item input:focus+label,
.search-item input:valid+label {
	top: 0px;
	font-size: 2px;
}

.search-item label {
	position: absolute;
	left: 0;
	top: 12px;
	transition: all 0.5s linear;
}

.search-btn {
	padding: 10px 20px;
	margin-top: 10px;
	color: #03e9f4;
	position: relative;
	overflow: hidden;
	text-transform: uppercase;
	letter-spacing: 2px;
	left: 35%;
}

.search-btn:hover {
	border-radius: 5px;
	color: #fff;
	background: #03e9f4;
	box-shadow: 0 0 5px 0 #03e9f4,
		0 0 25px 0 #03e9f4,
		0 0 50px 0 #03e9f4,
		0 0 100px 0 #03e9f4;
	transition: all 1s linear;
}

.search-btn>span {
	position: absolute;
}

.search-btn>span:nth-child(1) {
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

.search-btn>span:nth-child(2) {
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

.search-btn>span:nth-child(3) {
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

.search-btn>span:nth-child(4) {
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
</style>