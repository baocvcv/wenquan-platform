import Vue from "vue";
import "./plugins/axios";
import App from "./App.vue";
import router from "./router";
import store from "./store";
import "./registerServiceWorker";
import vuetify from "./plugins/vuetify";
import VueProgressBar from "vue-progressbar";
import Notifications from "vue-notification";

Vue.use(Notifications);

Vue.config.productionTip = false;

const options = {
  color: "#1976D2",
  failedColor: "#FF5252",
  thickness: "3px",
  transition: {
    speed: "0.2s",
    opacity: "0.6s",
    termination: 300
  },
  autoRevert: true,
  location: "top",
  inverse: false
};
Vue.use(VueProgressBar, options);

new Vue({
  router,
  store,
  vuetify,
  render: h => h(App)
}).$mount("#app");
