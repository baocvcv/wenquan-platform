import {mount, createLocalVue} from "@vue/test-utils";
import AppBar from "@/components/AppBar.vue";
import UserFactory from "./UserFactory.js";
import Vue from "vue";
import Vuex from "vuex";
import Vuetify from "vuetify";
import Router from "vue-router";

const localVue = createLocalVue();
Vue.use(Vuex);
Vue.use(Vuetify);
Vue.use(Router);

const user_factory = new UserFactory();

describe("AppBar.vue", () => {
    let vuetify;

    beforeEach(() => {
        vuetify = new Vuetify();
    });

    it("renders Sign in/ Sign up button if not signed in", () => {
        const store = new Vuex.Store({
            state: {
                user: null
            }
        });
        const router = new Router();
        const wrapper = mount(AppBar, {
            localVue,
            vuetify,
            store,
            router,
            sync: false,
        });
        expect(wrapper.contains("a[href='#/signup']")).toBe(true);
        expect(wrapper.contains("a[href='#/signin']")).toBe(true);
    });

    it("not renders Sign in/Sign up button if signed in", () => {
        const user = user_factory.create_user_admin();
        const store = new Vuex.Store({
            state: {
                user: user
            }
        });
        const router = new Router();
        const wrapper = mount(AppBar, {
            localVue,
            vuetify,
            store,
            router,
            sync: false,
        });
        expect(wrapper.contains("a[href='#/signup']")).toBe(false);
        expect(wrapper.contains("a[href='#/signin']")).toBe(false);
    });
});