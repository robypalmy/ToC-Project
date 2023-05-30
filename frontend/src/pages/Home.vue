<template>
    <MainContent/>
</template>
  
<script>
import MainContent from '../components/Main/MainContent.vue'

export default {
    name: 'HomeApp',
    components: {
      MainContent
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
  
  
  .MainContent {
    display: flex;
    padding-top: 10%;
    align-items: center;
    justify-content: center;
    text-align: center;
    color: #2c3e50;
  }
  </style>
  