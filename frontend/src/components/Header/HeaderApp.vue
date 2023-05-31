<template>
  <div app class="containerHeader" :class="{ 'dark-mode-header': isDarkMode, 'light-mode-header': !isDarkMode }">
    <div class="logo">
      <img class="logo-image" :src="logoSrc" alt="logo" @click="redirectToHome">
    </div>
    <div class="navbarContainer">
      <navbar class="navbar">
        <li @click="redirectToHome">
          <a href="#" :class="{ 'textNavBar_Dark': isDarkMode, 'textNavBar': !isDarkMode }"><b>Home</b></a>
        </li>
        <li @click="redirectToGraphGenerator">
          <a href="#" :class="{ 'textNavBar_Dark': isDarkMode, 'textNavBar': !isDarkMode }"><b>Graph Generator</b></a>
        </li>
        <!-- <li @click="redirectToAbout">
          <a href="#" :class="{ 'textNavBar_Dark': isDarkMode, 'textNavBar': !isDarkMode }"><b>About</b></a>
        </li> -->
      </navbar>
    </div>
  </div>
</template>

<script>

import EventBus from '../../js/event-bus.js';

export default {
  name: 'HeaderApp',
  computed: {
    isDarkMode() {
      return EventBus.isDarkMode.value;
    },
    logoSrc() {
      return this.isDarkMode
        ? require('@/assets/VettorialeLogoWhite.png')
        : require('@/assets/VettorialeLogo.png')
    },
  },
  methods: {
    redirectToHome() {
      this.$router.push('/');
    },
    redirectToAbout() {
      // Redirect to the 'about' route
      this.$router.push('/about');
    },
    redirectToGraphGenerator() {
      // Redirect to the 'about' route
      this.$router.push('/graphGenerator');
    }
  }
};

</script>

<style scoped>
.containerHeader {
  height: 10vh;
  min-height: 10vh;
  width: 100vw;
  min-width: 100vw;
  display: flex;
  flex-direction: row;
  justify-content: flex-end;
  align-items: center;
  background-color: beige;
}

.logo {
  height: 10vh;
  width: 30vw;
  max-width: 30vw;
  min-height: 10vh;
  display: flex;
  position: absolute;
  left: 2%;
  justify-content: center;
  align-items: center;
}

b {
  font-weight: bold;
}

.logo-image {
  max-width: 100%;
  max-height: 100%;
  object-fit: contain;
}

.navbarContainer {
  height: 10vh;
  min-height: 10vh;
  width: 100vw;
  display: flex;
  justify-content: flex-end;
  align-items: center;
}



.light-mode-header {

background-color: beige;

}

.dark-mode-header {

background-color: #3a332a;

}


.navbar li a {
  text-decoration: none;
  font-size: 1.2em;
  list-style: none;
}


.navbar li:hover {
  background-color: rgb(157, 141, 94);
  transition-delay: 0.12s;
  list-style: none;
}



.textNavBar_Dark {
  color: beige;
}


.textNavBar {
  color: black;
  font-weight: bold;
}


.navbar {
  
  display: flex;
  justify-content: space-around;
  align-items: center;
  height: 10vh;
  width: 40vw;
  text-align: center;
  margin-right: 10px;
  min-height: 10vh;

}

.navbar li {
  list-style: none;
  height: 60%;
  width: 30%;
  display: flex;
  text-align: center;
  justify-content: center;
  align-items: center;
  border-radius: 10%;
}


</style>