<template>
    <div id="question-banks">
        <v-card>
            <v-card-text>
                <v-tabs vertical>
                    <v-tab>
                        <v-icon left>mdi-earth</v-icon>
                        Explore
                    </v-tab>
                    <v-tab>
                        <v-icon left>mdi-account</v-icon>
                        MyBank
                    </v-tab>
                    <v-tab-item>
                        <question-banks-list :flat="true" :readonly="true" title="Explore Your Favourite Question Banks"></question-banks-list>
                    </v-tab-item>
                    <v-tab-item>
                        <h1 class="text--center display-4">Developing...</h1>
                    </v-tab-item>
                </v-tabs>
            </v-card-text>
        </v-card>
    </div>
</template>

<script>
import QuestionBanksList from "@/components/QuestionBanksList.vue";

export default {
    name: "question-banks",
    components: {
        "question-banks-list": QuestionBanksList
    }
}
</script>