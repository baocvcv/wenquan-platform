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
                   position="top left"
                   >

       <template slot="body" slot-scope="props">
        <div :class="get_class(props)" @click="props.close">
          <div class="custom-template-content">
            <div class="custom-template-title">
              {{props.item.title}}
            </div>
            <div class="custom-template-text"
                 v-html="props.item.text"></div>
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
      let style = "custom-template";
      if (props.item.type) {
        if (props.item.type === 'error') {
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
.custom-template {
  display: flex;
  flex-direction: row;
  flex-wrap: nowrap;
  text-align: left;
  font-size: 13px;
  color: white;
  margin: 5px;
  margin-bottom: 0;
  align-items: center;
  justify-content: center;
  &, & > div {
    box-sizing: border-box;
  }
  background: rgb(157, 206, 252);
  border: 2px solid rgb(75, 151, 226);
  .custom-template-icon {
    flex: 0 1 auto;
    color: #15C371;
    font-size: 32px;
    padding: 0 10px;
  }
  .custom-template-close {
    flex: 0 1 auto;
    padding: 0 20px;
    font-size: 16px;
    opacity: 0.2;
    cursor: pointer;
    &:hover {
      opacity: 0.8;
    }
  }
  .custom-template-content {
    padding: 10px;
    flex: 1 0 auto;
    .custom-template-title {
      letter-spacing: 1px;
      text-transform: uppercase;
      font-size: 10px;
      font-weight: 600;
    }
  }
}
.custom-template.warning {
    background: #ffb648;
  border: 2px solid #f48a06 !important;
}

.custom-template.fail {
    background: rgb(231, 140, 134);
  border: 2px solid rgb(192, 99, 92) !important;
}

.custom-template.succeed {
    background: rgb(138, 202, 157);
  border: 2px solid rgb(89, 175, 113) !important;
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