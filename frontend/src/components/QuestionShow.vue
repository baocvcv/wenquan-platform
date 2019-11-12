<template>
    <v-card>
        <v-card-title>
            <slot name="title">{{ question_data.question_name }}</slot>
        </v-card-title>
        <v-list>
            <slot name="content">
                <v-list-item>
                    {{ question_data.question_content }}
                </v-list-item>
                <v-list-item v-if="question_data.question_img && question_data.question_img.length > 0">
                    <image-uploader
                        v-model="question_data.question_img"
                        readonly
                    ></image-uploader>
                </v-list-item>
            </slot>
            <slot name="answer"></slot>
            <slot name="score"></slot>
            <slot name="comment"></slot>
            <slot name="button"></slot>
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