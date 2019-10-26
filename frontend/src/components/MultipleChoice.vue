<template>
    <div class="multiple-choice-component">
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
            <image-uploader
			  ref="uploader"
              v-model="data.image"
              width="50%"
              label="picture"
              :readonly="readonly"
              multiple
              placeholder="Upload an image if necessary"
            ></image-uploader>
            <v-list flat>
                <v-list-item two-line>
                    <v-list-item-content align="left">
                    <v-list-item-title>Choices</v-list-item-title>
                    <v-list-item-subtitle :style="answer=='none' ? 'color:red' : 'color:green'">
                        You have chosen {{ answer }}
                    </v-list-item-subtitle>
                    </v-list-item-content>
                </v-list-item>
                <v-list-item-group color="primary">
                    <v-list-item
                        v-for="(item,index) in data.choices"
                        :key="item.name"
                    >
                        <v-list-item-icon>
                            {{ item.name }}
                        </v-list-item-icon>
                        <v-text-field
                            placeholder="Enter choice"
                            v-model="item.content"
                            :rules="[v => !!v || 'Choice content is required!']"
                            :readonly="readonly"
                        ></v-text-field>
                        <v-btn icon small
                            @click="readonly ? ()=>{} : changeRightStatus(item)"
                            >
                            <v-icon color="green" v-if="item.right">mdi-check-circle</v-icon>
                            <v-icon color="red" v-else>mdi-close-circle</v-icon>
                        </v-btn>
                        <v-btn icon small
                            @click="removeChoice(index)" v-if="!readonly">
                            <v-icon color="red">mdi-minus</v-icon>
                        </v-btn>
                    </v-list-item>
                </v-list-item-group>
                <v-btn
                    class="mx-2"
                    block
                    tile
                    dark
                    color="green"
                    @click="addChoice()"
                    v-if="!readonly"
                >
                    Create New
                </v-btn>
            </v-list>
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
    name: "multiple-choice",
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
        answer() {
            let ans=[];
            this.data.rightAnswer.every(item => ans.push(item.name));
            if(ans.length<1) return "none";
            else return ans.join("");
        },
        canSubmit() {
            return this.valid && this.answer!="none";
        }
    },
    methods: {
        addChoice() {
            let length=this.data.choices.length;
            this.data.choices.push({
                name: String.fromCharCode(65+length),
                content: "",
                right: false
            });
        },
        removeChoice(index) {
            if(this.data.choices[index].right)
                this.data.rightAnswer.splice(this.data.rightAnswer.indexOf(this.data.choices[index]));
            this.data.choices.splice(index,1);
            for(var i=0;i<this.data.choices.length;i++)
                this.data.choices[i].name=String.fromCharCode(65+i);
        },
        changeRightStatus(item) {
            item.right=!item.right;
            if(item.right) this.data.rightAnswer.push(item);
            else this.data.rightAnswer.splice(this.data.rightAnswer.indexOf(item),1);
            this.data.rightAnswer.sort((a,b) => a.name>b.name);
        },
        submit() {
            this.$emit("submit",this.parse());
        },
        reset() {
            this.$refs.form.reset();
			this.$refs.uploader.reset();
            this.data.rightAnswer=[];
            this.data.choices= [
                {
                    name: "A",
                    content: "",
                    right: false
                },
                {
                    name: "B",
                    content: "",
                    right: false
                },
                {
                    name: "C",
                    content: "",
                    right: false
                },
                {
                    name: "D",
                    content: "",
                    right: false
                },
            ];
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

            let choices = [];
            input.question_choice.forEach(item => {
                let choiceName = String.fromCharCode(65 + choices.length);
                choices.push({
                    name: choiceName,
                    content: item,
                    right: input.question_ans.indexOf(choiceName)!=-1 ? true : false
                });
            });
            this.data.choices = choices;

            let rightAns = [];
            choices.forEach(item => {
                if(item.right)
                    rightAns.push(item);
            });
            this.data.rightAnswer = rightAns;
        },
        parse() {
            let result = {
                id: this.data.id,
                parents_node: this.data.parents,
                question_change_time: this.data.change_time,
                question_name: this.data.title,
                question_type: "multiple",
                question_level: this.data.difficulty,
                question_content: this.data.content,
                question_image: this.data.image,
                question_choice: [],
                question_ans: [], 
                question_ans_num: this.data.rightAnswer.length,
                question_solution: this.data.analyse
            };
            this.data.rightAnswer.forEach(item => result.question_ans.push(item.name));
            this.data.choices.forEach(item => result.question_choice.push(item.content));
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
                choices: [
                    {
                        name: "A",
                        content: "",
                        right: false
                    },
                    {
                        name: "B",
                        content: "",
                        right: false
                    },
                    {
                        name: "C",
                        content: "",
                        right: false
                    },
                    {
                        name: "D",
                        content: "",
                        right: false
                    },
                ],
                rightAnswer: [],
                analyse: "",
                difficulty: 0,
            },
            valid: false
        };
    }
}
</script>
