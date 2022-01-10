import { createStore } from 'vuex'

export default createStore({
  state: {
    user: {
      email: '',
    },
    isAuthenticated: false,
    token: '',
    // ticket: false,
    // bookingData: {},
    // seatSelected: false,
  },
  mutations: {
    initializeStore(state) {
      if (localStorage.getItem('token')) {
        state.token = localStorage.getItem('token')
        state.isAuthenticated = true
      }
      else {
        state.token = ''
        state.isAuthenticated = false
      }
    },
    setToken(state, token) {
      state.token = token
      state.isAuthenticated = true
    },
    removeToken(state) {
      state.token = ''
      state.isAuthenticated = false
    },
    // getBookingData(state) {
    //   if (localStorage.getItem('bookingData')) {
    //     state.bookingData = localStorage.getItem('bookingData')
    //   }
    // },
    setBookingData(state, bookingData) {
      localStorage.setItem('bookingData', JSON.stringify(bookingData))
      // state.bookingData = localStorage.getItem('bookingData')
    },
    setTicket(state, bookingData) {
      localStorage.setItem('bookingData', JSON.stringify(bookingData))
      // state.ticket = true;
    },
    // setSeat(state, seat) {
    //   localStorage.setItem('seat', seat)
    //   state.seatSelected = true;
    // }
  },
  actions: {
  },
  modules: {
  }
})
