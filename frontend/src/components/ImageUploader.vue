<template>
  <div class="image-uploader" :style="img_style">
    <v-card outlined v-show="!tool">
      <v-card-text v-if="!!label">
        {{ label }}
      </v-card-text>
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
            <v-img
              v-if="/^\/media\/pictures\/.*?/.test(image)"
              :aspect-ratio="aspectRatio"
              :src="image"
              contain
            />
            <v-btn v-if="!readonly" icon @click="delete_image(i)">
              <v-icon color="red">mdi-delete</v-icon>
            </v-btn>
          </v-col>
          <v-col v-if="check_create() && !loading" align="center">
            <v-btn icon large @click="upload()">
              <v-icon color="green">mdi-plus</v-icon>
            </v-btn>
            <br />
            <v-label>{{ placeholder }}</v-label>
          </v-col>
          <v-col v-if="loading" align="center">
            <v-progress-circular
              indeterminate
              color="primary"
            ></v-progress-circular>
            <br />
            <v-label>Uploading ... </v-label>
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
    </v-card>

    <v-dialog v-model="not_an_image" max-width="250px">
      <v-card>
        <v-toolbar>
          <v-toolbar-title>Error</v-toolbar-title>
        </v-toolbar>
        <v-card-text align="center">
          <v-row justify="center">
            <v-col cols="12">
              <v-icon x-large color="error">mdi-information</v-icon>
            </v-col>
            <v-col cols="12">
              <span>Not an image!</span>
            </v-col>
          </v-row>
        </v-card-text>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn text @click="not_an_image = false">Close</v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </div>
</template>

<script>
import axios from "axios";
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
    img: {
      type: Array,
      default: () => []
    },
    tool: {
      type: Boolean,
      default: false
    },
    width: String,
    height: String
  },
  data: function() {
    return {
      loading: false,
      not_an_image: false,
      img_style: {
        width: this.width,
        height: this.height
      }
    };
  },
  methods: {
    preview_image(src) {
      this.$emit("upload-start");
      this.loading = true;
      var file = src.target.files[0];
      let that = this;
      let reader = new FileReader();

      if (file) {
        reader.readAsDataURL(file);
      }

      reader.onload = async function() {
        if (/^data:image.*?base64/.test(this.result)) {
          let formData = new FormData();
          formData.append("imagefile", file);
          const headers = {
            Authorization: "Token " + this.$store.state.user.token
          };
          var url = await axios
            .post("/api/upload/image/", formData, {headers: headers})
            .catch(error => {
              alert(error);
              that.loading = false;
            });
          url = url.data.url;
          that.img.push(url);
          that.$emit("change", that.img);
          that.$emit("upload-finish", url);
        } else {
          that.not_an_image = true;
        }
        that.loading = false;
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
