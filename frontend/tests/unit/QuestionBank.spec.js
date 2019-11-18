import { mount, createLocalVue } from "@vue/test-utils";
import QuestionBank from "@/views/admin/QuestionBank.vue";
import Home from "@/views/Home.vue";
import Vue from "vue";
import Vuex from "vuex";
import Vuetify from "vuetify";
import Router from "vue-router";
import "./mock/QuestionBankMock.js";

const localVue = createLocalVue();
Vue.use(Vuex);
Vue.use(Vuetify);
Vue.use(Router);

describe("QuestionBank.vue", () => {
  let vuetify, router;

  beforeEach(() => {
    vuetify = new Vuetify();
    //router = new Router({RouterRule});
    router = new Router({
      routes: [
        {
          path: "/admin/questionbanks/:id",
          name: "question-bank",
          component: QuestionBank
        },
        { path: "/", component: Home }
      ]
    });
  });

  it("Failed to fetch data", async done => {
    sessionStorage.setItem("user", {
      user_group: "Admin"
    });
    router.push({ name: "question-bank", params: { id: 500 } });
    let wrapper = mount(QuestionBank, {
      localVue,
      vuetify,
      router,
      sync: false
    });
    setTimeout(() => {
      done();
    }, 1000);
  });

  it("Can cancel and save in edit mode", async done => {
    sessionStorage.setItem("user", {
      user_group: "Admin"
    });
    router.push({ name: "question-bank", params: { id: 200 } });
    let wrapper = mount(QuestionBank, {
      localVue,
      vuetify,
      router,
      sync: false
    });
    setTimeout(async () => {
      expect(wrapper.vm.question_bank.id).toBe(200);
      expect(wrapper.exists(wrapper.vm.question_bank.title)).toBe(true);
      let edit_button = wrapper.find(".mdi-pencil");
      expect(edit_button.exists()).toBe(true);
      edit_button.trigger("click");
      await wrapper.vm.$nextTick();
      wrapper.setData({
        edited_question_bank: {
          name: "edited"
        }
      });
      let cancel_button, save_button;
      let buttons = wrapper.findAll("button");
      for (let i = 0; i < buttons.length; i++) {
        if (buttons.at(i).text() === "Cancel") cancel_button = buttons.at(i);
        else if (buttons.at(i).text() === "Save") save_button = buttons.at(i);
      }
      expect(cancel_button.exists()).toBe(true);
      expect(save_button.exists()).toBe(true);
      cancel_button.trigger("click");
      await wrapper.vm.$nextTick();
      expect(wrapper.vm.edited_question_bank.name === "edited").toBe(false);
      edit_button.trigger("click");
      await wrapper.vm.$nextTick();
      wrapper.setData({
        edited_question_bank: {
          name: "Fail"
        }
      });
      save_button.trigger("click");
      setTimeout(async () => {
        expect(wrapper.vm.edit_mode).toBe(true);
        wrapper.setData({
          edited_question_bank: {
            name: "edited"
          }
        });
        wrapper.vm.save();
        // save_button.trigger("click");
        setTimeout(() => {
          expect(wrapper.vm.edit_mode).toBe(false);
          expect(wrapper.vm.question_bank.name).toBe("edited");
          done();
        }, 1000);
      }, 500);
    }, 500);
  });

  it("Pops up an alert before discarding changes", async done => {
    sessionStorage.setItem("user", {
      user_group: "Admin"
    });
    router.push({ name: "question-bank", params: { id: 200 } });
    let wrapper = mount(QuestionBank, {
      localVue,
      vuetify,
      router,
      sync: false
    });
    setTimeout(async () => {
      window.confirm = jest.fn(() => {
        return false;
      });
      let edit_button = wrapper.find(".mdi-pencil");
      edit_button.trigger("click");
      await wrapper.vm.$nextTick();
      wrapper.setData({
        edited_question_bank_image: ["image"],
        edited_question_bank: {
          name: "edited"
        }
      });
      await wrapper.vm.$nextTick();
      expect(wrapper.vm.edit_mode).toBe(true);
      expect(wrapper.vm.edited).toBe(true);
      edit_button.trigger("click");
      await wrapper.vm.$nextTick();
      expect(window.confirm).toHaveBeenCalled();
      expect(wrapper.vm.edit_mode).toBe(true);
      window.confirm = jest.fn(() => {
        return true;
      });
      edit_button.trigger("click");
      await wrapper.vm.$nextTick();
      expect(window.confirm).toHaveBeenCalled();
      expect(wrapper.vm.edit_mode).toBe(false);
      done();
    }, 1000);
  });

  it("Pops up an alert when leaving current route with unsaved changes", async done => {
    sessionStorage.setItem("user", {
      user_group: "Admin"
    });
    router.push({ name: "question-bank", params: { id: 200 } });
    let wrapper = mount(QuestionBank, {
      localVue,
      vuetify,
      router,
      sync: false
    });
    setTimeout(async () => {
      let edit_button = wrapper.find(".mdi-pencil");
      edit_button.trigger("click");
      await wrapper.vm.$nextTick();
      wrapper.setData({
        edited_question_bank_image: ["edited_image"]
      });
      await wrapper.vm.$nextTick();
      expect(wrapper.vm.edited).toBe(true);
      window.confirm = jest.fn(() => {
        return false;
      });
      wrapper.vm.$router.push("/");
      await wrapper.vm.$nextTick();
      //expect(window.confirm).toHaveBeenCalled();
      //expect(wrapper.vm.$route.path === "/").toBe(false);
      window.confirm = jest.fn(() => {
        return true;
      });
      await wrapper.vm.$nextTick();
      //expect(wrapper.vm.$route.path).toBe("/");
      done();
    }, 1000);
  });
});
