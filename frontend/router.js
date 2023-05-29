import Vue from 'vue';
import VueRouter from 'vue-router';

Vue.use(VueRouter);

const routes = [
  // Define your routes here
  {
    path: '/',
    component: Home,
  },
  {
    path: '/about',
    component: About,
  },
  {
    path: '/projects',
    component: Projects,
  },
];

const router = new VueRouter({
  routes,
  mode: 'history', // Use 'history' mode to remove the '#' from URLs
});

export default router;
