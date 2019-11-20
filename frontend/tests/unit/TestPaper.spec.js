import { mount, createLocalVue } from "@vue/test-utils";
import TestPaper from "@/components/TestPaper.vue";
import Vue from "vue";
import Vuex from "vuex";
import Vuetify from "vuetify";
import Router from "vue-router";
import { wrap } from "module";

const localVue = createLocalVue();
Vue.use(Vuex);
Vue.use(Vuetify);
Vue.use(Router);

describe("TestPaper.vue", () => {
  let vuetify, router, store;

  beforeEach(() => {
    vuetify = new Vuetify();
    store = new Vuex.Store({
      state: {
        user: {
          id: 123
        }
      },
      mutations: {
        updateUser(state, payload) {
        },
        updateUserWithKey(state, payload) {
        }
      },
    })
  });

  it("travel through all funcs", () => {
    const wrapper = mount(TestPaper, {
      localVue,
      vuetify,
      router,
      store,
      sync: false,
      propsData: {
        paper: {
          title: "",
          total_point: "",
          tips: "",
          time_limit: "",
          status: "drafted",
          sections: []
        }
      }
    });
    for(var i=0;i<1001;i++) wrapper.vm.roman(i);
    wrapper.vm.reset();
    wrapper.vm.cancel();
    wrapper.vm.create_section();
    wrapper.vm.$emit("save",{
      title: "",
      total_point: "",
      tips: "",
      time_limit: "",
      status: "drafted",
      sections: []
    });
    wrapper.vm.judge_points_sum;
    wrapper.vm.edited_paper.sections[0].questions.push({
        id: -1,
        content: {},
        point_every_blank: [1,2,3]
      });
    wrapper.vm.question_sum_up(0);
    wrapper.vm.blank_point_sum_up(0,0);
    wrapper.vm.submit();
    wrapper.vm.drop_question(wrapper.vm.edited_paper.sections[0],0);
    wrapper.vm.drop_section(0);
    wrapper.vm.get_bank_id(0);
    wrapper.vm.get_selected_questions([1]);
    wrapper.vm.edit_button_clicked();
  });

});
