import { createRouter, createWebHistory } from 'vue-router'
import Home from '../views/Home.vue'
import Showtime from '../views/Showtime.vue'
import Booking from '../views/Booking.vue'
import { findProp } from '@vue/compiler-core'

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/about',
    name: 'About',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/About.vue')
  },
  {
    path: '/showtime/:id/:slug',
    name: 'Showtime',
    // props: true,
    component: Showtime
  },
  {
    path: '/booking/',
    name: 'Booking',
    props: true,
    component: Booking,
    // beforeRouteLeave: (to, from, next) => {
    //   if (localStorage.getItem("ticket")) localStorage.removeItem("ticket");
    //   next()
    // }
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

router.beforeEach((to, from, next) => {
  // console.log("I came to ", to.name)
  // console.log("I came from ", from.name)
  // console.log();
  if (to.name === 'Booking' && from.name !== undefined || from.name === 'Booking' || from.name === undefined && to.name !== "Booking") {
    if (localStorage.getItem("bookingData")) localStorage.removeItem("bookingData");
  }
  next()
})

export default router
