import { mount, createLocalVue } from "@vue/test-utils";
import SignUpBox from "@/components/SignUpBox.vue";
import SignUp from "@/views/SignUp.vue";
import Vue from "vue";
import Vuetify from "vuetify";

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
});
