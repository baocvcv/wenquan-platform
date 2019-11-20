import { mount, createLocalVue } from "@vue/test-utils";
import Test from "@/views/Test.vue";
import Vue from "vue";
import Vuetify from "vuetify";
import Vuex from "vuex";
import Router from "vue-router";
import RouterRule from "@/router";
import "./mock/Test.js";

const localVue = createLocalVue();
Vue.use(Vuetify);
Vue.use(Router);

describe("Test.vue", () => {
  let vuetify, router;
  beforeEach(() => {
    vuetify = new Vuetify();
    router = new Router({ RouterRule });
  });

  it("travel", async done => {
    const store = new Vuex.Store({
      state: {
        user: {
          id: 123
        }
      }
    });
    const wrapper = mount(Test, {
      localVue,
      vuetify,
      router,
      store,
      sync: false,
    });
    await setTimeout(() => {},500);
    wrapper.vm.submit({});
    await setTimeout(() => {},500);
    wrapper.vm.submit({});
    setTimeout(() => {
      done();
    },500);
  });

});
