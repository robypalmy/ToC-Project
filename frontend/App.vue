<template>
  <v-app app>
    <HeaderApp/>
    <router-view></router-view>
  </v-app>
</template>

<script>

import HeaderApp from './src/components/Header/HeaderApp.vue'

export default {
  name: 'App',
  components: {
    HeaderApp
  }
}
</script>

<style scoped>
.appl {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  display: flex;
  align-items: center;
  justify-content: space-around;
  flex-direction: column;
  min-height: 100vh;
  min-width: 100vw;
}

</style>
