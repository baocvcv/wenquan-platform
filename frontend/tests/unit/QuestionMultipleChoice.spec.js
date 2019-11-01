import { mount,createLocalVue } from "@vue/test-utils";
import MultipleChoice from "@/components/QuestionMultipleChoice.vue";
import Vuetify from "vuetify";
import Vue from "vue";

const localVue = createLocalVue();
Vue.use(Vuetify);

describe("QuestionMultipleChoice.vue", () => {
    let vuetify;
    beforeEach(() => {
        vuetify = new Vuetify();
    });
    it("Answer choice none assert", () => {
        const wrapper=mount(MultipleChoice, {
            localVue,
            vuetify,
            sync: false
        });
        wrapper.vm.$nextTick(() => {
            expect(wrapper.vm.answer).toBe("none");
        });
    });
    it("Add choice assert", () => {
        const wrapper=mount(MultipleChoice, {
            localVue,
            vuetify,
            sync: false
        });
        expect(wrapper.vm.edited_data.choices.length).toBe(4);
        wrapper.vm.addChoice();
        expect(wrapper.vm.edited_data.choices.length).toBe(5);
    });
    it("Remove choice assert", () => {
        const wrapper=mount(MultipleChoice, {
            localVue,
            vuetify,
            sync: false
        });
        console.log(wrapper.vm.edited_data.choices);
        expect(wrapper.vm.edited_data.choices.length).toBe(4);
        wrapper.vm.changeRightStatus(wrapper.vm.edited_data.choices[0]);
        wrapper.vm.removeChoice(0);
        expect(wrapper.vm.edited_data.choices.length).toBe(3);
        wrapper.vm.removeChoice(0);
        expect(wrapper.vm.edited_data.choices.length).toBe(2);
    });
    it("Change choice assert", () => {
        const wrapper=mount(MultipleChoice, {
            localVue,
            vuetify,
            sync: false
        });
        expect(wrapper.vm.edited_data.choices[0].right).toBe(false);
        wrapper.vm.changeRightStatus(wrapper.vm.edited_data.choices[0]);
        expect(wrapper.vm.edited_data.choices[0].right).toBe(true);
        wrapper.vm.changeRightStatus(wrapper.vm.edited_data.choices[0]);
        expect(wrapper.vm.edited_data.choices[0].right).toBe(false);
    });
    it("Right choice sort and answer gen assert", () => {
        const wrapper=mount(MultipleChoice, {
            localVue,
            vuetify,
            sync: false
        });
        wrapper.vm.changeRightStatus(wrapper.vm.edited_data.choices[1]);
        wrapper.vm.changeRightStatus(wrapper.vm.edited_data.choices[0]);
        expect(wrapper.vm.edited_data.rightAnswer.length).toBe(2);
        expect(wrapper.vm.edited_data.rightAnswer[0].name).toBe("A");
        expect(wrapper.vm.answer).toBe("AB");
    });
    it("Submit event listener", () => {
        const wrapper=mount(MultipleChoice, {
            localVue,
            vuetify,
            sync: false
        });
        wrapper.vm.changeRightStatus(wrapper.vm.edited_data.choices[1]);
        wrapper.vm.changeRightStatus(wrapper.vm.edited_data.choices[0]);
        wrapper.vm.submit();
        expect(wrapper.emitted().submit).toBeTruthy();
    });
    it("Submitted assignment", () => {
        const wrapper=mount(MultipleChoice, {
            localVue,
            vuetify,
            sync: false
        });
        let testObj = JSON.parse(wrapper.vm.data);
        testObj.id = -100;
        wrapper.vm.updateData(testObj);
        expect(wrapper.vm.edited_data.id == -100).toBe(true);
        wrapper.vm.submitted();
        expect(wrapper.vm.data).toBe(JSON.stringify(testObj));
    });
    it("Submitted assignment", () => {
        const wrapper=mount(MultipleChoice, {
            localVue,
            vuetify,
            sync: false
        });
        wrapper.vm.edited_data.id = -100;
        wrapper.vm.cancel();
        expect(wrapper.vm.edited_data.id).toBe(-1);
        expect(wrapper.emitted().cancel).toBeTruthy();
    });
    it("Reset assignment", () => {
        const wrapper=mount(MultipleChoice, {
            localVue,
            vuetify,
            sync: false
        });
        wrapper.vm.addChoice();
        wrapper.vm.submitted();
        wrapper.vm.reset();
        expect(wrapper.vm.edited_data.choices.length).toBe(4);
    });
    it("Update data assignment", () => {
        const wrapper=mount(MultipleChoice, {
            localVue,
            vuetify,
            sync: false
        });
        let input = {
            "id": 12,
            "parents_node": [0,1],
            "history_version_id":1,
            "question_change_time": "2019-10-15T01:11:21.754312Z",
            "question_name": "question2",
            "question_type": "multiple",
            "question_level": 5,
            "question_content": "人类的本质是?",
            "question_image": [""],
            "question_choice": ["A.复读机", "B.鸽子", "C.真香", "D.草履虫"],
            "question_ans": ["A","B","C"],
            "question_ans_num": 3,
            "question_solution": "某一时刻被观测时, 人类会坍缩为A,B,C中某一种情况"
        };
        wrapper.vm.updateData(input);
        expect(wrapper.vm.edited_data.id).toBe(12);
    });
});
