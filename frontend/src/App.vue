<template>
  <v-app class="appl">
    <HeaderApp/>
    <MainContent/>
  </v-app>
</template>

<script>
// import He lloWorld from './components/HelloWorld.vue'
import MainContent from './components/Main/MainContent.vue'
import HeaderApp from './components/Header/HeaderApp.vue'

export default {
  name: 'App',
  components: {
    MainContent,
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
}

.header {
  width: 100%;
  height: 100px;
  display: flex;
}

.myAppBar {
  height: 100px;
}


#main {
  display: flex;
  padding-top:10%;
  align-items: center;
  justify-content: center;
  text-align: center;
  color: #2c3e50;

}




</style>
