import { mount, createLocalVue } from "@vue/test-utils";
import CreateQuestionBank from "@/components/CreateQuestionBank";
import Vue from "vue";
import Vuetify from "vuetify";
import Router from "vue-router";
import router from "@/router";
import "./mock/SignUpMock";
const localVue = createLocalVue();
Vue.use(Vuetify);
Vue.use(Router);

describe("CreateQuestionBank.vue", () => {
  let vuetify;
  beforeEach(() => {
    vuetify = new Vuetify();
  });
  it("create public success", async done => {
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
    await wrapper.vm.$nextTick();
    wrapper.vm.$refs.form.validate();
    await wrapper.vm.$nextTick();
    expect(wrapper.vm.valid).toBe(true);
    const submit_btn = wrapper.findAll("button").at(1);
    submit_btn.trigger("click");
    setTimeout(() => {
      expect(wrapper.vm.$route.path).not.toBe("/admin/questionbanks");
      done();
    }, 1000);
  });
});
