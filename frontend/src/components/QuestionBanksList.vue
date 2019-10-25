<template>
  <div>
    <h4 v-if="process != 'End'" align="center" style="color: grey;">
      {{ process }}
    </h4>
    <v-list two-line>
      <v-list-item
        v-for="qst_bank in question_banks"
        :key="qst_bank.name"
        @click="$router.push('questionbanks/' + qst_bank.id)"
      >
        <v-list-item-avatar>
          <v-img :src="qst_bank.icon"></v-img>
        </v-list-item-avatar>

        <v-list-item-content align="left">
          <v-list-item-title v-text="qst_bank.name"></v-list-item-title>
          <v-list-item-subtitle v-text="qst_bank.brief"></v-list-item-subtitle>
        </v-list-item-content>

        <v-list-item-action
          @click.stop="
            detail = true;
            cur_qst_bank = qst_bank;
          "
        >
          <v-hover v-slot:default="{ hover }">
            <v-btn v-if="hover" color="blue" icon>detail</v-btn>
            <v-btn v-else icon>
              <v-icon color="grey lighten-1">mdi-information</v-icon>
            </v-btn>
          </v-hover>
        </v-list-item-action>

        <v-list-item-action
          v-bind:style="read_only ? 'display:none' : ''"
          @click.stop="
            show_del_dialog = true;
            cur_qst_bank = qst_bank;
          "
        >
          <v-hover v-slot:default="{ hover }">
            <v-btn v-if="hover" color="red" icon>delete</v-btn>
            <v-btn v-else icon><v-icon>mdi-trash-can-outline</v-icon></v-btn>
          </v-hover>
        </v-list-item-action>
      </v-list-item>
    </v-list>

    <!--detailed infomation for question banks-->
    <v-dialog v-model="detail" max-width="500">
      <v-card>
        <v-toolbar flat color="blue" dark>
          <v-toolbar-title>
            Details of {{ cur_qst_bank.name }}
          </v-toolbar-title>
        </v-toolbar>
        <v-card-text>
          <v-list>
            <v-list-item
              v-for="(value, attr) in cur_qst_bank.details"
              :key="attr"
            >
              <v-list-item-content>
                {{ attr }}: {{ cur_qst_bank.details[attr] }}
              </v-list-item-content>
            </v-list-item>
          </v-list>
        </v-card-text>
        <v-card-actions>
          <div class="flex-grow-1"></div>
          <v-btn
            color="green"
            dark
            @click="$router.push('questionbanks/' + cur_qst_bank.id)"
          >
            Goto
          </v-btn>
          <v-btn color="primary" dark @click="detail = false">Back</v-btn>
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
          Are you sure to delete this question bank({{ cur_qst_bank.name }})?
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
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "question-banks-list",
  props: {
    question_banks: {},
    read_only: Boolean(true),
    process: {
      type: String,
      default: "End"
    }
  },
  data: function() {
    return {
      detail: false,
      show_del_dialog: false,
      cur_qst_bank: {}
    };
  },
  methods: {
    delete_qst_bank() {
      let that = this;
      axios
        .post("/api/question_banks/" + that.cur_qst_bank.id + "/", {
          id: that.cur_qst_bank.id
        })
        .catch(error => {
          alert(error);
        });
    }
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped></style>
