<template>
<div id="question-bank">
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
                    <v-text-field
                        label="Name"
                        :readonly="!edit_mode"
                        outlined
                        v-model="edited_question_bank.name"
                    ></v-text-field>
                    <v-row>
                        <v-col>
                            <v-text-field
                                label="Created Time"
                                :readonly="true"
                                outlined
                                v-model="edited_question_bank.createTime"
                            >
                            </v-text-field>
                        </v-col>
                        <v-col>
                            <v-text-field
                                label="Last Update"
                                :readonly="true"
                                outlined
                                v-model="edited_question_bank.lastUpdate"
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
                    <v-row>
                        <v-col>
                            <v-text-field
                                label="Invitation Code Count"
                                v-model="question_bank.invitation_code_count"
                                :readonly="true"
                                outlined
                                hint="The total count of the invitation code"
                            >
                            </v-text-field>
                        </v-col>
                        <v-col>
                            <v-text-field
                                label="Invitation Code Count"
                                v-model="question_bank.activated_code_count"
                                :readonly="true"
                                outlined
                                hint="The total count of the invitation code"
                            >
                            </v-text-field>
                        </v-col>
                    </v-row>
                </v-col>
                <v-col>
                    <span class="grey--text caption">Picture</span>
                    <image-uploader
                        v-model="edited_question_bank_image"
                        :readonly="!edit_mode"
                        placeholder="No picture"
                    >
                    </image-uploader>
                </v-col>
            </v-row>
        </v-card-text>
        <v-expand-transition>
            <v-card-actions v-show="edit_mode">
                <div class="flex-grow-1"></div>
                <v-btn color="blue darken-1" text @click="cancel">Cancel</v-btn>
                <v-btn color="blue darken-1" text @click="save">Save</v-btn>
            </v-card-actions>
        </v-expand-transition>
    </v-card>
    <question-list v-if="question_bank.id" :id="question_bank.id" :editable="true"></question-list>
</div>
</template>

<script>
import question_list from "@/components/QuestionList.vue";
import image_uploader from "@/components/ImageUploader.vue";

export default {
    name: "question-bank",
    components: {
        "question-list": question_list,
        "image-uploader": image_uploader
    },
    data: () => ({
        question_bank: {},
        edited_question_bank: {},
        edit_mode: false,
        question_bank_image: [],
        edited_question_bank_image: []
    }),
    beforeRouteLeave (to, from, next) {
        if (this.edit_mode === true)
        {
            const answer = window.confirm("You have changes that are not saved. Are you sure you want to leave the web page?");
            if (answer) {
                next()
            } else {
                next(false)
            }
        }
    },
    methods: {
        cancel() {
            this.edit_mode = false;
            this.edited_question_bank = Object.assign({}, this.question_bank);
            this.edited_question_bank_image = JSON.parse(JSON.stringify(this.question_bank_image));
        },
        save() {
            this.edited_question_bank.picture = this.edited_question_bank_image[0];
            this.$axios
                .put('/api/question_banks/' + this.question_bank.id + '/', this.edited_question_bank)
                .then((response) => {
                    this.edit_mode = false;
                    this.quesion_bank = Object.assign({}, this.edited_question_bank);
                })
                .catch((error) => {
                    console.log(error);
                })
        }
    },
    created() {
        let id = this.$route.params.id;
        this.$axios
            .get('/api/question_banks/' + id + '/')
            .then(response => {
                this.question_bank = response.data;
                this.edited_question_bank = response.data;
                this.question_bank_image.push(this.question_bank.picture);
                this.edited_question_bank_image = JSON.parse(JSON.stringify(this.question_bank_image));
            })
            .catch((error) => {
                console.log(error);
            })
    },
}
</script>