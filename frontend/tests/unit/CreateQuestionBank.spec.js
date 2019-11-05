import { mount, createLocalVue } from "@vue/test-utils";
import CreateQuestionBank from "@/components/CreateQuestionBank";
import Vue from "vue";
import Vuetify from "vuetify";
import Router from "vue-router";
import RouterRule from "@/router";
import "./mock/CreateQuestionBankMock.js";
const localVue = createLocalVue();
Vue.use(Vuetify);
Vue.use(Router);

describe("CreateQuestionBank.vue", () => {
  let vuetify, router;
  beforeEach(() => {
    vuetify = new Vuetify();
    router = new Router({ RouterRule });
  });
  it("create public question bank successfully", async done => {
    window.alert = jest.fn();
    const wrapper = mount(CreateQuestionBank, {
      vuetify,
      localVue,
      router,
      sync: false
    });
    wrapper.setData({
      name: "test",
      brief: "brief",
      authority: "public",
      image: [""]
    });
    sessionStorage.setItem("user", '{ "user_group": "admin" }');
    await wrapper.vm.$nextTick();
    wrapper.vm.$refs.form.validate();
    await wrapper.vm.$nextTick();
    expect(wrapper.vm.valid).toBe(true);
    const submit_btn = wrapper.findAll("button").at(1);
    submit_btn.trigger("click");
    setTimeout(() => {
      expect(wrapper.vm.$route.path).toBe("/questionbanks/1");
      done();
    }, 1000);
  });
  it("create private question bank successfully", async done => {
    window.alert = jest.fn();
    const wrapper = mount(CreateQuestionBank, {
      vuetify,
      localVue,
      router,
      sync: false
    });
    wrapper.setData({
      name: "test",
      brief: "brief",
      authority: "private",
      invitation_code_count: "not a number",
      image: [""]
    });
    wrapper.vm.$router.push("/");
    await wrapper.vm.$nextTick();
    wrapper.vm.$refs.form.validate();
    await wrapper.vm.$nextTick();
    expect(wrapper.vm.valid).toBe(false);
    wrapper.vm.invitation_code_count = 100;
    await wrapper.vm.$nextTick();
    wrapper.vm.$refs.form.validate();
    await wrapper.vm.$nextTick();
    expect(wrapper.vm.valid).toBe(true);
    const submit_btn = wrapper.findAll("button").at(1);
    submit_btn.trigger("click");
    setTimeout(() => {
      expect(wrapper.vm.$route.path).toBe("/questionbanks/1");
      done();
    }, 1000);
  });
  it("Reset button", async () => {
    window.alert = jest.fn();
    const wrapper = mount(CreateQuestionBank, {
      vuetify,
      localVue,
      sync: false
    });
    wrapper.setData({
      name: "test",
      brief: "brief",
      authority: "public",
      image: [""]
    });
    await wrapper.vm.$nextTick();
    const reset_btn = wrapper.findAll("button").at(2);
    reset_btn.trigger("click");
    await wrapper.vm.$nextTick();
    expect(!wrapper.vm.name).toBe(true);
    expect(!wrapper.vm.brief).toBe(true);
    expect(!wrapper.vm.authority).toBe(true);
    expect(wrapper.vm.image.length).toBe(0);
  });
  it("Failed", async done => {
    window.alert = jest.fn();
    const wrapper = mount(CreateQuestionBank, {
      vuetify,
      localVue,
      router,
      sync: false
    });
    wrapper.setData({
      name: "Error",
      brief: "brief",
      authority: "public",
      image: [""]
    });
    const cur_route = wrapper.vm.$route.path;
    await wrapper.vm.$nextTick();
    const submit_btn = wrapper.findAll("button").at(1);
    submit_btn.trigger("click");
    setTimeout(() => {
      expect(wrapper.vm.$route.path).toBe(cur_route);
      done();
    }, 1000);
  });
});
