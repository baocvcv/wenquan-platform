import { mount } from "@vue/test-utils";
import SignUpBox from "@/components/SignUpBox.vue";
import SignUp from "@/views/SignUp.vue";

describe("SignUp.vue", () => {
  it("renders correctly", () => {
    const wrapper = mount(SignUp);
    expect(wrapper.contains("v-form")).toBe(true);
    expect(wrapper.contains("v-card")).toBe(true);
  });
});

describe("SignUpBox.vue", () => {
  it("correct input", () => {
    const wrapper = mount(SignUpBox);
    wrapper.setData({
      user_name: "test",
      password: "11111111",
      re_pswd: "11111111",
      email: "kxz@qq.com",
      accept_terms: "true"
    });
    expect(wrapper.vm.show_dialog).toBe(false);
    wrapper.vm.$nextTick(() => {
      expect(wrapper.vm.valid).toBe(true);
      done();
    });
  });

  it("Incorrect input", () => {
    const wrapper = mount(SignUpBox);
    wrapper.setData({
      user_name: "test",
      password: "11111111",
      re_pswd: "11111111",
      email: "kxz@qq.com",
      accept_terms: "true"
    });
    //user_name exceed limits
    wrapper.vm.user_name = "12345678901";
    wrapper.vm.$nextTick(() => {
      expect(wrapper.vm.valid).toBe(false);
      done();
    });
    wrapper.vm.user_name = "test";
    //re_password is not consistent with former
    wrapper.vm.re_pswd = "1";
    wrapper.vm.$nextTick(() => {
      expect(wrapper.vm.valid).toBe(false);
      done();
    });
    wrapper.vm.re_pswd = "11111111";
    //wrong email
    wrapper.vm.email = "wrongEmail";
    wrapper.vm.$nextTick(() => {
      expect(wrapper.vm.valid).toBe(false);
      done();
    });
    wrapper.vm.email = "kxz@qq.com";
  });
});
