import { mount, createLocalVue } from "@vue/test-utils";
import SignInBox from "@/components/SignInBox.vue";
import SignIn from "@/views/SignIn.vue";
import Vuetify from "vuetify";
import Notification from "vue-notification";
import Vuex from "vuex";
import Vue from "vue";
import Router from "vue-router";
import RouterRule from "@/router";
import "./mock/SignInMock.js";

const localVue = createLocalVue();
Vue.use(Vuetify);
Vue.use(Vuex);
Vue.use(Router);
Vue.use(Notification);

describe("SignInBox.vue", () => {
  let vuetify, router;
  beforeEach(() => {
    vuetify = new Vuetify();
    router = new Router({ RouterRule });
  });
  it("Correct Input", () => {
    const wrapper = mount(SignInBox, {
      localVue,
      vuetify,
      router,
      sync: false
    });
    wrapper.setData({
      username: "test",
      password: "test"
    });
    wrapper.vm.$nextTick(() => {
      expect(wrapper.contains(".v-btn--disabled")).toBe(false);
    });
  });
  it("Wrong Input", () => {
    const wrapper = mount(SignInBox, {
      localVue,
      vuetify,
      router,
      sync: false
    });
    wrapper.setData({
      username: "test",
      password: ""
    });
    wrapper.vm.$nextTick(() => {
      expect(wrapper.contains(".v-btn--disabled")).toBe(true);
    });
  });

  it("Try login correctly", async done => {
    const store = new Vuex.Store({
      state: {
        user: null
      },
      mutations: {
        updateUser(state, payload) {
          state.user = payload.user;
          sessionStorage.setItem("user", JSON.stringify(payload.user));
        }
      },
      actions: {}
    });
    const wrapper = mount(SignInBox, {
      localVue,
      vuetify,
      store,
      router,
      sync: false,
      attachToDocument: true
    });
    wrapper.setData({
      username: "testusr",
      password: "testpsw"
    });
    await wrapper.vm.$nextTick();
    wrapper.find("button").trigger("click");
    await wrapper.vm.$nextTick();
    setTimeout(() => {
      expect(wrapper.vm.sign_in_result).toBe("Success");
      sessionStorage.removeItem("user");
      done();
    }, 1000);
  });

  it("Try login with session", async done => {
    const store = new Vuex.Store({
      state: {
        user: null
      },
      mutations: {
        updateUser(state, payload) {
          state.user = payload.user;
          sessionStorage.setItem("user", JSON.stringify(payload.user));
        }
      },
      actions: {}
    });
    const wrapper = mount(SignInBox, {
      localVue,
      vuetify,
      store,
      router,
      sync: false,
      attachToDocument: true
    });
    sessionStorage.setItem(
      "user",
      JSON.stringify({
        username: "test",
        password: "test"
      })
    );
    await wrapper.vm.$nextTick();
    wrapper.vm.click();
    await wrapper.vm.$nextTick();
    setTimeout(() => {
      //expect(wrapper.vm.sign_in_result).toBe("");
      sessionStorage.removeItem("user");
      done();
    }, 1000);
  });

  it("Try login with banned", async done => {
    const store = new Vuex.Store({
      state: {
        user: null
      },
      mutations: {
        updateUser(state, payload) {
          state.user = payload.user;
          sessionStorage.setItem("user", JSON.stringify(payload.user));
        }
      },
      actions: {}
    });
    const wrapper = mount(SignInBox, {
      localVue,
      vuetify,
      store,
      router,
      sync: false,
      attachToDocument: true
    });
    wrapper.setData({
      username: "bannedusr",
      password: "bannedpsw"
    });
    await wrapper.vm.$nextTick();
    wrapper.find("button").trigger("click");
    await wrapper.vm.$nextTick();
    setTimeout(() => {
      //expect(wrapper.vm.sign_in_result).toBe("Error");
      //expect(wrapper.vm.sign_in_response).toBe(
      //  "You are banned! Please contact your administrator."
      //);
      sessionStorage.removeItem("user");
      done();
    }, 1000);
  });

  it("Try login wrongly", async done => {
    const store = new Vuex.Store({
      state: {
        user: null
      },
      mutations: {
        updateUser(state, payload) {
          state.user = payload.user;
          sessionStorage.setItem("user", JSON.stringify(payload.user));
        }
      },
      actions: {}
    });
    const wrapper = mount(SignInBox, {
      localVue,
      vuetify,
      store,
      router,
      sync: false,
      attachToDocument: true
    });
    wrapper.setData({
      username: "testusr",
      password: "wrongpsw"
    });
    await wrapper.vm.$nextTick();
    wrapper.find("button").trigger("click");
    await wrapper.vm.$nextTick();
    setTimeout(() => {
      //expect(wrapper.vm.sign_in_result).toBe("Error");
      done();
    }, 1000);
    wrapper.destroy();
  });
});

describe("SignIn.vue", () => {
  let vuetify, router;
  beforeEach(() => {
    vuetify = new Vuetify();
    router = new Router({ RouterRule });
  });
  it("Render Component Correctly", () => {
    const wrapper = mount(SignIn, {
      localVue,
      vuetify,
      router,
      sync: false
    });
    expect(wrapper.contains(".sign-in-box")).toBe(true);
    expect(wrapper.contains(".v-text-field")).toBe(true);
    expect(wrapper.contains(".v-btn")).toBe(true);
  });
});
