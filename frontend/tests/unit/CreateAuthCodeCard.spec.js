import { mount, createLocalVue } from "@vue/test-utils";
import CreateAuthCodeCard from "@/components/CreateAuthCodeCard.vue";
import Vue from "vue";
import Vuetify from "vuetify";
import Router from "vue-router";
import RouterRule from "@/router";
import "./mock/CreateAuthCodeCard.js";

const localVue = createLocalVue();
Vue.use(Vuetify);
Vue.use(Router);

describe("CreateAuthCodeCard.vue", () => {
  let vuetify, router;
  beforeEach(() => {
    vuetify = new Vuetify();
    router = new Router({ RouterRule });
  });

  it("travel", done => {
    const wrapper = mount(CreateAuthCodeCard, {
      localVue,
      vuetify,
      router,
      sync: false,
    });
    wrapper.vm.submit();
    setTimeout(() => {
      done();
    },500);
  });

});
