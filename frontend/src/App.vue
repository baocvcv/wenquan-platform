<template>
  <v-app id="app">
    <app-bar></app-bar>
    <router-view/>
  </v-app>
</template>

<script>
import app_bar from "./components/AppBar.vue";

export default {
  name: 'App',
  components: {
    "app-bar": app_bar
  },
  data: () => ({
    //
  }),
};
</script>

<style>
#app {
  font-family: "Avenir", Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
#nav {
  padding: 30px;
}

#app-bar a {
  font-weight: bold;
  color: #2c3e50;
}

#app-bar a.router-link-exact-active {
  color: #42b983;
}
</style>
