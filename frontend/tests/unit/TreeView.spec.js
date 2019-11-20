import { mount, createLocalVue } from "@vue/test-utils";
import TreeView from "@/components/TreeView.vue";
import Vue from "vue";
import Vuex from "vuex";
import Vuetify from "vuetify";
import Router from "vue-router";
import { wrap } from "module";

const localVue = createLocalVue();
Vue.use(Vuex);
Vue.use(Vuetify);
Vue.use(Router);

describe("TreeView.vue", () => {
  let vuetify, router;

  beforeEach(() => {
    vuetify = new Vuetify();
  });

  it("travel through all funcs", () => {
    const wrapper = mount(TreeView, {
      localVue,
      vuetify,
      router,
      sync: false
    });
    wrapper.vm.select([wrapper.vm.treeData[0]]);
    wrapper.vm.beginEdit();
    wrapper.vm.select([wrapper.vm.treeData[0]]);
    wrapper.vm.clearSelection();
    wrapper.vm.submit();
    wrapper.vm.cancel();
    wrapper.vm.updateData([]);
  });

  it("travel through all funcs", () => {
    const wrapper = mount(TreeView, {
      localVue,
      vuetify,
      router,
      sync: false
    });
    wrapper.vm.removeNode();
    wrapper.vm.rename();
    wrapper.vm.beginEdit();
    wrapper.vm.select([wrapper.vm.treeData[0]]);
    wrapper.vm.rename();
    wrapper.vm.renameConfirmation();
    wrapper.vm.removeNode();
  });

});
