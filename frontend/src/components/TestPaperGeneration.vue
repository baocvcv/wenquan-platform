<template>
  <div>
    <v-form v-model="valid">
      <v-text-field
        v-model="title"
        :rules="title_rules"
        hint="The title of the test paper"
        label="Title"
        outlined
        required
      ></v-text-field>
      <v-text-field
        v-model="total_points"
        :rules="total_points_rules"
        label="Total points"
        outlined
        required
      ></v-text-field>
      <v-textarea
        v-model="tips"
        hint="Tips provided to students(optional)"
        label="Tips"
        auto-grow
        outlined
      ></v-textarea>
      <v-list>
        <v-list-item-group v-for="(section, key) in sections" :key="key">
          <v-list-item>
            <v-list-item-avatar>
              <v-icon>{{ roman(key + 1) }}</v-icon>
            </v-list-item-avatar>
            <v-list-item-content>
              <v-row align="center">
              <v-col cols="12" xs="6" lg="4">
              <v-text-field
                v-model="section.title"
                label="Title"
                :rules="title_rules"
              ></v-text-field>
              </v-col>
              <v-col cols="12" xs="3" lg="2">
              <v-text-field
                v-model="section.total_points"
                label="Total points"
                :rules="total_points_rules"
              ></v-text-field>
              </v-col>
              <v-col cols="12" xs="3" lg="2">
                <v-label>points</v-label>
              </v-col>
              </v-row>
            </v-list-item-content>
            <v-list-item-action>
              <v-tooltip top>
                <template v-slot:activator="{ on }">
                  <v-btn
                    icon
                    v-on="on"
                    @click.stop="adding_question = true"
                  ><v-icon color="green" dark>mdi-plus</v-icon>
                  </v-btn>
                </template>
                <span>Add question</span>
              </v-tooltip>
            </v-list-item-action>
            <v-list-item-action>
              <v-tooltip top>
                <template v-slot:activator="{ on }">
                  <v-btn
                    icon
                    v-on="on"
                    @click.stop="drop_section(key)"
                  ><v-icon color="red" dark>mdi-trash-can-outline</v-icon>
                  </v-btn>
                </template>
                <span>remove</span>
              </v-tooltip>
            </v-list-item-action>
          </v-list-item>
        </v-list-item-group>
        <v-list-item>
        <v-list-item-content>
        <v-btn
          class="mx-2"
          block
          tile
          dark
          color="green"
          @click="create_section()"
          >Create new</v-btn
        >
        </v-list-item-content>
        </v-list-item>
      </v-list>
    </v-form>
	<!--The dialog is for selecting questions-->
    <v-dialog
      v-model="adding_question"
      fullscreen
      hide-overlay
      transition="dialog-bottom-transition"
    >
      <v-card>
        <v-toolbar>
          <v-btn icon @click="adding_question = false">
            <v-icon>mdi-arrow-left</v-icon>
          </v-btn>
          <v-toolbar-title>Selecting {{ process }}</v-toolbar-title>
        </v-toolbar>
		<question-banks-list v-if="process == 'question bank'" />
		<question-list v-if="process == 'question'" />
      </v-card>
    </v-dialog>
  </div>
</template>

<script>
import QuestionBanksList from "@/components/QuestionBanksList.vue";
import QuestionList from "@/components/QuestionList.vue";
export default {
  name: "",
  props: {},
  components: {
	"question-banks-list": QuestionBanksList,
	"question-list": QuestionList
  },
  data: function() {
    return {
      valid: false,
      title: "",
      title_rules: [v => !!v || "Title is required!"],
      total_points: "",
      total_points_rules: [
        v => !!v || "Total points is required!",
        v => (!!v && /^[0-9]+$/.test(v)) || "An integer is expected!"
      ],
      tips: "",
      sections: [],
      adding_question: false,
	  process: "question bank"
    };
  },
  methods: {
    create_section() {
      this.sections.push({
        title: "",
        total_points: "",
        questions: []
      });
    },
    drop_section(index) {
      this.sections.splice(index, 1);
    },
    roman(num) {
      var n,
        m,
        str = "",
        i = 1000;
      for (; i > 0; i /= 10) {
        n = Math.floor(num / i); //向下取整
        m = n;
        switch (i) {
          case 1000: {
            if (m > 0) str += "M".repeat(n);
            num -= n * i; //减去
            break;
          }
          case 100: {
            if (n == 9) {
              str += "CM";
              m -= 9;
            }
            if (m >= 5) {
              str += "D";
              m -= 5;
            }
            if (m == 4) {
              str += "CD";
              m -= 4;
            }
            if (m > 0) str += "C".repeat(m);
            num -= n * i;
            break;
          }
          case 10: {
            if (n == 9) {
              str += "XC";
              m -= 9;
            }
            if (m >= 5) {
              str += "L";
              m -= 5;
            }
            if (m == 4) {
              str += "XL";
              m -= 4;
            }
            if (m > 0) str += "X".repeat(m);
            num -= n * i;
            break;
          }
          case 1: {
            if (n == 9) {
              str += "IX";
              m -= 9;
            }
            if (m >= 5) {
              str += "V";
              m -= 5;
            }
            if (m == 4) {
              str += "IV";
              m -= 4;
            }
            if (m > 0) str += "I".repeat(m);
            num -= n * i;
            break;
          }
        }
      }
      return str;
    }
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped></style>
