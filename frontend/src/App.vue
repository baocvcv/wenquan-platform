<template>
  <v-app id="app">
    <app-bar :key="$route.fullPath"></app-bar>
    <v-content>
      <v-container fluid>
        <router-view />
      </v-container>
    </v-content>
    <notifications
      :duration="5000"
      :width="500"
      animation-name="v-fade-left"
      position="top right"
    >
      <template slot="body" slot-scope="props">
        <div
          :class="get_class(props)"
          @click="props.close"
        >
          <div
            v-if="props.item.title"
            class="notification-title"
            v-html="props.item.title"
          >
          </div>
          <div
            class="notification-content"
            v-html="props.item.text"
          >
          </div>
        </div>
      </template>
    </notifications>
  </v-app>
</template>

<script>
import app_bar from "./components/AppBar.vue";

export default {
  name: "App",
  components: {
    "app-bar": app_bar
  },
  data: () => ({
    //
  }),
  methods: {
    get_class(props) {
      let style = "vue-notification-template vue-notification";
      if (props.item.type) {
        if (props.item.type === "error") {
          style += " fail";
        } else if (props.item.type === "success") {
          style += " succeed";
        } else if (props.item.type === "warn") {
          style += " warning";
        }
      }
      return style;
    }
  }
};
</script>

<style lang="scss">
#app {
  font-family: "Avenir", Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #2c3e50;
}
/*
  EXAMPLES
*/
.vue-notification {
  display: block;
  box-sizing: border-box;  
  text-align: left;
  font-size: 12px;
  padding: 10px;
  margin: 0 5px 5px;

  color: white;
  background: #44A4FC;
  border-left: 5px solid #187FE7;
}

.vue-notification.warning {
  background: #ffb648;
  border-left-color: #f48a06;
}

.vue-notification.fail {
  background: #E54D42;
  border-left-color: #B82E24;
}

.vue-notification.succeed {
  background: #68CD86;
  border-left-color: #42A85F;
}

.v-fade-left-enter-active,
.v-fade-left-leave-active,
.v-fade-left-move {
  transition: all 1s;
}
.v-fade-left-enter,
.v-fade-left-leave-to {
  opacity: 0;
  transform: translateX(-500px) scale(0.2);
}
</style>
