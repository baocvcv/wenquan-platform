import { mount,createLocalVue } from "@vue/test-utils";
import SignInBox from "@/components/SignInBox.vue";
import SignIn from "@/views/SignIn.vue";
import Vuetify from "vuetify";
import Vuex from "vuex";
import Vue from "vue";
import "./mock/SignInMock.js";
import bus from "../../src/components/EventBus";

const localVue = createLocalVue();
Vue.use(Vuetify);
Vue.use(Vuex);

describe("SignInBox.vue", () => {
    let vuetify;
    beforeEach(() => {
        vuetify = new Vuetify();
    });
    it("Correct Input", () => {
        const wrapper=mount(SignInBox, {
            localVue,
            vuetify,
            sync: false
        });
        wrapper.setData({
            username:"test",
            password:"test"
        });
        wrapper.vm.$nextTick(() => {
            expect(wrapper.contains(".v-btn--disabled")).toBe(false);
        });
    });
    it("Wrong Input", () => {
        const wrapper=mount(SignInBox, {
            localVue,
            vuetify,
            sync: false
        });
        wrapper.setData({
            username:"test",
            password:""
        });
        wrapper.vm.$nextTick(() => {
            expect(wrapper.contains(".v-btn--disabled")).toBe(true);
        });
    });

    it("Try login", async done => {
        const wrapper=mount(SignInBox, {
            localVue,
            vuetify,
            Vuex,
            sync: false
        });
        wrapper.setData({
            username: "testusr",
            password: "testpsw"
        });
        await wrapper.vm.$nextTick();
        wrapper.find("button").trigger("click");
        await wrapper.vm.$nextTick();
        bus.$on("error",() => {
            console.log(wrapper.vm.sign_in_response);
            done();
        });
    });
});

describe("SignIn.vue", () => {
    let vuetify;
    beforeEach(() => {
        vuetify = new Vuetify();
    });
    it("Render Component Correctly", () => {
        const wrapper=mount(SignIn, {
            localVue,
            vuetify,
            sync: false
        });
        expect(wrapper.contains(".sign-in-box")).toBe(true);
        expect(wrapper.contains(".v-text-field")).toBe(true);
        expect(wrapper.contains(".v-btn")).toBe(true);
    });
});