<template>
  <v-app>
    <v-app-bar app class="my-app-bar">
      <HeaderApp/>
    </v-app-bar>
    <v-main>
      <!--  <img alt="Vue logo" src="./assets/logo.png">-->
      <!-- <HelloWorld msg="Welcome to Your Vue.js App"/> -->
      <InputFile/>
    </v-main>
  </v-app>
</template>

<script>
// import HelloWorld from './components/HelloWorld.vue'
import InputFile from './components/InputFile.vue'
import HeaderApp from './components/HeaderApp.vue'

export default {
  name: 'App',
  components: {
    InputFile,
    HeaderApp
  }
}
</script>

<style scoped>



#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  display: flex;
  align-items: center;
  justify-content: center;
  margin: 50px;
  
}


#main {
  display: flex;
  align-items: center;
  justify-content: center;
  text-align: center;
  color: #2c3e50;

}



</style>
