<template>
  <div id="admin">
    <h1 class="text-center">Welcome back, {{ $store.state.user.username }}.</h1>
  </div>
</template>

<script>
export default {
  name: "admin"
};
</script>
