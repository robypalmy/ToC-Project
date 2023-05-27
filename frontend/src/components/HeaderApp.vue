<template>
  <header>
    <div class="ciao">
      <h1> Formula Hamilton </h1>
    </div>
    <v-btn icon>
      <v-icon @click="toggleMenu">
        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><title>menu</title><path d="M3,6H21V8H3V6M3,11H21V13H3V11M3,16H21V18H3V16Z" /></svg>
      </v-icon>
    </v-btn>
  </header>
</template>

<script>

export default {
  name: 'HeaderApp',
  methods: {
    toggleMenu() {
      // Handle menu toggle logic here
    },
  }
}

</script>

<style scoped>



header {
  height: 100%;
  width: 100%;
  display: flex;
  background-color: beige;
  align-items: center;
  justify-content: center;
  text-align: center;
}

.ciao {
  height: 100%;
  width: 100%;
  display: flex;
  align-items: center;
  justify-content: center;
  text-align: center;
}


h1 {
  font-size: 40px;
  font-weight: bold;
  color: black;

}

.v-btn {
  margin-right: 20px;
  color: black;
}
 

</style>