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
	  console.log(wrapper.vm.question_banks);
	  console.log(wrapper.vm.process);
      console.log(wrapper.text());
	  done();
	})
  })
});
