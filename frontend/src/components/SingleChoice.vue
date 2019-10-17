<template>
  <div>
    <v-form ref="single-choice" v-model="valid">
      <v-text-field
        label="Title"
        v-model="question_name"
        outlined
      ></v-text-field>
      <v-textarea
        label="Content"
        v-model="question_content"
        :rules="[v => !!v || 'Question content is required!']"
        auto-grow
        outlined
        required
      ></v-textarea>
      <v-list>
        <v-subheader>Choices</v-subheader>
        <v-list-item-group color="primary">
          <v-list-item
            v-for="(choice, i) in question_choice"
            :key="i"
            :style="question_ans == choice ? 'background-color: #B3E5FC;' : ''"
          >
            <v-list-item-icon>{{ choice.name }}</v-list-item-icon>
            <v-text-field
              v-model="choice.content"
              placeholder="Enter content"
            ></v-text-field>
            <v-tooltip top>
              <template v-slot:activator="{ on }">
                <v-btn icon small @click="check_ans(choice)" v-on="on"
                  ><v-icon :color="question_ans == choice ? 'green' : ''" dark
                    >mdi-check</v-icon
                  ></v-btn
                >
              </template>
              <span>select as right answer</span>
            </v-tooltip>
            <v-tooltip top>
              <template v-slot:activator="{ on }">
                <v-btn icon small @click="delete_choice(i)" v-on="on"
                  ><v-icon dark>mdi-minus</v-icon></v-btn
                >
              </template>
              <span>remove</span>
            </v-tooltip>
          </v-list-item>
        </v-list-item-group>
        <v-btn
          class="mx-2"
          block
          tile
          flat
          dark
          color="green"
          @click="choice_num_up()"
          >create new</v-btn
        >
      </v-list>
      <br />
      <v-textarea
        label="Analyse"
        v-model="question_solution"
        :rules="[v => !!v || 'Analyse is required!']"
        auto-grow
        outlined
        required
      ></v-textarea>
    </v-form>
  </div>
</template>

<script>
export default {
  name: "",
  props: {},
  data: function() {
    return {
      valid: false,
      question_name: "",
      question_content: "",
      question_image: [],
      question_choice: [],
      question_ans: "",
      question_solution: ""
    };
  },
  methods: {
    choice_num_up() {
      let choice_num = this.question_choice.length;
      this.question_choice.push({
        name: String.fromCharCode(choice_num + 65),
        content: ""
      });
    },
    delete_choice(index) {
      if (this.question_ans == this.question_choice[index]) {
        this.question_ans = undefined;
      }
      this.question_choice.splice(index, 1);
      for (var i = 0; i < this.question_choice.length; i++) {
        this.question_choice[i].name = String.fromCharCode(65 + i);
      }
    },
    check_ans(choice) {
      this.question_ans = this.question_ans == choice ? undefined : choice;
    }
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped></style>
