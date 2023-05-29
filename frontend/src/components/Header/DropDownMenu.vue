<template>
    <v-app>
      <v-app-bar app>
        <v-toolbar-title>Formula Hamilton</v-toolbar-title>
        <v-spacer></v-spacer>
        <v-menu offset-y>
          <template v-slot:activator="{ on }">
            <v-btn icon v-on="on">
              <v-icon>mdi-menu</v-icon>
            </v-btn>
          </template>
          <v-list>
            <v-list-item v-for="item in dropdownItems" :key="item.title" @click="redirectToPage(item.route)">
              <v-list-item-title>{{ item.title }}</v-list-item-title>
            </v-list-item>
          </v-list>
        </v-menu>
      </v-app-bar>
  
      <v-main>
        <!-- Content of your pages -->
      </v-main>
    </v-app>
</template>
  
<script>
  export default {
    data() {
      return {
        dropdownItems: [
          { title: 'Page 1', route: '/page1' },
          { title: 'Page 2', route: '/page2' },
          { title: 'Page 3', route: '/page3' },
        ],
      };
    },
    methods: {
      redirectToPage(route) {
        this.$router.push(route);
      },
    },
  };
  </script>
  