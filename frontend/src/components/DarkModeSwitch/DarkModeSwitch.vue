<template>
  <button class="dark-mode-switch" @click="toggleDarkMode">
    <img :src="buttonImage" alt="Switch mode">
  </button>
</template>

<script>

import EventBus from '../../js/event-bus.js';

export default {
  name: 'DarkModeSwitch',
  computed: {
    buttonImage() {
      return EventBus.isDarkMode.value ? require('@/assets/moon.png') : require('@/assets/sun.png');
    },
  },
  methods: {
    toggleDarkMode() {
      EventBus.isDarkMode.value = !EventBus.isDarkMode.value;
      localStorage.setItem('isDarkMode', EventBus.isDarkMode.value);
    },
  },
};
</script>

<style scoped>
.dark-mode-switch {
  position: fixed;
  height: 7%;
  width: 7%;
  bottom: 2vh;
  left: 0;
}

.dark-mode-switch img {
  height: 100%;
  width: 100%;
  object-fit: contain;
}
</style>
