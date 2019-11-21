import { mount, createLocalVue } from "@vue/test-utils";
import ActivationCard from "@/components/ActivationCard.vue";
import Vue from "vue";
import Vuex from "vuex";
import Vuetify from "vuetify";
import Router from "vue-router";
import RouterRule from "@/router";
import "./mock/ActivationCard.js";

const localVue = createLocalVue();
Vue.use(Vuetify);
Vue.use(Router);

describe("ActivationCard.vue", () => {
  let vuetify, router;
  beforeEach(() => {
    vuetify = new Vuetify();
    router = new Router({ RouterRule });
  });

  it("travel", done => {
    const store = new Vuex.Store({
      state: {
        user: {
          id: 123
        }
      },
      mutations: {
        updateUser(state, payload) {},
        updateUserWithKey(state, payload) {}
      }
    });
    const wrapper = mount(ActivationCard, {
      localVue,
      vuetify,
      router,
      store,
      sync: false
    });
    wrapper.vm.reset();
    wrapper.vm.code = "123";
    wrapper.vm.activate();
    setTimeout(() => {
      done();
    }, 500);
  });

  it("travel", done => {
    const store = new Vuex.Store({
      state: {
        user: {
          id: 123
        }
      },
      mutations: {
        updateUser(state, payload) {},
        updateUserWithKey(state, payload) {}
      }
    });
    const wrapper = mount(ActivationCard, {
      localVue,
      vuetify,
      router,
      store,
      sync: false
    });
    wrapper.vm.code = "234";
    wrapper.vm.activate();
    setTimeout(() => {
      done();
    }, 500);
  });

  it("travel", done => {
    const store = new Vuex.Store({
      state: {
        user: {
          id: 123
        }
      },
      mutations: {
        updateUser(state, payload) {},
        updateUserWithKey(state, payload) {}
      }
    });
    const wrapper = mount(ActivationCard, {
      localVue,
      vuetify,
      router,
      store,
      sync: false
    });
    wrapper.vm.code = "345";
    wrapper.vm.activate();
    setTimeout(() => {
      done();
    }, 500);
  });
});
