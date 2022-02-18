import { createRouter, createWebHistory } from 'vue-router'
import Home from '../views/Home.vue'
// import Showtime from '../views/Showtime.vue'
// import Booking from '../views/Booking.vue'
import Product from '../views/Product.vue'
import Account from '../views/Account.vue'
import { findProp } from '@vue/compiler-core'

const routes = [
    {
        path: '/',
        name: 'Home',
        component: Home
    },
    //   {
    //     path: '/about',
    //     name: 'About',
    //     // route level code-splitting
    //     // this generates a separate chunk (about.[hash].js) for this route
    //     // which is lazy-loaded when the route is visited.
    //     component: () => import(/* webpackChunkName: "about" */ '../views/About.vue')
    //   },
    {
        path: "/product/:key/:slug",
        name: 'Product',
        component: Product
    },
    {
        path: '/account',
        name: 'Account',
        component: Account,
    },
]

const router = createRouter({
    history: createWebHistory(),
    // history: createWebHistory(process.env.BASE_URL),
    routes,
})

router.beforeEach((to, from, next) => {
    window.scroll({ top: 0, left: 0, behavior: "auto" });
    next()
})

export default router