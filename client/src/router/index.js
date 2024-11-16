import { createRouter, createWebHistory } from 'vue-router'
import Ping from '../components/Ping.vue'
import Books from '../components/Books.vue'
import Bujo from '../components/Bujo.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'bujo',
      component: Bujo
    },
    {
      path: '/books',
      name: 'books',
      component: Books
    },
    {
      path: '/ping',
      name: 'ping',
      component: Ping
    },
  ]
})

export default router