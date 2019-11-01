import { mount, createLocalVue } from "@vue/test-utils";
import BriefAnswer from "@/components/QuestionBriefAnswer.vue";
import Vuetify from "vuetify";
import Vue from "vue";

const localVue = createLocalVue();
Vue.use(Vuetify);

describe("QuestionBriefAnswer.vue", () => {
  let vuetify;
  beforeEach(() => {
    vuetify = new Vuetify();
  });
  it("Submit event listener", () => {
    const wrapper = mount(BriefAnswer, {
      localVue,
      vuetify,
      sync: false
    });
    wrapper.vm.answer = "Answer";
    wrapper.vm.submit();
    expect(wrapper.emitted().submit).toBeTruthy();
  });
  it("Submitted assignment", () => {
    const wrapper = mount(BriefAnswer, {
      localVue,
      vuetify,
      sync: false
    });
    let testObj = Object.assign({}, wrapper.vm.data);
    testObj.id = -100;
    wrapper.vm.edited_data = testObj;
    expect(wrapper.vm.data.id == -100).toBe(false);
    wrapper.vm.submitted();
    expect(wrapper.vm.data).toEqual(testObj);
  });
  it("Submitted assignment", () => {
    const wrapper = mount(BriefAnswer, {
      localVue,
      vuetify,
      sync: false
    });
    wrapper.vm.edited_data.id = -100;
    expect(wrapper.vm.data.id).toBe(-1);
    wrapper.vm.cancel();
    expect(wrapper.vm.edited_data.id).toBe(-1);
    expect(wrapper.emitted().cancel).toBeTruthy();
  });
  it("Reset assignment", () => {
    const wrapper = mount(BriefAnswer, {
      localVue,
      vuetify,
      sync: false
    });
    wrapper.vm.data.answer = "test";
    wrapper.vm.submitted();
    wrapper.vm.reset();
    expect(wrapper.vm.data.answer).toBe("");
  });
  it("Update data assignment", () => {
    const wrapper = mount(BriefAnswer, {
      localVue,
      vuetify,
      sync: false
    });
    let input = {
      id: 12,
      parents_node: [2],
      history_version_id: 1,
      question_change_time: "2019-10-15T01:11:21.754312Z",
      question_name: "question5",
      question_type: "brief_ans",
      question_level: 5,
      question_content: "人类的本质是?",
      question_image: [""],
      question_ans: "复读机",
      question_solution: "因为人类的本质是复读机"
    };
    wrapper.vm.updateData(input);
    expect(wrapper.vm.data.id).toBe(12);
    expect(wrapper.vm.edited_data.id).toBe(12);
  });
});
