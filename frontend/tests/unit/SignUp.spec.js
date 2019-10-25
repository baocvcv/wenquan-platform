import { mount, createLocalVue } from "@vue/test-utils";
import SignUpBox from "@/components/SignUpBox.vue";
import SignUp from "@/views/SignUp.vue";
import Vue from "vue";
import Vuetify from "vuetify";
import "./mock/SignUpMock";
const localVue = createLocalVue();
Vue.use(Vuetify);

describe("SignUp.vue", () => {
  let vuetify;
  beforeEach(() => {
    vuetify = new Vuetify();
  });
  it("renders correctly", () => {
    const wrapper = mount(SignUp, {
      vuetify,
      localVue,
      sync: false
    });
    expect(wrapper.contains(".v-form")).toBe(true);
    expect(wrapper.contains(".v-card")).toBe(true);
  });
});

describe("SignUpBox.vue", () => {
  let vuetify;
  beforeEach(() => {
    vuetify = new Vuetify();
  });

  it("correct input", () => {
    const wrapper = mount(SignUpBox, {
      vuetify,
      localVue,
      sync: false
    });
    wrapper.setData({
      user_name: "test",
      password: "11111111",
      re_pswd: "11111111",
      email: "kxz@qq.com",
      accept_terms: true
    });
    expect(wrapper.vm.show_dialog).toBe(false);
    wrapper.vm.$nextTick(() => {
      expect(wrapper.vm.$refs.input.validate()).toBe(true);
    });
  });

  it("user name exceed 10 limits", () => {
    const wrapper = mount(SignUpBox, {
      vuetify,
      localVue,
      sync: false
    });
    wrapper.setData({
      user_name: "exceedlimit",
      password: "11111111",
      re_pswd: "11111111",
      email: "kxz@qq.com",
      accept_terms: true
    });
    wrapper.vm.$nextTick(() => {
      expect(wrapper.vm.$refs.input.validate()).toBe(false);
    });
  });

  it("re_password not consistent with former", () => {
    const wrapper = mount(SignUpBox, {
      vuetify,
      localVue,
      sync: false
    });
    wrapper.setData({
      user_name: "test",
      password: "11111111",
      re_pswd: "1",
      email: "kxz@qq.com",
      accept_terms: true
    });
    wrapper.vm.$nextTick(() => {
      expect(wrapper.vm.$refs.input.validate()).toBe(false);
    });
  });

  it("wrong email", () => {
    const wrapper = mount(SignUpBox, {
      vuetify,
      localVue,
      sync: false
    });
    wrapper.setData({
      user_name: "test",
      password: "11111111",
      re_pswd: "11111111",
      email: "wrongEmail",
      accept_terms: true
    });
    wrapper.vm.$nextTick(() => {
      expect(wrapper.vm.$refs.input.validate()).toBe(false);
    });
  });

  it("Not check contract", () => {
    const wrapper = mount(SignUpBox, {
      vuetify,
      localVue,
      sync: false
    });
    wrapper.setData({
      user_name: "test",
      password: "11111111",
      re_pswd: "11111111",
      email: "kxz@qq.com",
      accept_terms: false
    });
    wrapper.vm.$nextTick(() => {
      expect(wrapper.contains(".v-btn--disabled")).toBe(true);
    });
  });

  it("Reset btn", () => {
    const wrapper = mount(SignUpBox, {
      vuetify,
      localVue,
      sync: false
    });
    wrapper.setData({
      user_name: "test",
      password: "11111111",
      re_pswd: "11111111",
      email: "kxz@qq.com",
      accept_terms: false
    });
    wrapper.vm.$refs.input.validate();
    const reset_btn = wrapper.findAll("button").at(1);
    reset_btn.trigger("click");
    wrapper.vm.$nextTick(() => {
      expect(!!wrapper.vm.user_name).toBe(false);
    });
  });

  it("sign up success", async done => {
    const wrapper = mount(SignUpBox, {
      vuetify,
      localVue,
      sync: false,
      attachToDocument: true
    });
    wrapper.setData({
      user_name: "test",
      password: "11111111",
      re_pswd: "11111111",
      email: "kxz@qq.com",
      accept_terms: true
    });
	wrapper.element.setAttribute("data-app", true);
    await wrapper.vm.$nextTick();
    wrapper.vm.$refs.input.validate();
    await wrapper.vm.$nextTick();
    const signup_btn = wrapper.findAll(".v-btn").at(0);
    signup_btn.trigger("click");
    await wrapper.vm.$nextTick();
    setTimeout(() => {
      expect(wrapper.vm.sign_up_result).toBe("Success");
      done();
    }, 1000);
  });

  it("sign up failed", async done => {
    const wrapper = mount(SignUpBox, {
      vuetify,
      localVue,
      sync: false,
      attachToDocument: true
    });
    wrapper.setData({
      user_name: "fail",
      password: "11111111",
      re_pswd: "11111111",
      email: "kxz@qq.com",
      accept_terms: true
    });
	wrapper.element.setAttribute("data-app", true);
    await wrapper.vm.$nextTick();
    wrapper.vm.$refs.input.validate();
    await wrapper.vm.$nextTick();
    const signup_btn = wrapper.findAll(".v-btn").at(0);
    signup_btn.trigger("click");
    await wrapper.vm.$nextTick();
    setTimeout(() => {
      expect(wrapper.vm.sign_up_result).toBe("Error");
	  done();
    }, 1000);
  });
});
