<template>
  <div id="rich-text-editor">
    <v-container class="pl-0 pr-0 ml-0 mr-0">
      <span class="grey--text caption">{{ label }}</span>
      <image-uploader
        ref="uploader"
        multiple
        tool
        @upload-start="start_upload"
        @upload-finish="finish_upload"
      ></image-uploader>
      <quill-editor
        ref="TextEditor"
        :content="content"
        :disabled="readonly"
        @change="onEditorChange($event)"
        @blur="blur"
        @focus="focus"
        :options="editorOption"
      >
      </quill-editor>
      <v-btn id="virtual-upload-button" @click="$refs.uploader.upload()" v-show="false"></v-btn>
      <span v-show="is_empty && required" class="caption error--text pl-2 pr-2">{{get_label}} is required.</span>
    </v-container>
  </div>
</template>

<script>
// require styles
import "quill/dist/quill.core.css";
import "quill/dist/quill.snow.css";
import "quill/dist/quill.bubble.css";

import { quillEditor } from "vue-quill-editor";

import ImageUploader from "@/components/ImageUploader.vue";

export default {
  name: "rich-text-editor",
  props: {
    readonly: {
      type: Boolean,
      default: false
    },
    placeholder: {
      type: String,
      default: ""
    },
    label: {
      type: String,
      default: ""
    },
    content: {
      type: String,
      default: ""
    },
    required: {
      type: Boolean,
      default: false
    }
  },
  components: {
    quillEditor,
    "image-uploader": ImageUploader
  },
  data: function() {
    return {
      is_empty: false,
      editorOption: {
        theme: "bubble",
        placeholder: "",
        modules: {
          toolbar: {
            container: [
              ["bold", "italic", "underline", "strike"],
              [{ list: "ordered" }, { list: "bullet" }],
              [{ header: [1, 2, 3, 4, 5, 6, false] }],
              [{ color: [] }, { background: [] }],
              [{ font: [] }],
              [{ align: [] }],
              ["link", "image"],
              ["clean"]
            ],
            handlers: {
              image: function(value) {
                if (value) {
                  document.querySelector('#virtual-upload-button').click()
                } else {
                  this.quill.format("image", false);
                }
              }
            }
          }
        }
      }
    };
  },
  model: {
    prop: "content",
    event: "change"
  },
  created() {
    if (this.readonly) this.editorOption.theme = "bubble";
    else this.editorOption.theme = "snow";
    this.editorOption.placeholder = this.placeholder;
  },
  computed: {
    get_label() {
      let str = this.label;
      if (str && str.endsWith('*'))
        return str.substr(0, str.length - 1);
      return str;
    }

  },
  methods: {
    onEditorChange({ editor, html, text }) {
      this.$emit("change", html);
    },
    start_upload() {
      console.log("Start uploading!");
      this.$notify({
        title: "Start uploading the picutre..."
      })
    },
    finish_upload(url) {
      let quill = this.$refs.TextEditor.quill;
      // 获取光标所在位置
      let length = quill.getSelection().index;
      // 插入图片  res.info为服务器返回的图片地址
      quill.insertEmbed(length, 'image', url);
      // 调整光标到最后
      quill.setSelection(length + 1);
      this.$notify({
        title: "Finish uploading the picture!",
        type: "success"
      })
    },
    blur() {
      if (this.content.length === 0) {
        this.is_empty = true;
      }
    },
    focus() {
      this.is_empty = false;
    },
    reset() {
      this.$refs.TextEditor.deleteText();
    }
  }
};
</script>
