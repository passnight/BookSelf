import { stat } from 'original-fs';
import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
    state: {
        //用户信息
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
        //搜索结果
        bookList : [{
            title:'book1',
            id: 0
        },{
            title:'book2',
            id: 1
        },{
            title:'book3',
            id: 2
        }],
        //详情页书Id
        bookDetailId : -1,
        // 购物车 本地存储，防止数据丢失
        car : [],
        // 总价
        detailBookId: -1
    },
    getters: {
        bookList(state) {
            return state.bookList;
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
            state.user.userId=userId;
        },
        //添加书目
        addBookList(state, book) {
            state.bookList.push(book);
        },
        //添加详情页书目id
        setBookDetail(state,id) {
            state.bookDetailId=id;
        },
        addCar(state,book){
            state.car.push(book)
        }
    },
    actions: {
       
    }
})