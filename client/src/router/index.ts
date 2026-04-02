import { createRouter, createWebHistory } from 'vue-router'
import AnimaliumView from '@/views/AnimaliumView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'animalium',
      component: AnimaliumView,
    },
  ],
})

export default router
