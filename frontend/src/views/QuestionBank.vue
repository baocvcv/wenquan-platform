<template>
  <div id="question-bank">
    <vue-element-loading :active="loading" is-full-screen></vue-element-loading>
    <v-row>
      <v-col>
        <v-card v-show="!loading" style="height: 100%">
          <v-card-title
            >Profile
            <v-btn
              absolute
              right
              icon
              @click="edit_button_clicked"
              v-if="editable"
              ><v-icon>mdi-pencil</v-icon></v-btn
            >
          </v-card-title>
          <v-card-text>
            <v-row>
              <v-col cols="12" md="9">
                <v-text-field
                  label="Name"
                  :readonly="!edit_mode"
                  outlined
                  v-model="edited_question_bank.name"
                ></v-text-field>
                <v-row>
                  <v-col>
                    <v-text-field
                      label="Created Time"
                      :readonly="true"
                      outlined
                      v-model="edited_question_bank.createTime"
                    >
                    </v-text-field>
                  </v-col>
                  <v-col>
                    <v-text-field
                      label="Last Update"
                      :readonly="true"
                      outlined
                      v-model="edited_question_bank.lastUpdate"
                    >
                    </v-text-field>
                  </v-col>
                  <v-col>
                    <v-text-field
                      label="Question Count"
                      :readonly="true"
                      outlined
                      hint="How many questions there are in this question bank"
                      v-model="edited_question_bank.question_count"
                    >
                    </v-text-field>
                  </v-col>
                </v-row>
                <v-textarea
                  label="Brief"
                  :readonly="!edit_mode"
                  outlined
                  hint="A short brief for this question bank to help others identify it more easily"
                  v-model="edited_question_bank.brief"
                >
                </v-textarea>
              </v-col>
              <v-col>
                <span class="grey--text caption">Picture</span>
                <image-uploader
                  v-model="edited_question_bank_image"
                  :readonly="!edit_mode"
                  placeholder="No picture"
                >
                </image-uploader>
              </v-col>
            </v-row>
          </v-card-text>
          <v-expand-transition>
            <v-card-actions v-show="edit_mode">
              <div class="flex-grow-1"></div>
              <v-btn color="blue darken-1" text @click="cancel">Cancel</v-btn>
              <v-btn color="blue darken-1" text @click="save" :disabled="edited"
                >Save</v-btn
              >
            </v-card-actions>
          </v-expand-transition>
        </v-card>
      </v-col>
      <v-col cols="12" sm="4" md="4" v-if="editable">
        <v-card v-show="!loading" style="height: 100%">
          <v-card-title>
            Activation Code
            <v-menu
              bottom
              offset-y
              transition="slide-y-transition"
              :close-on-content-click="false"
            >
              <template v-slot:activator="{ on }">
                <v-btn right absolute icon color="primary" v-on="on"
                  ><v-icon>mdi-plus</v-icon></v-btn
                >
              </template>
              <create-auth-code-card
                :bankID="this.question_bank.id"
                @add-auth-code="add_auth_code"
              ></create-auth-code-card>
            </v-menu>
          </v-card-title>
          <v-card-text>
            <v-row>
              <v-col cols="12" md="6" class="pb-0">
                <v-text-field
                  label="Invitation Code Count"
                  v-model="invitation_code_count"
                  :readonly="true"
                  outlined
                >
                </v-text-field>
              </v-col>
              <v-col cols="12" md="6" class="pb-0">
                <v-text-field
                  label="Available Code Count"
                  v-model="available_code_count"
                  :readonly="true"
                  outlined
                >
                </v-text-field>
              </v-col>
            </v-row>
            <v-data-table
              :headers="[
                {
                  text: 'Availabe Codes',
                  align: 'left',
                  sortable: false,
                  value: 'code'
                }
              ]"
              :items="td_codes"
            ></v-data-table>
          </v-card-text>
        </v-card>
      </v-col>
    </v-row>
    <question-list
      v-show="!loading"
      v-if="question_bank.id"
      :editable="editable"
      :id="question_bank.id"
    ></question-list>
  </div>
