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
        }, 500)
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
        }, 500)
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
        }, 500)
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
        }, 500)
    })

    it("Filters work properly", async (done) => {
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
        wrapper.setData({
            type_filter: ["single"]
        })
        setTimeout(async () => {
            let filter_button = wrapper.find(".mdi-filter");
            filter_button.trigger("click");
            await wrapper.vm.$nextTick();
            let reset_filter_button = wrapper.find(".mdi-autorenew");
            reset_filter_button.trigger("click");
            await wrapper.vm.$nextTick();
            expect(wrapper.vm.type_filter.length === 0).toBe(true);
            done();
        }, 500)
    })

    it("Creates questions", async(done) => {
        const wrapper = mount(QuestionList, {
            localVue,
            vuetify,
            router,
            sync: false,
            propsData: {
                id: 2,
                select: true,
                questions: []
            }
        })
        setTimeout(async () => {
            let create_button;
            let buttons = wrapper.findAll("button");
            for (let index = 0; index < buttons.length; index++)
            {
                if (buttons.at(index).text() === "Create")
                    create_button = buttons.at(index); 
            }
            expect(create_button.exists()).toBe(true);
            create_button.trigger("click");
            await wrapper.vm.$nextTick();
            wrapper.vm.create(2);
            setTimeout(() => {
                wrapper.vm.create(3);
                setTimeout(() => {
                    expect(wrapper.vm.question_list.length === 1).toBe(true);
                    done();
                }, 250)
            }, 250)
        }, 250)
    })
})