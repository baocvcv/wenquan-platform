import { mount, createLocalVue } from "@vue/test-utils";
import PaperMarking from "@/components/PaperMarking.vue";
import Vue from "vue";
import Vuetify from "vuetify";
import Vuex from "vuex";
import Router from "vue-router";
import RouterRule from "@/router";
import "./mock/PaperMarking.js";

const localVue = createLocalVue();
Vue.use(Vuetify);
Vue.use(Router);

describe("PaperMarking.vue", () => {
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
    const wrapper = mount(PaperMarking, {
      localVue,
      vuetify,
      router,
      store,
      sync: false,
      propsData: {
        record: {
          questions: {
            "1": {

            }
          }
        }
      }
    });
    wrapper.vm.question_info({},{
      id: "1",
      content: {

      }
    });
    wrapper.vm.question_info({},{
      id: "1",
      point_every_blank: [1],
      content: {
        question_blank_num: 2
      }
    });
    wrapper.vm.question_ref(0,0);
    wrapper.vm.question_ref(0,0);
    setTimeout(() => {
      done();
    }, 500);
  });
  it("travel", async done => {
    const store = new Vuex.Store({
      state: {
        user: {
          id: 123
        }
      }
    });
    const wrapper = mount(PaperMarking, {
      localVue,
      vuetify,
      router,
      store,
      sync: false,
    });
    setTimeout(() => {
      done();
    }, 500);
  });
  it("travel", async done => {
    const store = new Vuex.Store({
      state: {
        user: {
          id: 123
        }
      }
    });
    const wrapper = mount(PaperMarking, {
      localVue,
      vuetify,
      router,
      store,
      sync: false,
      propsData: {
        paper_record_id: 1
      }
    });
    setTimeout(() => {
      done();
    }, 500);
  });
  it("travel", async done => {
    const store = new Vuex.Store({
      state: {
        user: {
          id: 123
        }
      }
    });
    const wrapper = mount(PaperMarking, {
      localVue,
      vuetify,
      router,
      store,
      sync: false,
      propsData: {
        paper_record_id: 1
      }
    });
    setTimeout(() => {
      done();
    }, 500);
  });
});
