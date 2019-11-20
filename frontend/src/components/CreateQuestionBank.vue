<template>
  <div>
    <v-card id="create-form">
      <v-toolbar color="primary" dark elevation="0" dense>
        <v-toolbar-title>Create a Question Bank</v-toolbar-title>
      </v-toolbar>
      <v-card-text>
        <v-form ref="form" v-model="valid">
          <v-row>
            <v-col>
              <v-text-field
                v-model="name"
                :rules="name_rules"
                hint="The name of the question bank"
                label="Name"
                outlined
                required
              ></v-text-field>
              <v-select
                :items="authorities"
                label="Authorities"
                v-model="authority"
                outlined
              ></v-select>
              <v-text-field
                v-if="authority == 'private'"
                v-model="invitation_code_count"
                label="Invite code number"
                :rules="invite_code_rules"
                hint="Number of invite code you want create(can be changed later)"
                outlined
              ></v-text-field>
            </v-col>
            <v-col>
              <image-uploader
                ref="uploader"
                v-model="image"
                label="Avatar"
                placeholder="Pick an avatar(optional)"
              />
            </v-col>
          </v-row>

          <v-textarea
            v-model="brief"
            :rules="brief_rules"
            hint="Brief introduction of the question bank"
            counter="200"
            label="Brief"
            auto-grow
            outlined
            required
          ></v-textarea>
          <v-layout class="mt-2">
            <v-spacer></v-spacer>
            <v-btn class="mr-4 cancel-button" text @click="reset()"
              >Reset</v-btn
            >
            <v-btn color="primary" :disabled="!valid" outlined @click="create()"
              >Create</v-btn
            >
          </v-layout>
        </v-form>
      </v-card-text>
    </v-card>
  </div>
</template>

<script>
import ImageUploader from "../components/ImageUploader.vue";
import axios from "axios";
export default {
  name: "create-question-bank",
  components: {
    "image-uploader": ImageUploader
  },
  data: function() {
    return {
      valid: false,
      name: "",
      name_rules: [
        v => !!v || "name is required!",
        v => (!!v && v.length <= 200) || "Max 200 characters!"
      ],
      brief: "",
      brief_rules: [
        v => !!v || "brief introduction is required",
        v => (!!v && v.length <= 200) || "Max 200 characters!"
      ],
      authorities: ["private", "public"],
      authority: "",
      invitation_code_count: 0,
      invite_code_rules: [v => this.isInt(v) || "You should enter an integer!"],
      image: []
    };
  },
  methods: {
    create() {
      let that = this;
      const headers = {
        Authorization: "Token " + this.$store.state.user.token
      };
      axios
        .post("/api/question_banks/", {
          id: -1,
          name: this.name,
          picture: this.image.length == 0 ? "" : this.image[0],
          brief: this.brief,
          authority: this.authority,
          invitation_code_count: this.invitation_code_count
        }, {headers: headers})
        .then(response => {
          alert("Success!");
          that.$router.push("questionbanks/" + response.data.id);
        })
        .catch(error => {
          alert(error);
        });
    },
    reset() {
      this.$refs.form.reset();
      this.$refs.uploader.reset();
    },
    isInt(target) {
      var regInt = /^[0-9]+$/;
      return regInt.test(target);
    }
  }
};
</script>
