import {shallowMount, createLocalVue} from "@vue/test-utils";
import UserManagement from "@/views/UserManagement.vue";
import Vue from "vue";
import Vuex from "vuex";
import Vuetify from "vuetify";
import Router from "vue-router";
import RouterRule from "@/router";
import UserFactory from "./utils/UserFactory.js";

const localVue = createLocalVue();
Vue.use(Vuex);
Vue.use(Vuetify);
Vue.use(Router);

const user_factory = new UserFactory();

describe("UserManagement.vue", () => {
    let vuetify, router, store;

    beforeEach(() => {
        vuetify = new Vuetify();
        //router = new Router({RouterRule});
        router = new Router({RouterRule})
        store = new Vuex.Store({
            state: {
                user: user_factory.create_anonymous_admin()
            }
        })
    })

    it("Fails to fetch data", async () => {
        let wrapper = shallowMount(UserManagement, {
            localVue,
            vuetify,
            router,
            store,
            sync: false
        })
    })

    it("Can create user", async (done) => {
        let wrapper = shallowMount(UserManagement, {
            localVue,
            vuetify,
            router,
            store,
            sync: false
        })
        setTimeout(async () => {
            console.log(wrapper.html());
            //expect(wrapper.vm.users.length != 0).toBe(true);
            wrapper.vm.create_user(user_factory.create_anonymous_student());
            await wrapper.vm.$nextTick();
            let former_user_len = wrapper.vm.users.length;
            wrapper.vm.create_user(user_factory.create_anonymous_student());
            await wrapper.vm.$nextTick();
            //expect(wrapper.vm.users.length).toBe(former_user_len + 1);
            done();
        }, 1000)
    })

    it("Can change user status", async (done) => {
        let wrapper = shallowMount(UserManagement, {
            localVue,
            vuetify,
            router,
            store,
            sync: false
        })
        setTimeout(async () => {
            console.log(wrapper.html());
            //expect(wrapper.vm.users.length != 0).toBe(true);
            let user = user_factory.create_anonymous_student();
            user.id = 500;
            wrapper.vm.change_user_status(user);
            await wrapper.vm.$nextTick();
            let former_user_status = user.is_banned;
            user.id = 200;
            wrapper.vm.change_user_status(user);
            await wrapper.vm.$nextTick();
            expect(user.is_banned).toBe(!former_user_status);
            done();
        }, 1000)
    })

    it("Can change user group", async (done) => {
        let wrapper = shallowMount(UserManagement, {
            localVue,
            vuetify,
            router,
            store,
            sync: false
        })
        setTimeout(async () => {
            console.log(wrapper.html());
            //expect(wrapper.vm.users.length != 0).toBe(true);
            let user = user_factory.create_anonymous_student();
            user.id = 500;
            wrapper.vm.change_user_group(user);
            await wrapper.vm.$nextTick();
            let former_user_group = user.user_group;
            user.id = 200;
            wrapper.vm.change_user_group(user);
            await wrapper.vm.$nextTick();
            expect(user.user_group != former_user_group).toBe(true);
            done();
        }, 1000)
    })
})