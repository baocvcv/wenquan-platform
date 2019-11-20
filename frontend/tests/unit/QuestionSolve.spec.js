import { mount, createLocalVue } from "@vue/test-utils";
import QuestionSolve from "@/components/QuestionSolve.vue";
import Vue from "vue";
import Vuetify from "vuetify";
import Router from "vue-router";
import RouterRule from "@/router";
import "./mock/CreateAuthCodeCard.js";

const localVue = createLocalVue();
Vue.use(Vuetify);
Vue.use(Router);

describe("QuestionSolve.vue", () => {
  let vuetify, router;
  beforeEach(() => {
    vuetify = new Vuetify();
    router = new Router({ RouterRule });
  });

  it("travel", done => {
    const wrapper = mount(QuestionSolve, {
      localVue,
      vuetify,
      router,
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
