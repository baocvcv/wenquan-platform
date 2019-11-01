import { mount, createLocalVue } from "@vue/test-utils";
import ImageUploader from "@/components/ImageUploader.vue";
import Vue from "vue";
import Vuetify from "vuetify";
const localVue = createLocalVue();
Vue.use(Vuetify);

var dataurl =
  "data:image/gif;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVQImWNgYGBgAAAABQABh6FO1AAAAABJRU5ErkJggg==";
var arr = dataurl.split(","),
  mime = arr[0].match(/:(.*?);/)[1],
  bstr = atob(arr[1]),
  n = bstr.length,
  u8arr = new Uint8Array(n);
while (n--) {
  u8arr[n] = bstr.charCodeAt(n);
}
var file = new File([u8arr], "test", { type: mime });
const src = {
  target: { files: [file] }
};
describe("ImageUploader.vue", () => {
  let vuetify;
  beforeEach(() => {
    vuetify = new Vuetify();
  });
  it("preview image", async done => {
    const wrapper = mount(ImageUploader, {
      vuetify,
      localVue,
      sync: false
    });
    const upload_btn = wrapper.find("button");
    upload_btn.trigger("click");
    wrapper.vm.preview_image(src);
    setTimeout(() => {
      expect(wrapper.vm.img[0]).toBe(dataurl);
      done();
    }, 1000);
  });
  it("Cancel selecting an image", async done => {
    const wrapper = mount(ImageUploader, {
      vuetify,
      localVue,
      sync: false
    });
    const none_src = {
      target: { files: [] }
    };
    wrapper.vm.preview_image(none_src);
    setTimeout(() => {
      expect(wrapper.vm.img.length).toBe(0);
      done();
    }, 1000);
  });
  it("delete image", async done => {
    const wrapper = mount(ImageUploader, {
      vuetify,
      localVue,
      sync: false
    });
    wrapper.setProps({
      img: [dataurl]
    });
    await wrapper.vm.$nextTick();
    const delete_btn = wrapper.find("button");
    delete_btn.trigger("click");
    await wrapper.vm.$nextTick();
    expect(wrapper.vm.img.length).toBe(0);
    done();
  });
});
