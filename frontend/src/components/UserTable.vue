<template>
<div>
      <v-data-table
        :headers="headers"
        :items="users"
      >
        <template v-slot:items="props">
        </template>
      </v-data-table>
</div>
</template>

<script>
export default {
    name: "user-table",
    components: {
    },
    props: {
        users: Array
    },
    data: function() {
        return {
            headers: [
                {
                    text: "Username",
                    align: "center",
                    value: "name"
                },
                {
                    text: "Last login time",
                    value: "last_login_time",
                    align: "center"
                },
                {
                    text: "IP",
                    value: "ip",
                    align: "center"
                },
                {
                    text: "Type",
                    value: "type",
                    align: "center"
                },
                {
                    text: "Actions",
                    value: "",
                    align: "center",
                    sortable: false
                }
            ]
        }   
    }
}
</script>