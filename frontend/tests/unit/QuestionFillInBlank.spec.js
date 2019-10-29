import { mount,createLocalVue } from "@vue/test-utils";
import FillInBlank from "@/components/QuestionFillInBlank.vue";
import Vuetify from "vuetify";
import Vue from "vue";

const localVue = createLocalVue();
Vue.use(Vuetify);

describe("QuestionFillInBlank.vue", () => {
    let vuetify;
    beforeEach(() => {
        vuetify = new Vuetify();
    });
    it("None blank number", () => {
        const wrapper=mount(FillInBlank, {
            localVue,
            vuetify,
            sync: false
        });
        expect(wrapper.vm.blankNum).toBe(0);
    });
    it("Blank number", () => {
        const wrapper=mount(FillInBlank, {
            localVue,
            vuetify,
            sync: false
        });
        wrapper.vm.edited_data.content = "a__b_c_______________    _alsjv";
        expect(wrapper.vm.blankNum).toBe(4);
    });
    it("Too long answers split rightly", () => {
        const wrapper=mount(FillInBlank, {
            localVue,
            vuetify,
            sync: false
        });
        wrapper.vm.edited_data.content = "a_b_c_d_e_f";
        wrapper.vm.edited_data.answers = [
            "1","2","3","4","5"
        ];
        wrapper.vm.edited_data.content = "a_b";
        expect(wrapper.vm.parse().question_blank_num).toBe(1);
        expect(wrapper.vm.parse().question_ans).toEqual(["1"]);
    });
    it("Submit event listener", () => {
        const wrapper=mount(FillInBlank, {
            localVue,
            vuetify,
            sync: false
        });
        wrapper.vm.submit();
        expect(wrapper.emitted().submit).toBeTruthy();
    });
    it("Submitted assignment", () => {
        const wrapper=mount(FillInBlank, {
            localVue,
            vuetify,
            sync: false
        });
        let testObj = Object.assign({},wrapper.vm.data);
        testObj.id = -100;
        wrapper.vm.edited_data = testObj;
        expect(wrapper.vm.data.id == -100).toBe(false);
        wrapper.vm.submitted();
        expect(wrapper.vm.data).toEqual(testObj);
    });
    it("Submitted assignment", () => {
        const wrapper=mount(FillInBlank, {
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
        const wrapper=mount(FillInBlank, {
            localVue,
            vuetify,
            sync: false
        });
        wrapper.vm.data.answers = ["test"];
        wrapper.vm.submitted();
        wrapper.vm.reset();
        expect(wrapper.vm.data.answers).toEqual([]);
    });
    it("Update data assignment", () => {
        const wrapper=mount(FillInBlank, {
            localVue,
            vuetify,
            sync: false
        });
        let input = {
            "id": 12,
            "parents_node": [1],
            "history_version_id":1,
            "question_change_time": "2019-10-15T01:11:21.754312Z",
            "question_name": "question4",
            "question_type": "fill_blank",
            "question_level": 5,
            "question_content": ["人类的本质是","和","还有",""],
            "question_blank_num": 3,
            "question_image": [""],
            "question_ans": ["复读机", "鸽子", "真香"],
            "question_solution": "因为人类的本质是复读机,鸽子,真香"
        };
        wrapper.vm.updateData(input);
        expect(wrapper.vm.data.id).toBe(12);
        expect(wrapper.vm.edited_data.id).toBe(12);
    });
});
