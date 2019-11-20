import { mount, createLocalVue } from "@vue/test-utils";
import PaperSolve from "@/components/PaperSolve.vue";
import Vue from "vue";
import Vuex from "vuex";
import Vuetify from "vuetify";
import Router from "vue-router";
import RouterRule from "@/router";
import "./mock/CreateAuthCodeCard.js";
import { wrap } from "module";

const localVue = createLocalVue();
Vue.use(Vuetify);
Vue.use(Router);
Vue.use(Vuex);

describe("PaperSolve.vue", () => {
  let vuetify, router, store;
  beforeEach(() => {
    vuetify = new Vuetify();
    router = new Router({ RouterRule });
    store = new Vuex.Store({
      state: {
        user: {
          id: 123
        }
      },
      mutations: {
        updateUser(state, payload) {},
        updateUserWithKey(state, payload) {}
      }
    });
  });

  it("travel", async done => {
    const wrapper = mount(PaperSolve, {
      localVue,
      vuetify,
      router,
      store,
      sync: false,
      propsData: {
        initData: {
          sections: [
            {
              questions: [
                {
                  id: 1
                }
              ]
            }
          ]
        }
      }
    });
    wrapper.setProps({
      initData: {
        sections: [
          {
            questions: [
              {
                id: 2
              },
              {
                id: 3
              }
            ]
          },
          {
            questions: [
              {
                id: 4
              },
              {
                id: 5
              }
            ]
          }
        ]
      }
    });
    await wrapper.vm.$nextTick();
    wrapper.vm.total_index;
    wrapper.vm.change_current_question(1, 1);
    wrapper.vm.change_current_question(0, 0);
    wrapper.vm.next_question();
    wrapper.vm.next_question();
    wrapper.vm.previous_question();
    wrapper.vm.previous_question();
    wrapper.vm.parse_answer([]);
    wrapper.vm.parse_answer(["A"]);
    wrapper.vm.parse_answer("A");
    wrapper.vm.parse_answer([undefined]);
    wrapper.vm.answers = [[], "A", "A", "A"];
    wrapper.vm.submit();
    wrapper.vm.answers = ["A", "A", "A", "A"];
    wrapper.vm.submit();
    wrapper.vm.submit_cache = null;
    wrapper.vm.submit_confirm();
    wrapper.vm.$nextTick(() => done());
  });
});
