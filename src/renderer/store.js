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
        // 购物车 本地存储，防止数据丢失
        car: localStorage["car"] ? JSON.parse(localStorage["car"]) : [],
        // 总价
        totlePrice: 0,
        // 全选状态
        all_selected: false,
        // 购物车中购买的数量
        payNum: 0,
        // list页面控制‘加入购物车按钮’的样式  本地存储，防止数据丢失
        isShow: localStorage["isShow"] ? JSON.parse(localStorage["isShow"]) : []
    },
    getters: {
        user (state) {
            return state.user;
        },
        // 时时监听car的变化
        carList(state) {
            // 初始化全选状态
            if (state.all_selected) {
                state.car.forEach(item => item.isBuy = true)
            }
            return state.car;
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
        },
        // 购买的商品的总数量
        payLength(state) {
            let paylength = 0
            state.car.forEach(item => {
                if (item.isBuy) {
                    paylength += item.num
                }
            })
            return  state.payNum = paylength;
        }
    },
    // 同步消息
    mutations: {
        // 从购物车中删除该商品
        deleteProduct(state, id) {
            // 商品在购物车中索引值
            let index = state.car.findIndex(item => item._id === id)
            // 商品在isShow中的索引值
            let indexShow = state.isShow.findIndex(item =>item.id === id)
            // 将购物车中该商品的selected属性改成false
            state.car[index].selected = false;
            // 从购物车中删除该商品
            state.car.splice(index, 1)
            // 从本地存储的购物车中删除该商品（即将删除了该商品的购物车赋值给本地存储）
            localStorage.setItem('car', JSON.stringify(state.car))
            // console.log(5555,state.car, state.isShow[index].show)
            // 将isShow中该商品的show属性改成相反的值
            state.isShow[indexShow].show = !state.isShow[indexShow].show
            // 将isShow赋值给本地
            localStorage.setItem('isShow', JSON.stringify(state.isShow)) 

        },
        // 商品数量增加
        addNum(state, id) {
            let index = state.car.findIndex(item => item._id === id)
            if (index >= 0) {
                state.car[index].num ++;
            }
        },
        // 数量减少
        reduceNum(state, id) {
            let index = state.car.findIndex(item => item._id === id);
            let indexShow = state.isShow.findIndex(item =>item.id === id)
            console.log('indexShow', indexShow)
            // 当数量为1时，从购物车里面删除
            if (state.car[index].num === 1) {
                // 逻辑同deleteProduct
                state.car[index].selected = false;
                state.car.splice(index, 1)
                localStorage.setItem('car', JSON.stringify(state.car))
                state.isShow[indexShow].show = !state.isShow[indexShow].show
                localStorage.setItem('isShow', JSON.stringify(state.isShow)) 
            } else {
                state.car[index].num --;
            }
            
        },
        // 加入购物车
        addCar(state, data) {
            // 修改传递进来的商品的属性 数量为1，默认选中加入购物车，默认加入购物车后先不购买
            // 数据丢失
            // Object.assign(data, {num: 1, selected: true, isBuy: false})
            let datas = {
                title: data.title,
                num: 1,
                selected: true,
                isBuy: false,
                img: data.img,
                sales: data.sales,
                _id: data._id,
                price: data.price
            }
            // 在购物车中查找该商品
            let index = state.car.findIndex(item => item._id === data._id)
            // 如果返回-1，说明购物车中没有该商品，将其添加进购物车
            // 当购物车中已经有该商品了则不再继续往里面添加该商品
            if (index === -1) {
                state.car.push(datas)
            }
            // 将购物车中的商品存入本地存储中，为了之后做页面的路由拦截
            localStorage.setItem('car', JSON.stringify(state.car))
        },
        // 单选  选择是否购买该商品
        selectSingle(state, id) {
            // 查找购物车中该商品的的索引值
            let index = state.car.findIndex(item => item._id === id)
            // console.log(111, state.car[index].isBuy, state.car[index].selected)
            // 将购物车中该商品选择属性取反
            state.car[index].isBuy = !state.car[index].isBuy;
            // console.log(222, state.car[index].isBuy)
            // 判断是否全选(如果有一个是未选中，则flag为true，如果全选中则flag为false)
            let flag = state.car.some(item => item.isBuy === false)
            // 全选中
            if (!flag) {
                state.all_selected = true
            } else {
                // 没有全选中
                state.all_selected = false
            }
        },
        // 全选
        selectAll(state) {
            // 取消所有商品的isBuy
            if (state.all_selected) {
                state.car.forEach(item => item.isBuy = false)
            } else {
                // 将所有商品的isBuy属性改成true
                state.car.forEach(item => item.isBuy = true)
            }
            state.all_selected = !state.all_selected;
        }
    },
    actions: {
       
    }
})