<template>
  <div id="Error">
    <v-container fluid fill-height>
      <v-row :align="'center'">
        <v-col>
          <h1 class="text-center display-4 font-weight-bold">404 Not Found</h1>
          <p class="body-1 text-center mt-10">
            Oops, it seems that you are visiting a wrong web page. You will be
            redirected to the homepage automatically after
            {{ timelag }} seconds, or you can click
            <router-link to="/">this link</router-link> to immediately switch to
            the homepage.
          </p>
        </v-col>
      </v-row>
    </v-container>
  </div>
</template>

<script>
export default {
  name: "Error",
  mounted() {
    // BUGS here! The function in setTimeout will be triggerd even having left the view.
    setTimeout(() => {
      this.$router.push("/");
    }, this.timelag * 1000);
  },
  data: function() {
    return {
      timelag: 3
    };
  }
};
</script>
