import { mount, createLocalVue } from "@vue/test-utils";
import QuestionBanksList from "@/components/QuestionBanksList.vue";
import Vue from "vue";
import Vuetify from "vuetify";
import "./mock/QuestionBanksListMock.js";
import Router from "vue-router";
import RouterRule from "@/router";
const localVue = createLocalVue();
Vue.use(Vuetify);
Vue.use(Router);

describe("SignUp.vue", () => {
  let vuetify, router;
  beforeEach(() => {
    vuetify = new Vuetify();
    router = new Router({ RouterRule });
  });
  it("render correctly", async done => {
    const wrapper = mount(QuestionBanksList, {
      vuetify,
      localVue,
      router,
      sync: false,
      attachToDocument: true
    });
    wrapper.element.setAttribute("data-app", true);
    const question_bank = {
      id: 1,
      name: "test",
      brief: "brief",
      icon: "mdi-eye",
      details: {
        question_number: 200
      }
    };
    wrapper.setProps({
      question_banks: [question_bank]
    });
    wrapper.setData({
      cur_qst_bank: question_bank
    });
    await wrapper.vm.$nextTick();
    expect(wrapper.exists("test")).toBe(true);
    expect(wrapper.exists("brief")).toBe(true);
    wrapper.vm.detail = true;
    await wrapper.vm.$nextTick();
    expect(wrapper.exists("Goto")).toBe(true);
    expect(wrapper.exists("Back")).toBe(true);
    expect(wrapper.exists("question_number: 200")).toBe(true);
    wrapper.vm.detail = false;
    wrapper.vm.show_del_dialog = true;
    await wrapper.vm.$nextTick();
    expect(wrapper.exists("Confirm")).toBe(true);
    expect(wrapper.exists("Cancel")).toBe(true);
    wrapper.vm.show_del_dialog = false;
    await wrapper.vm.$nextTick();
    wrapper.vm.select_action();
    await wrapper.vm.$nextTick();
    expect(wrapper.emitted()["done-select"]).toBeTruthy();
    done();
  });

  it("Delete question bank successfully", async done => {
    const wrapper = mount(QuestionBanksList, {
      vuetify,
      localVue,
      sync: false,
      attachToDocument: true
    });
    wrapper.element.setAttribute("data-app", true);
    const question_bank = {
      id: 1,
      name: "test",
      brief: "brief",
      icon: "mdi-eye",
      details: {
        question_number: 200
      }
    };
    wrapper.setProps({
      question_banks: [question_bank]
    });
    wrapper.setData({
      cur_qst_bank: question_bank
    });
    wrapper.vm.show_del_dialog = true;
    await wrapper.vm.$nextTick();
    wrapper.vm.delete_qst_bank();
    setTimeout(() => {
      done();
    }, 1000);
  });
  it("Fail to delete question bank", async done => {
    window.alert = jest.fn();
    const wrapper = mount(QuestionBanksList, {
      vuetify,
      localVue,
      sync: false,
      attachToDocument: true
    });
    wrapper.element.setAttribute("data-app", true);
    const question_bank = {
      id: 2,
      name: "Error",
      brief: "brief",
      icon: "mdi-eye",
      details: {
        question_number: 200
      }
    };
    wrapper.setProps({
      question_banks: [question_bank]
    });
    wrapper.setData({
      cur_qst_bank: question_bank
    });
    wrapper.vm.show_del_dialog = true;
    await wrapper.vm.$nextTick();
    wrapper.vm.delete_qst_bank();
    setTimeout(() => {
      done();
    }, 1000);
  });
});
