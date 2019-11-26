<template>
  <div>
    <v-card :flat="flat">
      <v-toolbar flat>
        <v-toolbar-title>{{ title }}</v-toolbar-title>
        <v-spacer></v-spacer>
        <v-text-field
          flat
          hide-details
          label="Search"
          prepend-inner-icon="mdi-magnify"
          clearable
        ></v-text-field>
        <v-dialog v-model="create_bank_dialog" v-if="admin" max-width="600px">
          <template v-slot:activator="{ on }">
            <v-btn color="primary" elevation="0" class="ml-2" v-on="on">
              Create
            </v-btn>
          </template>
          <create-question-bank
            ref="create-question-bank"
          ></create-question-bank>
        </v-dialog>

        <v-dialog v-if="explore" v-model="activation_dialog" max-width="600px">
          <template v-slot:activator="{ on }">
            <v-btn color="primary" elevation="0" class="ml-2" v-on="on">
              Activate
            </v-btn>
          </template>
          <activation-card
            ref="activation-card"
            @activated="activated"
          ></activation-card>
        </v-dialog>
      </v-toolbar>
      <v-card-text class="pt-0">
        <vue-progress-bar style="position: relative;"></vue-progress-bar>
        <p
          class="caption grey--text text-right mt-0 mb-0 pr-1"
          transition="fade-transition"
        >
          {{ process }}
        </p>
        <v-list two-line>
          <v-list-item
            v-for="qst_bank in question_banks"
            :key="qst_bank.name"
            @click="
              select
                ? select_action(qst_bank.id)
                : $router.push('questionbanks/' + qst_bank.id)
            "
            class="pr-0"
          >
            <v-list-item-avatar>
              <v-img
                v-if="/^\/media\/pictures\/.*?/.test(qst_bank.icon)"
                :src="qst_bank.icon"
              ></v-img>
            </v-list-item-avatar>

            <v-list-item-content align="left">
              <v-list-item-title v-text="qst_bank.name"></v-list-item-title>
              <v-list-item-subtitle
                v-text="qst_bank.brief"
              ></v-list-item-subtitle>
            </v-list-item-content>

            <v-list-item-action
              @click.stop="
                detail = true;
                cur_qst_bank = qst_bank;
              "
            >
              <v-tooltip bottom>
                <template v-slot:activator="{ on }">
                  <v-hover v-slot:default="{ hover }">
                    <v-btn icon v-on="on">
                      <v-icon :color="hover ? 'primary' : 'grey lighten-1'"
                        >mdi-information</v-icon
                      >
                    </v-btn>
                  </v-hover>
                </template>
                <span>Details</span>
              </v-tooltip>
            </v-list-item-action>

            <v-list-item-action
              v-bind:style="!explore ? 'display:none' : ''"
              @click.stop="
                show_del_dialog = true;
                cur_qst_bank = qst_bank;
              "
            >
              <v-tooltip bottom>
                <template v-slot:activator="{ on }">
                  <v-hover v-slot:default="{ hover }">
                    <v-btn icon v-on="on">
                      <v-icon :color="hover ? 'error' : 'grey lighten-1'"
                        >mdi-trash-can-outline</v-icon
                      >
                    </v-btn>
                  </v-hover>
                </template>
                <span>Delete</span>
              </v-tooltip>
            </v-list-item-action>
          </v-list-item>
        </v-list>

        <!--detailed infomation for question banks-->
        <v-dialog v-model="detail" max-width="500">
          <v-card>
            <v-card-title> Details of {{ cur_qst_bank.name }} </v-card-title>
            <v-card-text class="mt-2">
              <v-container>
                <p v-for="(value, attr) in cur_qst_bank.details" :key="attr">
                  <v-row align="center">
                    <v-col class="mt-0 mb-0 pt-0 pd-0">
                      <span class="font-weight-bold">{{ attr }}:</span>
                    </v-col>
                    <v-col class="mt-0 mb-0 pt-0 pd-0">
                      <span>{{
                        attr.search("Time") == -1
                          ? cur_qst_bank.details[attr]
                          : new Date(cur_qst_bank.details[attr])
                      }}</span>
                    </v-col>
                  </v-row>
                </p>
              </v-container>
            </v-card-text>
            <v-card-actions>
              <div class="flex-grow-1"></div>
              <v-btn
                color="primary"
                v-if="!explore"
                outlined
                @click="
                  select
                    ? select_action(cur_qst_bank.id)
                    : $router.push('questionbanks/' + cur_qst_bank.id)
                "
              >
                View
              </v-btn>
              <v-btn
                color="primary"
                v-if="explore && cur_qst_bank.details.Authority == 'private'"
                outlined
              >
                Buy
              </v-btn>
              <v-btn
                color="primary"
                v-if="explore && cur_qst_bank.details.Authority == 'public'"
                outlined
                @click="add_to_my_bank(cur_qst_bank.id)"
              >
                Add
              </v-btn>
              <v-btn class="cancel-button" text @click="detail = false"
                >Done</v-btn
              >
              <div class="flex-grow-1"></div>
            </v-card-actions>
          </v-card>
        </v-dialog>

        <!--dialog for delete confirm-->
        <v-dialog v-model="show_del_dialog" max-width="300">
          <v-card>
            <v-toolbar flat color="warning" dark>
              <v-toolbar-title>
                Deletion confirmation
              </v-toolbar-title>
            </v-toolbar>
            <br />
            <v-card-text align="left" style="color: red;">
              Are you sure to delete this question bank({{
                cur_qst_bank.name
              }})?
            </v-card-text>
            <v-card-actions>
              <div class="flex-grow-1"></div>
              <v-btn
                color="error"
                dark
                @click="
                  delete_qst_bank();
                  show_del_dialog = false;
                "
                >Confirm
              </v-btn>
              <v-btn color="grey" dark @click="show_del_dialog = false">
                Cancel
              </v-btn>
              <div class="flex-grow-1"></div>
            </v-card-actions>
          </v-card>
        </v-dialog>
      </v-card-text>
    </v-card>
  </div>
