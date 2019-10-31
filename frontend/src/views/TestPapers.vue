<template>
  <div>
    <v-card>
      <v-toolbar flat color="primary" dark>
        <v-toolbar-title>Test Papers</v-toolbar-title>
      </v-toolbar>

      <v-tabs vertical>
        <v-tab align="left">
          <v-icon>mdi-book-open</v-icon>
          Browse
        </v-tab>
        <v-tab align="left" :disabled="read_only">
          <v-icon>mdi-folder-plus</v-icon>
          Create
        </v-tab>

        <v-tab-item>
          <h1>developing...</h1>
		</v-tab-item>
        <v-tab-item>
		  <br />
          <test-paper-generation />
		</v-tab-item>
      </v-tabs>
    </v-card>  
  </div>
</template>

<script>
import TestPaperGeneration from "@/components/TestPaperGeneration.vue";
export default {
  name: "test-papers",
  props: {
  },
  components: {
	"test-paper-generation": TestPaperGeneration
  },
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped></style>

