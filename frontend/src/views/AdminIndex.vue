<template>
    <div>
        <user-list>
        </user-list>
    </div>
</template>

<script>
import user_list from "@/components/UserList.vue";

export default {
    name: "admin-index",
    components: {
        user_list
    }
}
</script>