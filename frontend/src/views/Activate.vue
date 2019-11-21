<template>
  <div id="activate">
    <v-container fluid fill-height>
      <v-row :align="'center'">
        <v-col>
          <div v-if="activated">
            <h1 class="text-center display-4 font-weight-bold">
              Successfully activated!
            </h1>
            <p class="body-1 text-center mt-10">
              Your account You will be redirected to the homepage automatically
              after
              {{ timelag }} seconds, or you can click
              <router-link to="/sigin">this link</router-link> to immediately
              switch to the signin page.
            </p>
          </div>
        </v-col>
      </v-row>
    </v-container>
  </div>
</template>

<script>
import axios from "axios";
export default {
  name: "activate",
  data: function() {
    return {
      activated: null,
      timelag: 3
    };
  },
  created() {
    axios
      .post(
        "/api/verification/",
        { token: this.$route.params.token },
      )
      .then(response => {
        this.activated = true;
        setTimeout(() => {
          this.$router.push("/signin");
        }, this.timelag * 1000);
      })
      .catch(error => {
        this.activated = false;
      });
  }
};
</script>
