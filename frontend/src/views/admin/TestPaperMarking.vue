<template>
  <v-card>
  Oh shit
    <v-card-text>
	  <paper-marking />
	</v-card-text>
  </v-card>
</template>

<script>
import PaperMarking from "@/components/PaperMarking.vue"
export default {
  name: "test-paper-marking",
  props: {
  },
  components: {
	"paper-marking": PaperMarking
  },
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped></style>

