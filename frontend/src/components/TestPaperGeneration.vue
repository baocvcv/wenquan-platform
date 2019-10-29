<template>
  <div>
    <v-form v-model="valid">
      <v-text-field
        v-model="name"
        :rules="name_rules"
        hint="The name of the test paper"
        label="Name"
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
        <v-list-item-group v-for="(body, key) in sections" :key="key">
          <v-list-item>
            <v-list-item-avatar>
              <v-icon>{{ roman(key + 1) }}</v-icon>
            </v-list-item-avatar>
          </v-list-item>
        </v-list-item-group>
        <v-btn
          class="mx-2"
          block
          tile
          dark
          color="green"
          @click="create_section()"
          >Create new</v-btn
        >
      </v-list>
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
      name: "",
      name_rules: [v => !!v || "Name is required!"],
      total_points: "",
      total_points_rules: [
        v => !!v || "Total points is required!",
        v => (!!v && /^[0-9]+$/.test(v)) || "An integer is expected!"
      ],
      tips: "",
      sections: []
    };
  },
  methods: {
    create_section() {
      this.sections.push({
        name: "",
        total_points: "",
        questions: []
      });
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
  },
  components: {}
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped></style>
