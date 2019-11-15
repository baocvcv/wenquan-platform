import Vue from "vue";
import Vuex from "vuex";

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    user: null
  },
  mutations: {
    updateUser(state, payload) {
      state.user = payload.user;
      sessionStorage.setItem("user", JSON.stringify(payload.user));
    },
    updateUserWithKey(state, payload) {
      state.user[payload.key] = payload.value;
      sessionStorage.setItem("user", JSON.stringify(state.user));
    }
  },
  actions: {}
});
