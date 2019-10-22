<template>
<div id="question-bank">
    <h1>{{ edited_question_bank.name }}</h1>
    <v-card>
        <v-card-title>Profile        
            <v-btn
                absolute
                right
                icon
                @click="edit_mode = !edit_mode"
            ><v-icon>mdi-pencil</v-icon></v-btn>
        </v-card-title>
        <v-card-text>
            <v-row>
                <v-col cols="12" md="9" sm="9">
                    <v-row>
                        <v-col>
                            <v-text-field
                                label="Created Time"
                                :readonly="true"
                                outlined
                                v-model="edited_question_bank.created_time"
                            >
                            </v-text-field>
                        </v-col>
                        <v-col>
                            <v-text-field
                                label="Last Update"
                                :readonly="true"
                                outlined
                                v-model="edited_question_bank.last_update"
                            >
                            </v-text-field>
                        </v-col>
                        <v-col>
                            <v-text-field
                                label="Question Count"
                                :readonly="true"
                                outlined
                                hint="How many questions there are in this question bank"
                                v-model="edited_question_bank.question_count"
                            >
                            </v-text-field>
                        </v-col>
                    </v-row>
                    <v-textarea
                        label="Brief"
                        :readonly="!edit_mode"
                        outlined
                        hint="A short brief for this question bank to help others identify it more easily"
                        v-model="edited_question_bank.brief"
                    >
                    </v-textarea>
                </v-col>
                <v-col>
                    <v-img></v-img>
                </v-col>
            </v-row>
        </v-card-text>
        <v-card-actions v-if="edit_mode">
            <div class="flex-grow-1"></div>
            <v-btn color="blue darken-1" text @click="cancel">Cancel</v-btn>
            <v-btn color="blue darken-1" text @click="save">Save</v-btn>
        </v-card-actions>
    </v-card>
    <question-list :editable="true"></question-list>
</div>
</template>

<script>
import question_list from "@/components/QuestionList.vue";

export default {
    name: "question-bank",
    components: {
        "question-list": question_list,
    },
    data: () => ({
        question_bank: {
            name: "Calclus",
            created_time: "2019-10-22",
            last_update: "2019-10-22",
            question_count: 1000,
            brief: "It is impossible to master CALCULUS."
        },
        edited_question_bank: {
            name: "",
            created_time: "",
            last_update: "",
            question_count: 0,
            brief: ""
        },
        edit_mode: false,
    }),
    beforeRouteLeave (to, from, next) {
        if (this.edit_mode === true)
        {
            confirm("You have changes that are not saved. Are you sure you want to leave the web page?");
        }
    },
    methods: {
        cancel() {
            this.edit_mode = false;
            this.edited_question_bank = Object.assign({}, this.question_bank);
        },
        save() {
            /*
            this.$axios
                .put('api/questionbanks/' + id + '/', this.edited_question_bank)
                .then((response) => {
                    this.edit_mode = false;
                    this.quesion_bank = Object.assign({}, this.edited_question_bank);
                })
                .catch((error) => {
                    console.log(error);
                })
            */
            this.edit_mode = false;
            this.question_bank = Object.assign({}, this.edited_question_bank);
        }
    },
    created() {
        let id = this.$route.params.id;
        /*
        this.$axios
            .get('api/questionbanks/' + id + '/')
            .then((response) => {
                this.question_bank = response.data;
            })
            .catch((error) => {
                console.log(error);
            })
        */
        this.edited_question_bank = Object.assign({}, this.question_bank);
    }
}
</script>