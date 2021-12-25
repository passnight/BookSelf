import { stat } from 'original-fs';
import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
    state: {
        //用户信息
        isLogin: false,
        user: { 
            userId: -1,
            userName: '',
            userPassword: '',
            userEmail: ''
        },
        book: {
            title: '',
        },
        isBookList : true,
        //是否是搜索的结果？
        isSearch : false,
        //搜索结果（初始为本地测试数据）
        bookList : [{
            isbn: '111',
            quality: 'bad',
            title:'book1',
            author: 'chen',
            price: "46"
        },{
            isbn: '222',
            quality: 'good',
            title:'book2',
            author: 'rao',
            price: "88"
        }],
        //详情页书Id
        bookDetailId : -1,
        // 购物车 本地存储，防止数据丢失
        car : [],
        //购物车是否为空
        isCarEmpty: true,
        // 总价
        checkoutList: [],
        checkoutListId: -1,
        credit_card: '',
        isHavePayWay: false
    },
    getters: {
        bookList(state) {
            return state.bookList;
        },
        checkoutList(state) {
            return state.checkoutList
        },
        car(state) {
            return state.car;
        },
        user (state) {
            return state.user;
        },
        detailId(state){
            return state.bookDetailId
        },
        // 购买的总价钱
        allPrice(state) {
            let totlePrice = 0
            state.car.forEach(item => {
                // 如果加入购物车后点击了购买按钮
                if (item.isBuy) {
                    totlePrice += item.num * item.price
                }
            })
            return state.totlePrice = totlePrice
        }
    },
    // 同步消息
    mutations: {
        //登录成功
        login(state, userId) {
            state.isLogin=true;
            state.user.userId=userId;
        },
        //更新书库 && 搜索结果
        updateBookList(state, list) {
            state.bookList=list;
            if(state.bookList.length === 0)
                state.isBookList= false;
            else
                state.isBookList= true;
        },
        //设置当前是否是搜索
        setSearchState(state,search){
            state.isSearch=search;
        },
        //添加详情页书目id
        setBookDetail(state,id) {
            state.bookDetailId=id;
        },
        //添加到购物车
        addCar(state,book){
            if(state.isCarEmpty == true)
                state.isCarEmpty=false
            for(var i=0;i<state.car.length;i++)
                if(state.car[i].isbn == book.isbn) {
                    state.car[i].quantity++
                    return
                }
            state.car.push(book)
        },
        //更新购物车
        updateCar(state,car){
            state.car=car;
        }
    },
    actions: {
       
    }
})