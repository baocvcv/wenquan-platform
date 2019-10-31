import { mount, createLocalVue } from "@vue/test-utils";
import QuestionList from "@/components/QuestionList.vue";
import Vue from "vue";
import Vuetify from "vuetify";
import Router from "vue-router";
import RouterRule from "@/router";
import "./mock/QuestionListMock.js";

const localVue = createLocalVue();
Vue.use(Vuetify);
Vue.use(Router);

describe("QuestionList.vue", () => {
    let vuetify, router;
    beforeEach(() => {
        vuetify = new Vuetify();
        router = new Router({ RouterRule });
    });
    it("Fails to fetch data from question bank", async (done) => {
        const wrapper = mount(QuestionList, {
            localVue,
            vuetify,
            router,
            sync: false,
            propsData: {
                id: 1,
                select: false
            }
        });
        setTimeout(() => {
            done();
        }, 1000)
    })

    it("Fails to fetch data from questions", async (done) => {
        const wrapper = mount(QuestionList, {
            localVue,
            vuetify,
            router,
            sync: false,
            propsData: {
                id: 1,
                select: true
            }
        });
        setTimeout(() => {
            done();
        }, 1000)
    })
    
    it("Renders the component successfully", async (done) => {
        const wrapper = mount(QuestionList, {
            localVue,
            vuetify,
            router,
            sync: false,
            propsData: {
                id: 1,
                questions: [1]
            }
        })
        setTimeout(() => {
            expect(wrapper.vm.question_list.length != 0).toBe(true);
            expect(wrapper.exists(wrapper.vm.question_list[0].content)).toBe(true);
            done();
        }, 1000)
    })

    it("Select works properly", async (done) => {
        const wrapper = mount(QuestionList, {
            localVue,
            vuetify,
            router,
            sync: false,
            propsData: {
                id: 1,
                questions: [1],
                select: true
            }
        })
        setTimeout(async () => {
            let buttons = wrapper.findAll("button");
            let cancel_button;
            let done_button;
            for (let index = 0; index < buttons.length; index++)
            {
                if (buttons.at(index).text() === "Cancel")
                    cancel_button = buttons.at(index);
                else if (buttons.at(index).text() === "Done")
                    done_button = buttons.at(index);
            }
            expect(cancel_button.exists()).toBe(true);
            expect(done_button.exists()).toBe(true);
            wrapper.setData({
                selected_questions: [1]
            });
            cancel_button.trigger("click");
            await wrapper.vm.$nextTick();
            expect(wrapper.emitted("cancel-select")).toBeTruthy();
            expect(wrapper.vm.selected_questions.length === 0).toBe(true);
            wrapper.setData({
                selected_questions: [1]
            })
            done_button.trigger("click");
            wrapper.vm.done_select();
            await wrapper.vm.$nextTick();
            expect(wrapper.emitted("done-select")).toBeTruthy();
            expect(wrapper.emitted("done-select").length).toBe(1);
            expect(wrapper.emitted("done-select")[0]).toEqual([[1]]);
            done();
        }, 1000)
    })
})