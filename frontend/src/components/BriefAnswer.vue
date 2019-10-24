<template>
    <div class="brief-answer-component">
        <v-form ref="form" v-model="valid">
            <v-text-field label="Title" v-model="data.title" outlined :readonly="readonly"></v-text-field>
            <v-textarea 
                label="Content"
                v-model="data.content" 
                :rules="[v => !!v || 'Question content is required!']"
                outlined
                auto-grow
                :readonly="readonly"
            ></v-textarea>
            <br/>
			<image-uploader
			  ref="uploader"
			  v-model="data.image"
			  width="50%"
			  label="picture"
			  :readonly="readonly"
			  multiple
			  placeholder="Upload an image if necessary"
			></image-uploader>
			<br/>
            <v-textarea 
                label="Answer"
                v-model="data.answer" 
                :rules="[v => !!v || 'Answer is required!']"
                outlined
                auto-grow
                :readonly="readonly"
            ></v-textarea>
            <br/>
            <v-textarea 
                label="Analyse"
                v-model="data.analyse" 
                :rules="[v => !!v || 'Analyse is required!']"
                outlined
                auto-grow
                :readonly="readonly"
            ></v-textarea>
            <v-list-item>
                <span>Difficulty:</span>
                <v-rating
                    v-model="data.difficulty"
                    color="yellow darken-3"
                    background-color="grey darken-1"
                    :readonly="readonly"
                    half-increments
                    hover
                ></v-rating>
            </v-list-item>
            <v-btn
                class="mr-4"
                color="success"
                @click="submit()"
                :disabled="!canSubmit"
                v-if="!readonly"
            >
                Submit
            </v-btn>
            <v-btn
                class="mr-4"
                color="error"
                @click="reset()"
                v-if="!readonly"
            >
                Reset
            </v-btn>
        </v-form>
    </div>
</template>

<script>
import ImageUploader from "./ImageUploader.vue";
export default {
    name: "brief-answer",
	components: {
	  "image-uploader": ImageUploader
	},
    props: {
        readonly: {
            type: Boolean,
            default: false
        },
    },
    computed: {
        canSubmit() {
            return this.valid;
        }
    },
    methods: {
        submit() {
            this.$emit("submit",this.parse());
        },
        reset() {
            this.$refs.form.reset();
			this.$refs.uploader.reset();
        },
        updateData(input) {
            //parse data input from backend
            this.data.id = input.id;
            this.data.parents = input.parents_node;
            this.data.change_time = input.question_change_time;
            this.data.title = input.question_name;
            this.data.content = input.question_content;
			this.data.image = input.question_image;
            this.data.analyse = input.question_solution;
            this.data.difficulty = input.question_level;
            this.data.answer = input.question_ans;
        },
        parse() {
            let result = {
                id: this.data.id,
                parents_node: this.data.parents,
                question_change_time: this.data.change_time,
                question_name: this.data.title,
                question_type: "brief_ans",
                question_level: this.data.difficulty,
                question_content: this.data.content,
                question_image: this.data.image,
                question_choice: [],
                question_ans: this.data.answer, 
                question_solution: this.data.analyse
            };
            console.log(JSON.stringify(result));
            return result;
        }
    },
    data: function() {
        return {
            data: {
                id: -1,
                parents: [0],
                change_time: "",
                title: "",
                content: "",
				image: [],
                answer: "",
                analyse: "",
                difficulty: 0,
            },
            valid: false
        };
    }
}
</script>
