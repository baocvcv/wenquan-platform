import { mount, createLocalVue } from "@vue/test-utils";
import QuestionBanks from "@/views/admin/QuestionBanks.vue";
import Vue from "vue";
import Vuetify from "vuetify";
import Vuex from "vuex";
import "./mock/QuestionBanksMock.js";
import VueProgressBar from "vue-progressbar";
const localVue = createLocalVue();
Vue.use(Vuetify);
Vue.use(Vuex);
Vue.use(VueProgressBar, {});

describe("QuestionBanks", () => {
  let vuetify;
  beforeEach(() => {
    vuetify = new Vuetify();
  });
  it("Render correctly", async done => {
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
    const wrapper = mount(QuestionBanks, {
      vuetify,
      localVue,
      store,
      sync: false
    });
    setTimeout(() => {
      expect(wrapper.exists("test1")).toBe(true);
      expect(wrapper.exists("test2")).toBe(true);
      done();
    }, 1000);
  });
  it("Render failed", async done => {
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
    const wrapper = mount(QuestionBanks, {
      vuetify,
      localVue,
      store,
      sync: false
    });
    setTimeout(() => {
      expect(wrapper.exists("Failed")).toBe(true);
      done();
    }, 1000);
  });
});
