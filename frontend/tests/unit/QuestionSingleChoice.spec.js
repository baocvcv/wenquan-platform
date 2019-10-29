import { mount,createLocalVue } from "@vue/test-utils";
import SingleChoice from "@/components/QuestionSingleChoice.vue";
import Vuetify from "vuetify";
import Vue from "vue";

const localVue = createLocalVue();
Vue.use(Vuetify);

describe("QuestionSingleChoice.vue", () => {
    let vuetify;
    beforeEach(() => {
        vuetify = new Vuetify();
    });
    it("Choice num change assert", () => {
        const wrapper=mount(SingleChoice, {
            localVue,
            vuetify,
            sync: false
        });
        expect(wrapper.vm.edited_question.question_choice.length).toBe(0);
        wrapper.vm.choice_num_up();
        expect(wrapper.vm.edited_question.question_choice.length).toBe(1);
        wrapper.vm.delete_choice(0);
        expect(wrapper.vm.edited_question.question_choice.length).toBe(0);
        wrapper.vm.choice_num_up();
        wrapper.vm.edited_question.question_ans = wrapper.vm.edited_question.question_choice[0];
        wrapper.vm.delete_choice(0);
        expect(wrapper.vm.edited_question.question_choice.length).toBe(0);
    });
    it("Submit event listener", () => {
        const wrapper=mount(SingleChoice, {
            localVue,
            vuetify,
            sync: false
        });
        wrapper.vm.choice_num_up();
        wrapper.vm.edited_question.question_ans = wrapper.vm.edited_question.question_choice[0];
        wrapper.vm.submit();
        expect(wrapper.emitted().submit).toBeTruthy();
    });
    it("Submitted assignment", () => {
        const wrapper=mount(SingleChoice, {
            localVue,
            vuetify,
            sync: false
        });
        let testObj = Object.assign({},wrapper.vm.question);
        testObj.id = -100;
        wrapper.vm.edited_question = testObj;
        expect(wrapper.vm.question.id == -100).toBe(false);
        wrapper.vm.submitted();
        expect(wrapper.vm.question).toEqual(testObj);
    });
    it("Submitted assignment", () => {
        const wrapper=mount(SingleChoice, {
            localVue,
            vuetify,
            sync: false
        });
        wrapper.vm.edited_question.id = -100;
        expect(wrapper.vm.question.id).toBe(-1);
        wrapper.vm.cancel();
        expect(wrapper.vm.edited_question.id).toBe(-1);
        expect(wrapper.emitted().cancel).toBeTruthy();
    });
    it("Reset assignment", () => {
        const wrapper=mount(SingleChoice, {
            localVue,
            vuetify,
            sync: false
        });
        wrapper.vm.choice_num_up();
        wrapper.vm.submitted();
        wrapper.vm.reset();
        expect(wrapper.vm.question.question_choice.length).toBe(0);
    });
    it("Update question assignment", () => {
        const wrapper=mount(SingleChoice, {
            localVue,
            vuetify,
            sync: false
        });
        let input = {
            "id": 12,
            "parents_node": [0],
            "history_version_id":1,
            "question_change_time": "2019-10-15T01:11:21.754312Z",
            "question_name": "question1",
            "question_type": "single",
            "question_level": 5,
            "question_content": "人类的本质是?",
            "question_image": [""],
            "question_choice": ["A.复读机", "B.鸽子", "C.真香", "D.以上选项均正确"],
            "question_ans": "D",
            "question_solution": "某一时刻被观测时, 人类会坍缩为A,B,C中某一种情况"
        };
        wrapper.vm.updateData(input);
        expect(wrapper.vm.question.id).toBe(12);
        expect(wrapper.vm.edited_question.id).toBe(12);
    });
});