</template>

<script>
import axios from "axios";
import CreateQuestionBank from "@/components/CreateQuestionBank.vue";
import ActivationCard from "@/components/ActivationCard.vue";

export default {
  name: "question-banks-list",
  props: {
    select: {
      type: Boolean,
      default: false
    },
    title: {
      type: String,
      default: ""
    },
    flat: {
      type: Boolean,
      default: false
    },
    explore: {
      type: Boolean,
      default: false
    },
    mybank: {
      type: Boolean,
      default: false
    },
    bankIDs: {
      type: Array,
      default: null
    },
    admin: {
      type: Boolean,
      default: true
    }
  },
  components: {
    "create-question-bank": CreateQuestionBank,
    "activation-card": ActivationCard
  },
  data: function() {
    return {
      detail: false,
      show_del_dialog: false,
      question_banks: [],
      cur_qst_bank: {
        details: {
          Authority: ""
        }
      },
      process: "",
      create_bank_dialog: false,
      activation_dialog: false
    };
  },
  methods: {
    load_question_banks(question_banks) {
      let that = this;
      let all_count = question_banks.length;
      let count = 0;
      let lock = false;
      that.$Progress.set(0);
      if (all_count === 0) {
        that.$Progress.finish();
        that.process = "Total Count: " + all_count;
      }
      const headers = {
        Authorization: "Token " + this.$store.state.user.token
      };
      for (var i = 0; i < question_banks.length; i++) {
        axios
          .get("/api/question_banks/" + question_banks[i] + "/", {
            headers: headers
          })
          .then(sub_response => {
            that.question_banks.push(that.parse(sub_response.data));
            while (lock);
            lock = true;
            count++;
            lock = false;
            that.process =
              "Loading question banks: " + count + " / " + all_count;
            that.$Progress.increase((1 / all_count) * 100);
            if (count == all_count) {
              that.process = "Total Count: " + all_count;
              that.$Progress.finish();
            }
          });
      }
    },
    delete_qst_bank() {
      let that = this;
      const headers = {
        Authorization: "Token " + this.$store.state.user.token
      };
      axios
        .delete("/api/question_banks/" + that.cur_qst_bank.id + "/", {
          headers: headers
        })
        .catch(error => {
          this.$notify({
            type: "error",
            title: "Failed to delete the bank"
          });
        });
    },
    select_action(id) {
      this.$emit("done-select", id);
    },
    activated(status) {
      if (status) this.activation_dialog = false;
      this.$emit("force-update");
    },
    parse(input) {
      var result = {
        id: input.id,
        name: input.name,
        brief: input.brief,
        icon: input.picture,
        details: {
          Authority: input.authority,
          "Create Time": input.createTime,
          "Last Updated Time": input.lastUpdate,
          Brief: input.brief,
          "Total Question Number": input.question_count,
          "Total Invite Code number": input.invitation_code_count,
          "Total Activated Code number": input.activated_code_count
        }
      };
      return result;
    },
    add_to_my_bank(bankID) {
      let user = this.$store.state.user;
      user.question_banks.push(bankID);
      const headers = {
        Authorization: "Token " + this.$store.state.user.token
      };
      axios
        .put("/api/accounts/users/" + user.id + "/", user, { headers: headers })
        .then(response => {
          this.$store.commit("updateUserWithKey", {
            key: "question_banks",
            value: user.question_banks
          });
          this.$emit("force-update");
          this.detail = false;
          this.$notify({
            type: "success",
            title: "Success",
            text:
              "The question bank has been added. You can find it in 'MYBANK' now. If you can not find it, please refresh the webpage."
          });
        })
        .catch(error => {
          this.$notify({
            type: "error",
            title: "Failed to add the bank."
          });
        });
    }
  },
  watch: {
    create_bank_dialog: function() {
      if (!this.create_bank_dialog) this.$refs["create-question-bank"].reset();
    },
    activation_dialog: function() {
      if (!this.activation_dialog) this.$refs["activation-card"].reset();
    },
    bankIDs() {
      let that = this;
      that.process = "Fetching data from server...";
      this.load_question_banks(this.bankIDs);
    }
  },
  mounted: function() {
    let that = this;
    that.process = "Fetching data from server...";
    if (!this.bankIDs) {
      const headers = {
        Authorization: "Token " + this.$store.state.user.token
      };
      axios
        .get("/api/question_banks/", { headers: headers })
        .then(response => {
          let question_banks = response.data;
          this.load_question_banks(question_banks);
        })
        .catch(error => {
          that.process = "Failed to access data: " + error;
          that.$notify({
            type: "error",
            title: "Failed to loa question banks."
          });
        });
    } else {
      this.load_question_banks(this.bankIDs);
    }
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped></style>
