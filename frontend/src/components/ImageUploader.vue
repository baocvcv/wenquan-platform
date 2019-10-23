<template>
  <div class="image-uploader" :style="img_style">
    <v-toolbar v-if="!!label">
      <v-toolbar-title>
        {{ label }}
      </v-toolbar-title>
    </v-toolbar>
    <v-container fluid align="center">
      <v-row justify="center" align="center">
        <v-col
          v-for="(image, i) in img"
          :key="i"
          cols="12"
          :lg="Math.max(12 / ((check_create() ? 1 : 0) + img.length), 4)"
          md="6"
          xs="12"
          align="center"
        >
          <v-img v-if="!!image" :aspect-ratio="aspectRatio" :src="image" />
          <v-btn v-if="!readonly" icon @click="delete_image(i)">
            <v-icon color="red">mdi-delete</v-icon>
          </v-btn>
        </v-col>
        <v-col v-if="check_create()" align="center">
          <v-btn icon large @click="upload()">
            <v-icon color="green">mdi-plus</v-icon>
          </v-btn>
          <br />
          <v-label>{{ placeholder }}</v-label>
        </v-col>
      </v-row>
    </v-container>
    <input
      ref="upload"
      type="file"
      @change="preview_image($event)"
      accept="image/*"
      style="display: none"
    />
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
      default: ""
    },
    placeholder: {
      type: String,
      default: "upload image"
    },
    icon: {
      type: String,
      default: "mdi-camera"
    },
    readonly: {
      type: Boolean,
      default: false
    },
    multiple: {
      type: Boolean,
      default: false
    },
    aspectRatio: {
      type: String,
      default: "1.78"
    },
    img: Array,
    width: String,
    height: String
  },
  data: function() {
    return {
      //img: [],
      img_style: {
        width: this.width,
        height: this.height
      }
    };
  },
  methods: {
    preview_image(src) {
      var file = src.target.files[0];
      let that = this;
      let reader = new FileReader();

      if (file) {
        reader.readAsDataURL(file);
      }

      reader.onload = function() {
        that.img.push(this.result);
        that.$emit("change", that.img);
      };
    },
    delete_image(index) {
      this.img.splice(index, 1);
      this.$emit("change", this.img);
    },
    check_create() {
      return !this.readonly && !(this.img.length >= 1 && !this.multiple);
    },
    upload() {
      let btn = this.$refs.upload;
      btn.click();
    },
    reset() {
      this.img.splice(0, this.img.length);
      this.$emit("change", this.img);
    },
	test() {
	  console.log("here test image uploader");
	  console.log(this.img);
	}
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.image-uploader {
  margin: auto;
}
.create {
  margin: auto;
  padding: auto;
  border: 2px dashed green;
}
</style>
