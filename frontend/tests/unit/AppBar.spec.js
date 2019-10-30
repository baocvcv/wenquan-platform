import {mount, createLocalVue} from "@vue/test-utils";
import AppBar from "@/components/AppBar.vue";
import UserFactory from "./UserFactory.js";
import Vue from "vue";
import Vuex from "vuex";
import Vuetify from "vuetify";
import Router from "vue-router";
import RouterRule from "@/router";
import { setFlagsFromString } from "v8";

const localVue = createLocalVue();
Vue.use(Vuex);
Vue.use(Vuetify);
Vue.use(Router);

const user_factory = new UserFactory();

describe("AppBar.vue", () => {
    let vuetify, router;

    beforeEach(() => {
        vuetify = new Vuetify();
        router = new Router({ RouterRule });
    });

    it("renders Sign in/ Sign up button if not signed in", () => {
        const store = new Vuex.Store({
            state: {
                user: null
            }
        });
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
        const user_logged_in = user_factory.create_anonymous_admin();
        const store = new Vuex.Store({
            state: {
                user: user_logged_in
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

    it("renders admin_entry and exit properly", async () => {
        const store = new Vuex.Store({
            state: {
                user: null,
            }
        })
        let wrapper = mount(AppBar, {
            localVue,
            vuetify,
            router,
            store,
            sync: false
        });

        //not logged in
        expect(wrapper.contains("a[href='#/admin']")).toBe(false);
        let button_wrappers = wrapper.findAll("a[href='#/']")
        let index;
        for (index = 0; index < button_wrappers.length; index++)
        {
            expect(button_wrappers.at(index).text() === "Exit").toBe(false);
        }

        //logged in  as Admin
        wrapper = user_factory.login(wrapper, "Admin");
        await wrapper.vm.$nextTick();
        button_wrappers = wrapper.findAll("a[href='#/']")
        for (index = 0; index < button_wrappers.length; index++)
        {
            expect(button_wrappers.at(index).text() === "Exit").toBe(false);
        }
        expect(wrapper.contains("a[href='#/admin']")).toBe(true);
        wrapper.vm.$router.push("/admin/");
        await wrapper.vm.$nextTick();
        button_wrappers = wrapper.findAll("a[href='#/']")
        let flag = false;
        for (index = 0; index < button_wrappers.length; index++)
        {
            if (button_wrappers.at(index).text() === "Exit")
                flag = true;
        }
        expect(flag).toBe(true);
        expect(wrapper.contains("a[href='#/admin']")).toBe(false);

        //logged in as SuperAdmin
        wrapper.vm.$router.push("/");
        wrapper = user_factory.login(wrapper, "SuperAdmin");
        await wrapper.vm.$nextTick();
        expect(wrapper.contains("a[href='#/admin']")).toBe(true);
        wrapper.vm.$router.push("/admin/");
        await wrapper.vm.$nextTick();
        button_wrappers = wrapper.findAll("a[href='#/']")
        flag = false;
        for (index = 0; index < button_wrappers.length; index++)
        {
            if (button_wrappers.at(index).text() === "Exit")
                flag = true;
        }
        expect(flag).toBe(true);

        //logged in as Student
        wrapper = user_factory.login(wrapper, "Student")
        await wrapper.vm.$nextTick();
        expect(wrapper.contains('a[href="#/admin"]')).toBe(false);
    });

    it("logout function works properly", async (done) => {
        window.alert = jest.fn();
        const store = new Vuex.Store({
            state: {
                user: null,
            }
        })
        let wrapper = mount(AppBar, {
            localVue,
            vuetify,
            router,
            store,
            sync: false
        });

        let button_wrappers = wrapper.findAll("a[href='#/']");
        let index;
        for (index = 0; index < button_wrappers.length; index++)
        {
            expect(button_wrappers.at(index).text != "Log out");
        }
        wrapper = user_factory.login(wrapper, "Student");
        await wrapper.vm.$nextTick();
        let log_out_wrapper;
        button_wrappers = wrapper.findAll("a[href='#/']");
        for (index = 0; index < button_wrappers.length; index++)
        {
            if (button_wrappers.at(index).text() === "Log out")
                log_out_wrapper = button_wrappers.at(index);
        }
        expect(log_out_wrapper.exists()).toBe(true);
        let log_out_button = log_out_wrapper.find('button');
        log_out_button.trigger("click");
        setTimeout(() => {
            expect(wrapper.vm.$store.state.user === null).toBe(true);
            done();
        }, 1000);
    })
});