<template>
  <div class="image-uploader" :style="img_style">
    <v-img v-if="!!img" :src="img ? img : ''" />
    <v-file-input
      :label="label"
      chips
      @change="preview_image($event)"
      accept="image/png image/jpg image/jpeg image/bmp"
      :placeholder="placeholder"
      :prepend-icon="icon"
    >
    </v-file-input>
  </div>
</template>

<script>
export default {
  name: "image-uploader",
  model: {
    prop: "img",
    event: "change"
  },
  props: {
    label: {
      type: String,
      default: "picture"
    },
    placeholder: {
      type: String,
      default: "upload image"
    },
    icon: {
      type: String,
      default: "mdi-camera"
    },
    image: undefined,
    width: String,
    height: String
  },
  data: function() {
    return {
      img: this.image,
      img_style: {
        width: this.width,
        height: this.height
      }
    };
  },
  methods: {
    preview_image(src) {
      var file = src;
      let that = this;
      let reader = new FileReader();

      if (file) {
        reader.readAsDataURL(file);
      } else {
        this.img = undefined;
        this.$emit("change", this.img);
      }

      reader.onload = function() {
        that.img = this.result;
        that.$emit("change", that.img);
      };
    }
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.image-uploader {
  margin: auto;
}
</style>
