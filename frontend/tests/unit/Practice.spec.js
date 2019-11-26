import { mount, createLocalVue } from "@vue/test-utils";
import Practice from "@/components/Practice.vue";
import Vue from "vue";
import Vuetify from "vuetify";
import Vuex from "vuex";
import Router from "vue-router";
import RouterRule from "@/router";
import Notifications from "vue-notification";
import VueProgressBar from "vue-progressbar";
import "./mock/PracticeMock.js";

const localVue = createLocalVue();
Vue.use(Vuetify);
Vue.use(Router);
Vue.use(Notifications);
Vue.use(VueProgressBar);

describe("Practice.vue", () => {
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
    const wrapper = mount(Practice, {
      localVue,
      vuetify,
      router,
      store,
      sync: false,
      attachToDocument: true
    });
    wrapper.vm.question_number = 2;
    wrapper.element.setAttribute("data-app", true);
    await setTimeout(() => {}, 500);
    wrapper.vm.done_select_bank(1);
    await setTimeout(() => {}, 500);
    wrapper.vm.start_practice();
    await setTimeout(() => {}, 500);
    wrapper.vm.question_number = 2;
    await setTimeout(() => {}, 500);
    wrapper.vm.done_select_bank(0);
    await setTimeout(() => {}, 500);
    wrapper.vm.start_practice();
    await setTimeout(() => {}, 500);
    wrapper.vm.done_select_bank(2);
    await setTimeout(() => {}, 500);
    wrapper.vm.start_practice();
    setTimeout(() => {
      done();
    }, 500);
  });
});
