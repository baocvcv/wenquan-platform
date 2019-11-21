import { mount, createLocalVue } from "@vue/test-utils";
import QuestionCorrect from "@/components/QuestionCorrect.vue";
import Vue from "vue";
import Vuex from "vuex";
import Vuetify from "vuetify";
import "./mock/QuestionCorrect.js";

const localVue = createLocalVue();
Vue.use(Vuex);
Vue.use(Vuetify);

describe("QuestionCorrect.vue", () => {
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
    const wrapper = mount(QuestionCorrect, {
      localVue,
      vuetify,
      router,
      store,
      sync: false,
    });
    setTimeout(() => {
      done();
    },500);
  });
  it("travel through all funcs", done => {
    const wrapper = mount(QuestionCorrect, {
      localVue,
      vuetify,
      router,
      store,
      sync: false,
      propsData: {
        question: {
          paper_record_id: 1,
          question_record_id: 1,
          paper_id: -1,
          section_id: -1,
          question_id: -1,
          question_point: 20,
          point_every_blank: [1, 2, 3]
        }
      }
    });
    wrapper.vm.save();
    wrapper.vm.save();
    wrapper.vm.check_ans(0,{});
    wrapper.vm.check_ans(0,{
      question_type: "fill_blank"
    });
    setTimeout(() => {
      done();
    },500);
  });
  it("travel through all funcs", done => {
    const wrapper = mount(QuestionCorrect, {
      localVue,
      vuetify,
      router,
      store,
      sync: false,
      propsData: {
        question: {
          paper_record_id: -1,
          question_record_id: 1,
          paper_id: -1,
          section_id: -1,
          question_id: -1,
          question_point: 20,
          point_every_blank: [1, 2, 3]
        }
      }
    });
    setTimeout(() => {
      done();
    },500);
  });
});
