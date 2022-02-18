import { createStore } from 'vuex'

export default createStore({
    state: {
        filters: {},
        isAuthenticated: false,
        token: '',
    },
    mutations: {
        INIT_STORE(state) {
            if (localStorage.getItem('token')) {
                state.token = localStorage.getItem('token')
                state.isAuthenticated = true
            }
            else {
                state.token = ''
                state.isAuthenticated = false
            }
        },
        SET_TOKEN(state, token) {
            state.token = token
            state.isAuthenticated = true
        },
        REMOVE_TOKEN(state) {
            state.token = ''
            state.isAuthenticated = false
        },
        SET_FILTERS(state, payload) {
            const key = Object.keys(payload)[0]
            const val = Object.values(payload)[0]

            if (key === 'availability' || key === 'category') {
                if (state.filters.hasOwnProperty(key)) {
                    if (state.filters[key].includes(val)) {
                        state.filters[key] = state.filters[key].filter(e => e !== val)
                        if (state.filters[key].length === 0) {
                            delete state.filters[key]
                        }
                    }
                    else {
                        state.filters[key].push(val)
                    }
                }
                else {
                    state.filters[key] = []
                    state.filters[key].push(val)
                }
            }
            else {
                if (state.filters.hasOwnProperty(key)) state.filters[key] = val
                else state.filters[key] = val
            }
            // console.log(JSON.stringify(state.filters));
        },
        CLEAR_FILTERS(state) {
            state.filters = {}
        },
    },
    actions: {
    },
    modules: {
    },
    getters: {
        filters: state => {
            return state.filters
        }
    }
})