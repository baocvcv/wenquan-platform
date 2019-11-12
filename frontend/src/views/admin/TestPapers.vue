<template>
  <div>
    <v-card>
      <test-papers-list title="Test Papers" />
    </v-card>
  </div>
</template>

<script>
import TestPapersList from "@/components/TestPapersList.vue";
export default {
  name: "test-papers",
  props: {},
  components: {
    "test-papers-list": TestPapersList
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped></style>
