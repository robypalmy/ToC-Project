<template>
  <v-app>
    <!--  <img alt="Vue logo" src="./assets/logo.png">-->
    <!-- <HelloWorld msg="Welcome to Your Vue.js App"/> -->
    <InputFile/>
  </v-app>
</template>

<script>
// import HelloWorld from './components/HelloWorld.vue'
import InputFile from './components/InputFile.vue'

export default {
  name: 'App',
  components: {
    InputFile
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
