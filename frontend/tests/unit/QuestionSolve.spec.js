import { mount, createLocalVue } from "@vue/test-utils";
import QuestionSolve from "@/components/QuestionSolve.vue";
import Vue from "vue";
import Vuex from "vuex";
import Vuetify from "vuetify";
import Router from "vue-router";
import RouterRule from "@/router";
import "./mock/CreateAuthCodeCard.js";

const localVue = createLocalVue();
Vue.use(Vuetify);
Vue.use(Router);
Vue.use(Vuex);

describe("QuestionSolve.vue", () => {
  let vuetify, router, store;
  beforeEach(() => {
    vuetify = new Vuetify();
    router = new Router({ RouterRule });
    store = new Vuex.Store({
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
  });

  it("travel", done => {
    const wrapper = mount(QuestionSolve, {
      localVue,
      vuetify,
      router,
      store,
      sync: false,
      props: {
        answer: []
      }
    });
    wrapper.setProps({
      answer: [123]
    });
    wrapper.vm.$nextTick(() => done());
  });
});
