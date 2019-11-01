import { mount, createLocalVue } from "@vue/test-utils";
import QuestionListItem from "@/components/QuestionListItem.vue";
import Vue from "vue";
import Vuex from "vuex";
import Vuetify from "vuetify";
import Router from "vue-router";
import RouterRule from "@/router";
import QuestionFactory from "./utils/QuestionFactory.js";

const localVue = createLocalVue();
Vue.use(Vuex);
Vue.use(Vuetify);
Vue.use(Router);

const resizeWindow = (x, y) => {
  window.innerWidth = x;
  window.innerHeight = y;
  window.dispatchEvent(new Event("resize"));
};

const question_factory = new QuestionFactory();

describe("QuestionListItem.vue", () => {
  let vuetify, router;

  beforeEach(() => {
    vuetify = new Vuetify();
    router = new Router({ RouterRule });
  });

  it("read_more and collapse feature work properly", async () => {
    let wrapper = mount(QuestionListItem, {
      localVue,
      vuetify,
      router,
      sync: false,
      propsData: {
        question: question_factory.create_single_choice(1)
      }
    });
    expect(wrapper.vm.question.id).toBe(1);
    await wrapper.vm.$nextTick();
    wrapper.vm.read_more();
    expect(wrapper.vm.hide_content).toBe(false);
    wrapper.vm.collapse();
    expect(wrapper.vm.hide_content).toBe(true);
  });

  it("Views questions properly", async done => {
    let wrapper = mount(QuestionListItem, {
      localVue,
      vuetify,
      router,
      sync: false,
      propsData: {
        question: question_factory.create_brief_answer(1),
        dialog: true
      }
    });
    let view_button = wrapper.find(".mdi-arrow-right");
    expect(view_button.exists()).toBe(true);
    view_button.trigger("click");
    await wrapper.vm.$nextTick();
    expect(wrapper.vm.viewing_question).toBe(true);
    wrapper.setData({
      viewing_question: false
    });
    wrapper.setProps({
      dialog: false
    });
    await wrapper.vm.$nextTick();
    setTimeout(() => {
      expect(wrapper.vm.$route.path).toBe("/questions/1");
      done();
    }, 1000);
  });
});
