import { mount } from "@vue/test-utils";
import SignInBox from "@/components/SignInBox.vue";
import SignIn from "@/views/SignIn.vue";

describe("SignInBox.vue", () => {
    it("Correct Input", () => {
        const wrapper=mount(SignInBox);
        wrapper.setData({
            username:"test",
            password:"test"
        });
        expect(wrapper.html()).toContain("<v-btn>");
    });
    it("Wrong Input", () => {
        const wrapper=mount(SignInBox);
        wrapper.setData({
            username:"test",
            password:""
        });
        expect(wrapper.html()).toContain('<v-btn disabled="true">');
    });
});

describe("SignIn.vue", () => {
    it("Render Component Correctly", () => {
        const wrapper=mount(SignIn);
        expect(wrapper.findAll("div").at(1).classes()).toContain("sign-in-box");
        expect(wrapper.contains("v-text-field")).toBe(true);
        expect(wrapper.contains("v-btn")).toBe(true);
    });
});