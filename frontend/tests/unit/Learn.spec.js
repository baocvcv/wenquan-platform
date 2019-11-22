import { mount, createLocalVue } from "@vue/test-utils";
import Learn from "@/views/student/Learn.vue";
import Vue from "vue";
import Vuetify from "vuetify";
import Vuex from "vuex";
import Router from "vue-router";
import RouterRule from "@/router";
import VueProgressBar from "vue-progressbar";
import Notifications from "vue-notification";
import "./mock/LearnMock.js";

const localVue = createLocalVue();
Vue.use(Vuetify);
Vue.use(Router);
Vue.use(VueProgressBar);
Vue.use(Notifications);

describe("Test.vue", () => {
  let vuetify, router;
  beforeEach(() => {
    vuetify = new Vuetify();
    router = new Router({ RouterRule });
  });

  it("travel", async done => {
    const store = new Vuex.Store({
      state: {
        user: {
          id: 123
        }
      }
    });
    const wrapper = mount(Learn, {
      localVue,
      vuetify,
      router,
      store,
      sync: false
    });
	const paper = {
    "title":"unnamed paper",
    "total_point":100,
    "tips":"",
    "status":"drafted",
    "sections":[
        {
            "title":"unnamed sections",
            "total_point":50,
            "section_num":1,
            "questions":[
                {
                    "id":10,
                    "question_point":25,
                    "point_every_blank":[],
                    "question_num":1
                },
                {
                    "id":13,
                    "question_point":25,
                    "point_every_blank":[],
                    "question_num":2
                }
            ]
        },
        {
            "title":"unnamed sections",
            "total_point":50,
            "questions":[
                {
                    "id":10,
                    "question_point":25,
                    "point_every_blank":[],
                    "question_num":1
                },
                {
                    "id":13,
                    "question_point":25,
                    "point_every_blank":[],
                    "question_num":2
                }
            ]
        }
    ]
}

	const result = {
	  sections: [{
		questions: [{
		  id: 0,
		  ans: "A"
		}]
	  }]
	}
    await setTimeout(() => {}, 500);
	wrapper.vm.finish_practicing(result);
    await setTimeout(() => {}, 500);
    setTimeout(() => {
      done();
    }, 500);
  });
});
