import { mount, createLocalVue } from "@vue/test-utils";
import CreateAuthCodeCard from "@/components/CreateAuthCodeCard.vue";
import Vue from "vue";
import Vuetify from "vuetify";
import Vuex from "vuex";
import Router from "vue-router";
import RouterRule from "@/router";
import "./mock/CreateAuthCodeCard.js";

const localVue = createLocalVue();
Vue.use(Vuetify);
Vue.use(Router);
Vue.use(Vuex);

describe("CreateAuthCodeCard.vue", () => {
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
        updateUser(state, payload) {
        },
        updateUserWithKey(state, payload) {
        }
      },
    })
    const wrapper = mount(CreateAuthCodeCard, {
      localVue,
      vuetify,
      router,
      store,
      sync: false,
    });
    wrapper.vm.submit();
    setTimeout(() => {
      done();
    },500);
  });

});
