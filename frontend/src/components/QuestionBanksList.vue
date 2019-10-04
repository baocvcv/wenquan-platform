<template>
  <div>
    <v-list two-line>
      <v-list-item
        v-for="qst_bank in question_banks"
        :key="qst_bank.name"
        @click="redirct('/questionbanks/' + qst_bank.id)"
      >
        <v-list-item-avatar>
          <v-icon v-text="qst_bank.icon"></v-icon>
        </v-list-item-avatar>

        <v-list-item-content align="left">
          <v-list-item-title v-text="qst_bank.name"></v-list-item-title>
          <v-list-item-subtitle v-text="qst_bank.brief"></v-list-item-subtitle>
        </v-list-item-content>

        <v-list-item-action @click.stop="">
          <v-btn
            icon
            @click="
              detail = true;
              cur_qst_bank = qst_bank;
            "
          >
            <v-icon color="grey lighten-1">mdi-information</v-icon>
          </v-btn>
        </v-list-item-action>
      </v-list-item>
    </v-list>

    <!--detailed infomation for question banks-->
    <v-dialog v-model="detail" max-width="500">
      <v-list subheader>
        <v-subheader inset>details of {{ cur_qst_bank.name }}</v-subheader>

        <v-list-item v-for="(value, attr) in cur_qst_bank.details" :key="attr">
          <v-list-item-content>
            {{ attr }}: {{ cur_qst_bank.details[attr] }}
          </v-list-item-content>
        </v-list-item>
      </v-list>
      <v-btn color="primary" dark @click="detail = false">Back</v-btn>
    </v-dialog>
  </div>
</template>

<script>
export default {
  name: "",
  props: {
    question_banks: {}
  },
  data: function() {
    return {
      detail: false,
      cur_qst_bank: {}
    };
  },
  methods: {
    redirct(path) {
      this.$router.replace(path);
    }
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped></style>
