<template>
  <div app class="container">
    <div class="logo">
      <h1> Formula Hamilton </h1>
    </div>
    <div class="navbarContainer">
      <navbar class="navbar">
        <li>
          <a href="/"><b>Home</b></a>
        </li>
        <li>
          <a href="/about"><b>About</b></a>
        </li>
        <li>
          <a href="/projects"><b>Projects</b></a>
        </li>
      </navbar>
    </div>
  </div>
  
</template>

<script>

export default {
  name: 'HeaderApp'
}

</script>

<style scoped>

.container {
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
  min-height: 10vh;
  display: flex;
  position: absolute;
  left: 2%;
  justify-content: center;
  align-items: center;
}

.navbarContainer {
  height: 10vh;
  min-height: 10vh;
  width: 100vw;
  display: flex;
  justify-content: flex-end;
  align-items: center;
}

.navbar {

  display: flex;
  justify-content: space-around;
  align-items: center;
  height: 10vh;
  width: 30vw;
  margin-right: 10px;
  min-height: 10vh;

}

.navbar li {
  list-style: none; 
  height: 60%;
  width: 30%;
  display: flex;
  justify-content: center;
  align-items: center;
  border-radius: 10%;
}


.navbar li a {
  text-decoration: none; /* Remove the default link underline */
  color: black; /* Set the color of the navbar links */
  font-size: 1.2em;
}


.navbar li:hover {
  background-color: rgb(157, 141, 94); /* Set the background color for hover effect */
  transition-delay: 0.12s; 
}



</style>