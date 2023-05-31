import { createApp } from 'vue';
import App from '../App.vue';
import { createRouter, createWebHistory } from 'vue-router';
import About from '../pages/AboutPage.vue';
import GraphGenerator from '../pages/GraphGenerator.vue';
import HomeApp from '../pages/Home.vue'; // Your root component

// Vuetify
import 'vuetify/styles'
import { createVuetify } from 'vuetify'
import * as components from 'vuetify/components'
import * as directives from 'vuetify/directives'

const vuetify = createVuetify({
  components,
  directives,
})

const router = createRouter({
  history: createWebHistory(),
  routes: [
    { path: '/', component: HomeApp },
    { path: '/about', component: About },
    { path: '/graphGenerator', component: GraphGenerator }
  ],
});

const app = createApp(App);
app.use(vuetify);
app.use(router);
app.mount('#app');
