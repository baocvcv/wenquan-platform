<template>
  <div id="create-auth-code-card">
    <v-card min-width="100px" min-height="100px">
      <v-card-text>
        <v-form v-model="valid" ref="form">
          <p>How many codes do you want to generate?</p>
          <v-text-field
            v-model="number"
            :rules="[v => !!v || 'The number of codes is required.']"
          >
          </v-text-field>
          <p>What's the length of the code?</p>
          <v-text-field
            label="Length"
            v-model="length"
            placeholder="10"
          ></v-text-field>
          <v-row>
            <v-spacer></v-spacer>
            <v-btn outlined :disabled="!valid" @click="submit">Submit</v-btn>
            <v-spacer></v-spacer>
          </v-row>
        </v-form>
      </v-card-text>
    </v-card>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "create-auth-code-card",
  props: {
    bankID: {
      type: Number,
      default: -1
    }
  },
  data: function() {
    return {
      valid: false,
      number: "",
      length: ""
    };
  },
  methods: {
    submit() {
      const post = {
        question_bank_id: this.bankID,
        num: Number(this.number),
        length: Number(this.length)
      };
      axios.post("/api/auth_code/", post).then(response => {
        this.$refs["form"].reset();
        this.$emit("add-auth-code", response.data);
      });
    }
  }
};
</script>
