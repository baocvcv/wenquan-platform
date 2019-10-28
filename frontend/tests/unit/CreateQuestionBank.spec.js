import { mount, createLocalVue } from "@vue/test-utils";
import CreateQuestionBank from "@/components/CreateQuestionBank";
import Vue from "vue";
import Vuetify from "vuetify";
import "./mock/SignUpMock";
const localVue = createLocalVue();
Vue.use(Vuetify);

describe("CreateQuestionBank.vue", () => {
  let vuetify;
  beforeEach(() => {
    vuetify = new Vuetify();
  });
  it("create success", () => {

  })
})
