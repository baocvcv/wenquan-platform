import { mount, createLocalVue } from "@vue/test-utils";
import Question from "@/views/Question.vue";
import Vue from "vue";
import Vuex from "vuex";
import Vuetify from "vuetify";
import Router from "vue-router";
import UserFactory from "./utils/UserFactory.js";
import QuestionFactory from "./utils/QuestionFactory.js";

const localVue = createLocalVue();
Vue.use(Vuex);
Vue.use(Vuetify);
Vue.use(Router);

const user_factory = new UserFactory();
const question_factory = new QuestionFactory();

describe("UserTable.vue", () => {
  let vuetify, router, store;
  
  beforeEach(() => {
    vuetify = new Vuetify();
    router = new Router({
      routes: [
        {
          path: "/admin/questions/:id",
          name: "question",
          component: Question
        },
        {path: "/"}
      ]
    });
    store = new Vuex.Store({
      state: {
        user: user_factory.create_anonymous_admin()
      }
    })
  });
  it("renders question view in a separate route", async (done) => {
    router.push({name: "question", params: { id: 500 }})
    let wrapper = mount(Question, {
      localVue,
      vuetify,
      router,
      store,
      sync: false
    })
    setTimeout(async () => {
      expect(wrapper.vm.initData).toBeNull();
      wrapper.destroy();
      router.push({name: "question", params: {id: 200}});
      wrapper = mount(Question, {
        localVue,
        vuetify,
        store,
        router,
        sync: false,
        propsData: {
        }
      });
      setTimeout(async () => {
        //expect(wrapper.vm.initData != null).toBe(true);
        expect(wrapper.vm._editable).toBe(true);
        let edit_button = wrapper.find(".mdi-pencil");
        edit_button.trigger("click");
        await wrapper.vm.$nextTick();
        expect(wrapper.vm.edit_mode).toBe(true);
        done();
      }, 1000)
    }, 1000)
  })

  it("Can submit", async (done) => {
    router.push({name: "question", params: { id: 500 }})
    let wrapper = mount(Question, {
      localVue,
      vuetify,
      router,
      store,
      sync: false
    })
    setTimeout(async () => {
      wrapper.vm.submit(question_factory.create_question_for_creation());
      setTimeout(() => {
        wrapper.vm.submit(question_factory.create_single_choice(233));
        setTimeout(() => {
          done();
        }, 200)
      }, 200)
    }, 200)
  })
})