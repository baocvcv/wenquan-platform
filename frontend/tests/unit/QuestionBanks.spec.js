import { mount, createLocalVue } from "@vue/test-utils";
import QuestionBanks from "@/views/QuestionBanks.vue";
import Vue from "vue";
import Vuetify from "vuetify";
import "./mock/QuestionBanksMock.js";
const localVue = createLocalVue();
Vue.use(Vuetify);

describe("QuestionBanks", () => {
  let vuetify;
  beforeEach(() => {
    vuetify = new Vuetify();
  });
  it("Render correctly", async done => {
    const wrapper = mount(QuestionBanks, {
      vuetify,
      localVue,
      sync: false
    });
	setTimeout(() => {
	  expect(wrapper.exists("test1")).toBe(true);
	  expect(wrapper.exists("test2")).toBe(true);
	  done();
	}, 1000);
  })
  it("Render failed", async done => {
    const wrapper = mount(QuestionBanks, {
      vuetify,
      localVue,
      sync: false
    });
	setTimeout(() => {
	  expect(wrapper.exists("Failed")).toBe(true);
	  done();
	}, 1000);
  })
});
