<template>
  <div app class="container">
    <div class="logo">
      <h1> Formula Hamilton </h1>
    </div>
    <v-btn icon>
      <v-icon @click="emitMenuClicked">
        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><title>menu</title><path d="M3,6H21V8H3V6M3,11H21V13H3V11M3,16H21V18H3V16Z" /></svg>
      </v-icon>
    </v-btn>
  </div>
  
</template>

<script>

export default {
  name: 'HeaderApp',
  methods: {
    emitMenuClicked() {
      this.$root.$emit('menuClicked');
    },
  }
}

</script>

<style scoped>


.container {
  height: 10vh;
  width: 100%;
  top: 0;
  left: 0;
  display: flex;
  background-color: beige;
  align-items: center;
  text-align: center;
}

.logo {
  width: 100vw;
  display: flex;
  align-items: center;
  justify-content: center;
  text-align: center;
  z-index: 0;
}


h1 {
  font-size: 40px;
  font-weight: bold;
  color: black;

}

.v-btn {
  top: 50;
  right:0;
  margin-left: auto;
  margin-right: 20px;
  color: black;
  z-index: 2;
}
 

</style>