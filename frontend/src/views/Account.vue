<template>
  <v-card>
    <v-card-title>
      Account
    </v-card-title>
    <v-card-text>
      {{ $store.state.user }}
    </v-card-text>
  </v-card>
</template>

<script>
export default {
  name: "account-view"
};
</script>
