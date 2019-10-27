<template>
    <div class="brief-answer-component">
        <v-form ref="form" v-model="valid">
            <v-text-field label="Title" v-model="edited_data.title" outlined :readonly="readonly"></v-text-field>
            <v-textarea 
                label="Content"
                v-model="edited_data.content" 
                :rules="[v => !!v || 'Question content is required!']"
                outlined
                auto-grow
                :readonly="readonly"
            ></v-textarea>
            <br/>
			<image-uploader
			  ref="uploader"
			  v-model="edited_data.image"
			  width="50%"
			  label="picture"
			  :readonly="readonly"
			  multiple
			  placeholder="Upload an image if necessary"
			></image-uploader>
			<br/>
            <v-textarea 
                label="Answer"
                v-model="edited_data.answer" 
                :rules="[v => !!v || 'Answer is required!']"
                outlined
                auto-grow
                :readonly="readonly"
            ></v-textarea>
            <br/>
            <v-textarea 
                label="Analysis"
                v-model="edited_data.analysis" 
                :rules="[v => !!v || 'Analysis is required!']"
                outlined
                auto-grow
                :readonly="readonly"
            ></v-textarea>
            <v-list-item>
                <span>Difficulty:</span>
                <v-rating
                    v-model="edited_data.difficulty"
                    color="yellow darken-3"
                    background-color="grey darken-1"
                    :readonly="readonly"
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
                v-if="!readonly && creation"
            >
                Reset
            </v-btn>
            <v-btn v-if="!readonly" @click="cancel">
                Cancel
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
        creation: {
            type: Boolean,
            default: false
        }
    },
    computed: {
        canSubmit() {
            return this.valid;
        }
    },
    created() {
        this.edited_data = this.data;
    },
    methods: {
        submit() {
            this.$emit("submit",this.parse());
        },
        reset() {
            this.$refs.form.reset();
			this.$refs.uploader.reset();
        },
        cancel() {
            this.edited_data = Object.assign({}, this.data);
            this.$emit("cancel");
        },
        submitted() {
            this.data = Object.assign({}, this.edited_data);
        },
        updateData(input) {
            //parse data input from backend
            this.data.id = input.id;
            this.data.parents = input.parents_node;
            this.data.change_time = input.question_change_time;
            this.data.title = input.question_name;
            this.data.content = input.question_content;
			this.data.image = input.question_image;
            this.data.analysis = input.question_solution;
            this.data.difficulty = input.question_level;
            this.data.answer = input.question_ans;
            this.edited_data = Object.assign({}, this.data);
        },
        parse() {
            let result = {
                id: this.edited_data.id,
                parents_node: this.edited_data.parents,
                question_change_time: this.edited_data.change_time,
                question_name: this.edited_data.title,
                question_type: "brief_ans",
                question_level: this.edited_data.difficulty,
                question_content: this.edited_data.content,
                question_image: this.edited_data.image,
                question_choice: [],
                question_ans: this.edited_data.answer, 
                question_solution: this.edited_data.analysis
            };
            console.log(JSON.stringify(result));
            return result;
        }
    },
    data: function() {
        return {
            data: {
                id: -1,
                parents: [],
                change_time: "",
                title: "",
                content: "",
				image: [],
                answer: "",
                analysis: "",
                difficulty: 0,
            },
            edited_data: null,
            valid: false
        };
    }
}
</script>
