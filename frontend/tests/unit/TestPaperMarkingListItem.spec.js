import { mount, createLocalVue } from "@vue/test-utils";
import TestPaperMarkingListItem from "@/components/TestPaperMarkingListItem.vue";
import Vue from "vue";
import Vuetify from "vuetify";
import Vuex from "vuex";
import Router from "vue-router";
import RouterRule from "@/router";
import VueProgressBar from "vue-progressbar";
import Notifications from "vue-notification";
import "./mock/TestPaperMarkingListItemMock.js";

const localVue = createLocalVue();
Vue.use(Vuetify);
Vue.use(Router);
Vue.use(VueProgressBar);
Vue.use(Notifications);

describe("TestPaperMarkingListItem.vue", () => {
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
    const wrapper = mount(TestPaperMarkingListItem, {
      localVue,
      vuetify,
      router,
      store,
      sync: false,
	  propsData: {
		id: 0
	  }
    });
	wrapper.vm.paper_records = [{id: 0}, {id: 1}];
	wrapper.vm.show();
    await setTimeout(() => {}, 500);
	wrapper.vm.upload_marking(0);
    await setTimeout(() => {}, 500);
	wrapper.vm.upload_marking(0);
    await setTimeout(() => {}, 500);
	wrapper.vm.upload_all();
    await setTimeout(() => {}, 500);
	wrapper.vm.upload_all();
    setTimeout(() => {
      done();
    }, 500);
  });
});
