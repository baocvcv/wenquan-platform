<template>
  <test-view>
    <template v-slot:comment="{ paper_data }">
	  <paper-marking :paper_record_id="$route.params.id" :paper_data="paper_data"/>
	</template>
  </test-view>
</template>

<script>
import PaperMarking from "@/components/PaperMarking.vue";
import TestView from "@/views/Test.vue";
export default {
  name: "test-paper-marking",
  components: {
	"paper-marking": PaperMarking,
	"test-view": TestView
  },
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped></style>