</template>

<script>
import question_list from "@/components/QuestionList.vue";
import image_uploader from "@/components/ImageUploader.vue";
import axios from "axios";
import VueElementLoading from "vue-element-loading";
import CreateAuthCodeCard from "@/components/CreateAuthCodeCard.vue";

export default {
  name: "question-bank",
  components: {
    "question-list": question_list,
    "image-uploader": image_uploader,
    "vue-element-loading": VueElementLoading,
    "create-auth-code-card": CreateAuthCodeCard
  },
  data: () => ({
    question_bank: {
      id: null
    },
    edited_question_bank: {},
    edit_mode: false,
    question_bank_image: [],
    edited_question_bank_image: [],
    edited: false,
    loading: false,
    codes: [],
    invitation_code_count: null,
    available_code_count: null,
    editable: null
  }),
  computed: {
    td_codes() {
      let ret_codes = [];
      let index;
      for (index in this.codes) {
        ret_codes.push({ code: this.codes[index] });
      }
      return ret_codes;
    }
  },
  watch: {
    edited_question_bank: {
      handler: function() {
        if (this.edit_mode) this.edited = true;
      },
      deep: true
    },
    edited_question_bank_image: {
      handler: function() {
        if (this.edit_mode) this.edited = true;
      },
      deep: true
    },
    edit_mode() {
      this.edited = false;
    }
  },
  beforeRouteLeave(to, from, next) {
    if (this.edited === true) {
      const answer = window.confirm(
        "You have changes that are not saved. Are you sure you want to leave the web page?"
      );
      if (answer) {
        next();
      } else {
        next(false);
      }
    } else {
      next();
    }
  },
  methods: {
    add_auth_code(info) {
      this.codes = info.auth_code;
      this.invitation_code_count = info.total_num;
      this.available_code_count = info.valid_num;
    },
    cancel() {
      this.edit_mode = false;
      this.edited_question_bank = JSON.parse(
        JSON.stringify(this.question_bank)
      );
      this.edited_question_bank_image = JSON.parse(
        JSON.stringify(this.question_bank_image)
      );
    },
    save() {
      this.edited_question_bank.picture = this.edited_question_bank_image[0];
      axios
        .put(
          "/api/question_banks/" + this.question_bank.id + "/",
          this.edited_question_bank
        )
        .then(response => {
          this.edit_mode = false;
          this.question_bank = JSON.parse(
            JSON.stringify(this.edited_question_bank)
          );
          this.question_bank_image = JSON.parse(
            JSON.stringify(this.edited_question_bank_image)
          );
        })
        .catch(error => {
          console.log(error);
        });
    },
    edit_button_clicked() {
      if (this.edit_mode && this.edited) {
        let ans = window.confirm(
          "You have changes that are not saved. Are you sure you want to discard the changes?"
        );
        if (ans) this.cancel();
      } else {
        this.edit_mode = !this.edit_mode;
      }
    }
  },
  created() {
    let id = this.$route.params.id;
    this.loading = true;
    this.editable = this.$route.fullPath.search("/admin/") == -1 ? false : true;
    axios
      .get("/api/question_banks/" + id + "/")
      .then(response => {
        this.question_bank = response.data;
        this.edited_question_bank = JSON.parse(
          JSON.stringify(this.question_bank)
        );
        this.question_bank_image.push(this.question_bank.picture);
        this.edited_question_bank_image = JSON.parse(
          JSON.stringify(this.question_bank_image)
        );
        this.loading = false;
      })
      .catch(error => {
        console.log(error);
      });
    if (this.editable) {
      axios
        .post("/api/auth_code/", { question_bank_id: id })
        .then(response => {
          this.codes = response.data.auth_code;
          this.invitation_code_count = response.data.total_num;
          this.available_code_count = response.data.valid_num;
        })
        .catch(error => {
          console.log(error);
        });
    }
  }
};
</script>
