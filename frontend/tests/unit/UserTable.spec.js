import { mount, createLocalVue } from "@vue/test-utils";
import UserTable from "@/components/UserTable.vue";
import UserFactory from "./utils/UserFactory.js";
import Vue from "vue";
import Vuex from "vuex";
import Vuetify from "vuetify";

const localVue = createLocalVue();
Vue.use(Vuex);
Vue.use(Vuetify);

const user_factory = new UserFactory();

describe("UserTable.vue", () => {
  let vuetify;

  beforeEach(() => {
    vuetify = new Vuetify();
  });

  it("renders props.users according to their types", async () => {
    const user_logged_in = user_factory.create_anonymous_superadmin();
    const users = [
      user_factory.create_anonymous_student(),
      user_factory.create_anonymous_admin(),
      user_logged_in
    ];
    const store = new Vuex.Store({
      state: {
        user: user_logged_in
      }
    });
    const wrapper = mount(UserTable, {
      localVue,
      vuetify,
      store,
      sync: false,
      propsData: {
        users
      }
    });
    const data_table_items = wrapper.find(".v-data-table > tbody >tr");
    for (let i = 0; i < data_table_items.length; i++) {
      let data_table_item = data_table_items[i];
      const username = data_table_item.find("td").text();
      expect(username).toBe(users[i].username);
    }
    wrapper.setData({
      dialog_create: true
    });
    await wrapper.vm.$nextTick();
    wrapper.vm.close_dialog_create();
    await wrapper.vm.$nextTick();
    expect(wrapper.vm.dialog_create).toBe(false);
  });

  it("emits change_user_group event after changing user group", async () => {
    const user_logged_in = user_factory.create_anonymous_superadmin();
    const users = [user_factory.create_anonymous_student(), user_logged_in];
    const store = new Vuex.Store({
      state: {
        user: user_logged_in
      }
    });
    const wrapper = mount(UserTable, {
      localVue,
      vuetify,
      store,
      sync: false,
      attachToDocument: true,
      propsData: {
        users
      }
    });
    wrapper.vm.change_user_group(user_factory.create_anonymous_student());
    await wrapper.vm.$nextTick();
    expect(wrapper.emitted("change-user-group")).toBeTruthy();
  });

  it("emits change_user_status event after changing user status", async () => {
    const user_logged_in = user_factory.create_anonymous_superadmin();
    const users = [user_factory.create_anonymous_student(), user_logged_in];
    const store = new Vuex.Store({
      state: {
        user: user_logged_in
      }
    });
    const wrapper = mount(UserTable, {
      localVue,
      vuetify,
      store,
      sync: false,
      propsData: {
        users
      }
    });
    let change_user_status_button = wrapper.find(".v-icon--link.mdi-cancel");
    change_user_status_button.trigger("click");
    expect(wrapper.emitted("change-user-status")).toBeTruthy();
  });

  it("Can create a new user", async () => {
    const user_logged_in = user_factory.create_anonymous_superadmin();
    const users = [user_logged_in];
    const store = new Vuex.Store({
      state: {
        user: user_logged_in
      }
    });
    let wrapper = mount(UserTable, {
      localVue,
      vuetify,
      store,
      sync: false,
      propsData: {
        users
      }
    });
    let create_user_button = wrapper.find(
      ".v-toolbar__content .v-btn.v-btn--contained"
    );
    create_user_button.trigger("click");
    wrapper = user_factory.login(wrapper, "Admin");
    await wrapper.vm.$nextTick();
    wrapper.vm.create();
    await wrapper.vm.$nextTick();
    expect(wrapper.emitted("create-user")).toBeTruthy();
    //expect(wrapper.emitted('create-user')).toBeTruthy();
  });
});
