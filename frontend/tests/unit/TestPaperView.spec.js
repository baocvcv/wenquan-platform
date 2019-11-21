import { mount, createLocalVue } from "@vue/test-utils";
import TestPaperView from "@/views/admin/TestPaperView.vue";
import Vue from "vue";
import Vuex from "vuex";
import Vuetify from "vuetify";
import "./mock/TestPaperView.js";

const localVue = createLocalVue();
Vue.use(Vuex);
Vue.use(Vuetify);

describe("TestPaperView.vue", () => {
  let vuetify, router, store;

  beforeEach(() => {
    vuetify = new Vuetify();
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

  it("travel through all funcs", done => {
    const wrapper = mount(TestPaperView, {
      localVue,
      vuetify,
      router,
      store,
      sync: false,
      mocks: {
        $route: {
          params: {
            id: 1
          }
        }
      }
    });
    setTimeout(() => {
      done();
    },500);
  });
});
