import {mount, createLocalVue} from "@vue/test-utils";
import UserTable from "@/components/UserTable.vue";
import UserFactory from "./UserFactory.js";
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

    it("renders props.users according to their types", () => {
        const users = [
            user_factory.create_anonymous_student(),
            user_factory.create_anonymous_admin(),
            user_factory.create_anonymous_superadmin()
        ];
        const user = user_factory.create_user_admin();
        const store = new Vuex.Store({
            state: {
                user: user
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
        for (let i = 0; i < data_table_items.length; i++)
        {
            let data_table_item = data_table_items[i];
            const username = data_table_item.find(td).text();
            expect(username).toBe(users[i].username);
        }
    });

    it("emits change_user_type event after changing user type", () => {
        const users = [
            user_factory.create_anonymous_student()
        ];
        const user = user_factory.create_user_superadmin();
        const store = new Vuex.Store({
            state: {
                user: user
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
        //expect(wrapper.vm.$store.state.user.username).toBe("Admin_signed_in");
        let change_user_type_button = wrapper.find('.v-icon--link.mdi-arrow-up');
        change_user_type_button.trigger("click");
        //expect(wrapper.vm.dialog_change_user_type).toBe(true);
        console.log(wrapper.html());
        //expect(wrapper.emitted("change-user-type")).toBeTruthy();
    });

    it("emits change_user_status event after changing user status", () => {
        const users = [
            user_factory.create_anonymous_student()
        ];
        const user = user_factory.create_user_admin();
        const store = new Vuex.Store({
            state: {
                user: user
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
        //expect(wrapper.emitted('change-user-status')).toBeTruthy();
    });

    it("emits create_user event after clicking the CREATE button in the dialog", () => {
        const users = [
            user_factory.create_anonymous_student()
        ];
        const user = user_factory.create_user_admin();
        const store = new Vuex.Store({
            state: {
                user: user
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
        //expect(wrapper.emitted('create-user')).toBeTruthy();
    });

    it("shows the dialog after toggling the CREATE button", () => {
        
    });

    it("updates the user list after modifying it in the parent component", () => {

    });
});