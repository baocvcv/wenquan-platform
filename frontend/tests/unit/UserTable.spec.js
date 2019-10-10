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
        vuetify = new Vuetify()
    });

    it("renders props.users according to their types", () => {
        const users = [
            user_factory.createAnonymousStudent(),
            user_factory.createAnonymousAdmin(),
            user_factory.createAnonymousSuperAdmin()
        ];
        const wrapper = mount(UserTable, {
            localVue,
            vuetify,
            propsData: {
                users
            }
        });
        expect(wrapper.contains(".v-dialog")).toBe(true);
    });

    it("emits change_user_type event after changing user type", () => {

    });

    it("emits change_user_status event after changing user status", () => {

    });

    it("emits create_user event after clicking the CREATE button in the dialog", () => {

    });

    it("shows the dialog after toggling the CREATE button", () => {

    });

    it("updates the user list after modifying it in the parent component", () => {

    });
});