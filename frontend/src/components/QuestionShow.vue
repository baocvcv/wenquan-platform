<template>
    <v-card>
        <v-card-title>
            <slot name="title" :question_data="question_data">{{ question_data.question_name }}</slot>
        </v-card-title>
        <v-list>
            <slot name="content" :question_data="question_data">
                <v-list-item>
                    {{ question_data.question_content }}
                </v-list-item>
            </slot>
            <slot name="image">
                <v-list-item v-if="question_data.question_image && question_data.question_image.length > 0">
                    <v-row justify="center">
                        <v-col cols="12" lg="4" md="6">
                            <image-uploader
                                width=100%
                                v-model="question_data.question_image"
                                readonly
                            ></image-uploader>
                        </v-col>
                    </v-row>
                </v-list-item>
            </slot>
            <slot name="answer" :question_data="question_data"></slot>
            <slot name="score" :question_data="question_data"></slot>
            <slot name="comment" :question_data="question_data"></slot>
            <slot name="button" :question_data="question_data"></slot>
        </v-list>
    </v-card>
</template>

<script>
import axios from "axios";
import ImageUploader from "./ImageUploader.vue";

export default {
    name: "question-show",
    props: {
        id: {
            type: Number,
            default: null
        }
    },
    components: {
        "image-uploader": ImageUploader
    },
    data: function() {
        return {
            question_data: {
                question_name: "Loading...",
                question_content: ""
            }
        };
    },
    created() {
        if(this.id)
            axios.get("/api/questions/" + this.id + "/")
                .then(response => {
                    this.question_data = response.data;
                })
                .catch(err => {
                    this.question_data = {
                        question_name: "Error!",
                        question_content: err.toString()
                    }
                });
    }
}
</script>