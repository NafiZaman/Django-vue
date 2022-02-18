import { createApp } from 'vue'
import App from './App.vue'
import './index.css'
import router from './router'
import axios from 'axios'
import store from './store'
import moment from 'moment';
import 'flowbite';

// axios.defaults.baseURL = 'https://myboringproject.com'
axios.defaults.baseURL = 'http://127.0.0.1:8000'


createApp(App).use(store).use(router, axios, moment).mount('#app')
